import sqlite3 
dbConn = sqlite3.connect('../w16/Database/Test.db')
dbCursor = dbConn.cursor()

conn = None

def createTable():
    global conn
    sqlStr = '''
            SELECT count( name )
            FROM sqlite_master
            WHERE type = 'table' AND name = 'student';
            '''
    dbCursor.execute(sqlStr)
    if dbCursor.fetchone()[0] == 1:
        print(f'Table student already exists')
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
        dbCursor.execute(sqlStr)
        print(f'Table student created')
    
if __name__ == '__main__':
    createTable()
    dbConn.close()
