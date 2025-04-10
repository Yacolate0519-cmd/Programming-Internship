import socket
import threading
from character import Charmander, Blastoise, Bulbassaur
from colorama import init, Fore, Style

init(autoreset=True)

def get_bar(current, max_value, length=20, color=Fore.GREEN):
    filled_length = int(length * current // max_value)
    bar = "█" * filled_length + '░' * (length - filled_length)
    return f'{color}[{bar}]{Style.RESET_ALL} {current}/{max_value}'

def get_status_bar(pokemon):
    hp_bar = get_bar(pokemon.hp, pokemon.max_hp, color=Fore.RED)
    fp_bar = get_bar(pokemon.fp, 60 if pokemon.fp <= 60 else pokemon.fp, color=Fore.BLUE)
    return f"{pokemon.name} HP: {hp_bar}\n{' ' * len(pokemon.name)} FP: {fp_bar}"

characters = {
    '1': Charmander("小火龍", 100, 60, 'fire'),
    '2': Blastoise("傑尼龜", 100, 30, 'water'),
    '3': Bulbassaur("妙蛙種子", 100, 90, 'grass')
}

clients = []
lock = threading.Lock()

def handle_player(index, server):
    addr = clients[index]
    server.sendto("請選擇角色:\n1. 小火龍\n2. 傑尼龜\n3. 妙蛙種子\n".encode('utf-8'), addr)

    msg, _ = server.recvfrom(1024)
    choice = msg.decode('utf-8').strip()
    if choice not in characters:
        choice = '1'

    player = characters[choice]
    server.sendto(f'你選擇了 {player.name}'.encode('utf-8'), addr)
    return player

def pvp_battle(server, addr1, addr2):
    player1 = handle_player(0, server)
    player2 = handle_player(1, server)

    players = [(player1, addr1), (player2, addr2)]

    for player, addr in players:
        enemy = player2 if player == player1 else player1
        msg = "🎮 對戰開始！\n你選擇的角色：\n" + get_status_bar(player)
        msg += "\n對手的角色：\n" + get_status_bar(enemy)
        server.sendto(msg.encode('utf-8'), addr)

    turn = 0
    while True:
        attacker, attacker_addr = players[turn % 2]
        defender, defender_addr = players[(turn + 1) % 2]

        status = f"\n{attacker.name} 的回合\n\n{get_status_bar(attacker)}\n{get_status_bar(defender)}\n\n技能選擇:\n"
        for i, (skill_name, skill_info) in enumerate(attacker.skill.items(), 1):
            status += f"{i}. {skill_name} (傷害: {skill_info['damage']}, FP: {skill_info['require_fp']})\n"
        server.sendto(status.encode('utf-8'), attacker_addr)

        msg, _ = server.recvfrom(1024)
        choice = msg.decode('utf-8').strip()

        try:
            skill_name = list(attacker.skill.keys())[int(choice) - 1]
            skill_info = attacker.skill[skill_name]

            if attacker.fp < skill_info['require_fp']:
                fail_msg = f"⚠️ FP 不足，無法施放「{skill_name}」，請重新選擇。\n"
                server.sendto(fail_msg.encode('utf-8'), attacker_addr)
                continue

            old_hp = defender.hp
            attacker.attack(skill_name, defender)
            result = f"\n{attacker.name} 使用了 {skill_name}，{defender.name} 從 {old_hp} → {defender.hp}\n"

        except Exception:
            result = "輸入無效，請重新輸入。\n"
            server.sendto(result.encode('utf-8'), attacker_addr)
            continue

        server.sendto(result.encode('utf-8'), attacker_addr)
        server.sendto(result.encode('utf-8'), defender_addr)

        if defender.dead():
            win_msg = f"{defender.name} 被擊敗，{attacker.name} 獲勝！\n" + '=='*9 +"Game Over" + '=='*9
            server.sendto(win_msg.encode('utf-8'), attacker_addr)
            server.sendto(win_msg.encode('utf-8'), defender_addr)
            break

        turn += 1

def wait_for_clients():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '192.168.1.110'
    port = 1024
    server.bind((host, port))
    print("✅ Server 啟動，等待兩位玩家加入...")

    while len(clients) < 2:
        msg, addr = server.recvfrom(1024)
        with lock:
            if addr not in clients:
                clients.append(addr)
                print(f"玩家加入：{addr}")
                server.sendto("等待另一位玩家加入...".encode('utf-8'), addr)

    print("開始對戰！")
    pvp_battle(server, clients[0], clients[1])
    server.close()

if __name__ == '__main__':
    wait_for_clients()
