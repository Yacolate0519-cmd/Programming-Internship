import graphviz

# 建立流程圖
dot = graphviz.Digraph(format='png')
dot.attr(rankdir='LR', size='10')

# 開始節點
dot.node('Start', '程式啟動')

# 等待連線
dot.node('WaitClients', '等待玩家加入 (clients < 2)\nUDP recvfrom')
dot.node('AddClient', '加入 clients 名單\n使用 with lock 確保同步')

# 玩家角色選擇階段
dot.node('HandleP1', '玩家一選角\nserver.sendto 選單 → recvfrom → 建立角色')
dot.node('HandleP2', '玩家二選角\nserver.sendto 選單 → recvfrom → 建立角色')

# 顯示角色資訊
dot.node('ShowStatus', '雙方顯示角色狀態\n使用 get_status_bar')

# 對戰迴圈
dot.node('BattleLoop', '回合迴圈：交替進行')
dot.node('SendSkillList', 'server.sendto\n傳送技能選單')
dot.node('RecvSkillChoice', 'recvfrom 等待技能選擇')
dot.node('FP Check', 'FP 是否足夠？')
dot.node('ExecuteSkill', '執行攻擊 → 改變 HP/FP')
dot.node('SendResult', '雙方顯示攻擊結果')

# 勝負結算
dot.node('CheckDead', '是否有角色死亡？')
dot.node('GameOver', '顯示獲勝訊息\nserver.sendto\n==Game Over==')

# 結束
dot.node('End', '結束對戰並關閉伺服器')

# 連線流程
dot.edge('Start', 'WaitClients')
dot.edge('WaitClients', 'AddClient', label='新玩家加入')
dot.edge('AddClient', 'WaitClients', label='clients < 2')
dot.edge('AddClient', 'HandleP1', label='clients == 2')
dot.edge('HandleP1', 'HandleP2')
dot.edge('HandleP2', 'ShowStatus')
dot.edge('ShowStatus', 'BattleLoop')

# 對戰流程
dot.edge('BattleLoop', 'SendSkillList')
dot.edge('SendSkillList', 'RecvSkillChoice')
dot.edge('RecvSkillChoice', 'FP Check')
dot.edge('FP Check', 'SendSkillList', label='不足 → 重選')
dot.edge('FP Check', 'ExecuteSkill', label='足夠')
dot.edge('ExecuteSkill', 'SendResult')
dot.edge('SendResult', 'CheckDead')
dot.edge('CheckDead', 'GameOver', label='死亡')
dot.edge('CheckDead', 'BattleLoop', label='未死亡')

# 結束流程
dot.edge('GameOver', 'End')

dot.render('/mnt/data/pvp_server_flowchart', cleanup=False)
'/mnt/data/pvp_server_flowchart.png'
