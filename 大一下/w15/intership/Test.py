import re

def check_syntax(file_path):
    """
    Check Python code syntax in the given file.
    """
    try:
        # Read the code file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Initialize error counter
        errors_found = False
        
        # Check each line of code
        for i, line in enumerate(lines):
            line = line.strip()
            line_number = i + 1
            
            # Skip empty lines
            if not line:
                continue
            
            # Check def syntax - should end with '():' or '():'
            if line.startswith('def '):
                # Check if function has parentheses and colon
                if not re.match(r'def\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(\s*.*\s*\)\s*:', line):
                    if not '(' in line or not ')' in line:
                        print(f"Line {line_number} {line} ➜ 錯誤：函數定義缺少括號 ()")
                        errors_found = True
                    elif not line.rstrip().endswith(':'):
                        print(f"Line {line_number} {line} ➜ 錯誤：缺少冒號")
                        errors_found = True
            
            # Check if/elif syntax - should have a condition and end with colon
            elif line.startswith('if ') or line.startswith('elif '):
                if not line.rstrip().endswith(':'):
                    print(f"Line {line_number} {line} ➜ 錯誤：if/elif 敘述缺少冒號")
                    errors_found = True
            
            # Check else syntax - should just be 'else:'
            elif line.startswith('else'):
                if not re.match(r'else\s*:', line):
                    print(f"Line {line_number} {line} ➜ 錯誤：else 敘述格式錯誤")
                    errors_found = True
            
            # Check for syntax - should include 'in' and end with colon
            elif line.startswith('for '):
                if not ' in ' in line:
                    print(f"Line {line_number} {line} ➜ 錯誤：for 缺少 in")
                    errors_found = True
                elif not line.rstrip().endswith(':'):
                    print(f"Line {line_number} {line} ➜ 錯誤：for 敘述缺少冒號")
                    errors_found = True
            
            # Check while syntax - should have a condition and end with colon
            elif line.startswith('while '):
                if not line.rstrip().endswith(':'):
                    print(f"Line {line_number} {line} ➜ 錯誤：while 敘述缺少冒號")
                    errors_found = True
            
            # Check print syntax - should include parentheses
            elif 'print' in line:
                # Look for print without proper parentheses
                if re.search(r'\bprint\s+(?!\()', line) or re.search(r'\bprint\(', line) and not re.search(r'\bprint\s*\(.*\)', line):
                    print(f"Line {line_number} {line} ➜ 錯誤：print 敘述缺少括號 ()")
                    errors_found = True
        
        # If no errors found, report success
        if not errors_found:
            print("沒有發現語法錯誤！")
            
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{file_path}'")
    except Exception as e:
        print(f"錯誤：{str(e)}")

if __name__ == "__main__":
    file_path = input("請輸入要檢查的Python程式碼檔案路徑：")
    check_syntax(file_path)