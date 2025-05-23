import sqlite3

conn = None

def db_connect():
    global conn
    try:    
        conn = sqlite3.connect('../w16/Database/Courses.db')
        print(f'Database Connected')
    except Exception as e:
        print(f'Error: {e}')
    

def create_table():
    global conn
    if conn is None:
        db_connect()
    cour = conn.cursor()
    cour.execute('''
                SELECT count( name )
                FROM sqlite_master
                WHERE type='table' AND name='students'                 
                ''')
    if cour.fetchone()[0] == 1:
        print('Table students exists')
    else:
        sqlStr = '''
                 CREATE TABLE student (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 gender TEXT NOT NULL,
                 email TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 creat_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                 address TEXT)
                 '''
        cour.execute(sqlStr)
        print(f'Table student created')

def get_student_table_columns():
    global conn
    if conn is None:
        db_connect()
    cour = conn.cursor()
    cour.execute("PRAGMA table_info('student')")
    return cour.fetchall()

def insert_student(stud):
    global conn

    stud_name = stud['stud_name']
    stud_gender = stud['stud_gender']
    stud_email = stud['stud_email']
    stud_phone = stud['stud_phone']
    stud_address = stud['stud_address']

    if conn is None:
        db_connect()

    cour = conn.cursor()
    cour.execute('''
                 INSERT INTO student (name , gender  , email , phone  , address)
                 VALUES (?,?,?,?,?)
                 ''' ,  (stud_name , stud_gender , stud_email , stud_phone  , stud_address))
    conn.commit()
    print(f'Student: {stud_name} inserted')

def list_students():
    global conn
    if conn is None:
        db_connect()
    cour = conn.cursor()
    cour.execute('SELECT * FROM student')
    students = cour.fetchall()
    for stud in students:
        print(f'id: {stud[1]:10} name: {stud[2]:14} gender: {stud[3]:3}', end = '')
        print(f'mail: {stud[4]:18} phone: {stud[5]:15} address: {stud[6]:20}')


def menu():
    print('\n0. Exit')
    print('1. Create student Table')
    print('2. Insert student data')
    print('3. List student')
    print('4. Search student')
    print('5. Update data')
    print('6. Delete data')
    print('7. Get student table columns')
    return input('Enter your choice: ')

def exit():
    global conn
    if conn is not None:
        conn.close()
        print('Connection closed')
    print('Exiting...')
    return False

def search_student(stud_id):
    global conn
    if conn is None:
        db_connect()
    cour = conn.cursor()
    cour.execute('SELECT * FROM student WHERE name = ?' , (stud_id,))
    stud = cour.fetchone()
    return stud

def update_student(stud_id):
    student = search_student(stud_id)
    if student is not None:
        new_id = input('Enter new student ID: ')
        new_name = input('Enter new student name: ')
        new_gender = input('Enter new gender: ')
        new_phone = input('Enter new phone: ')
        new_email = input('Enter new email: ')
        new_address = input('Enter new address: ')
        cour = conn.cursor()
        cour.execute('''
                    UPDATE student SET name = ? , name = ? , gender = ? , department = ? , email = ? , phone = ? , address = ? WHERE id = ?
                     ''' , (new_id , new_name , new_gender , new_email , new_phone , new_address))

def delete_student(stud_id):
    student = search_student(stud_id)
    if student is not None:
        flag = input('Are you sure you want to delete this student? (y/n)')
        if flag.lower() == 'y':
            cour = conn.cursor()
            cour.execute('DELETE FROM student WHERE name = ?' , (student[0],))
            conn.commit()
            print('Student deleted')
        else:
            print('User cancel student deletion')
    else:
        print('Student not found')

def main():
    while 1:
        choice = menu()
        if choice == '0':
            if not exit():
                break
        elif choice == '1':
            create_table()
        elif choice == '2':
            print('---'*15)
            # stud_id = input('student ID: ')
            stud_name = input('student name: ')
            stud_gender = input('gender: ')
            # stud_dept = input('dept: ')
            stud_email = input('email: ')
            stud_phone = input('phone: ')
            stud_address = input('address: ')
            insert_student(stud_name , stud_gender , stud_email , stud_phone , stud_address)
            print('---'*15)
        elif choice == '3':
            print('---'*15)
            list_students()
            print('---'*15)
        elif choice == '4':
            stud = search_student(input('Enter student ID: '))
            if stud is not None: 
                print(f'id: {stud[1]:10} name: {stud[2]:14} gender: {stud[3]:3} dept: {stud[4]:20}' , end = '')
                print(f'mail: {stud[5]:10} phone: {stud[6]:15} address: {stud[7]:20}')
            else:
                print('Student not found')
        elif choice == '5':
            update_student(input('Enter student ID: '))

        elif choice == '6':
            delete_student(input('Enter student ID: '))

        elif choice == '7':
            print('---'*15)
            columns = get_student_table_columns()
            for i in columns:
                print(i)
            print('---'*15)


if __name__ == "__main__":
    db_connect()
    # create_table()
    # `columns = get_student_table_columns()
    # for i in columns:
    #     print(i)

    # stud = {
    #     'stud_name' : "黃軍博",
    #     'stud_gender' : "male",
    #     'stud_email' : 'yacolate0519@gmail.com',
    #     'stud_phone' : '0928590005',
    #     'stud_address' : "iOS Club社辦"
    # }

    # insert_student(stud)

    main()

    conn.close()
    print('Connection closed')

