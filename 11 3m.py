import sqlite3

try:
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor

except sqlite3.DatabaseError:
    print('ошибка подключения')

finally:
    connection.close()

class User:
    def __init__(self,name,surname,gender):
        self.name=name
        self.surname=surname
        self.gender=gender

def get_users_list(cursor):
    command='''
    SELECT * FROM users;
    '''
    cursor.execute(command)
    result=cursor.execute(command)
    user=result.fetchall()
    print(user)


def create_table_user(cursor):
    command='''
    CREATE TABLE IF NOT EXISTS users(
       id INTEGER PRIMARY KEY,
       name TEXT,
       surname TEXT,
       gender TEXT);
    '''
    cursor.execute(command)
   



def add_user(cursor,user):
    command= '''
    INSERT INTO users (name,surname,gender) VALUES (?,?,?);
    '''
    cursor.execute(command,(user.name,user.surname,user.gender))

def get_user(cursor):
    command='''
    SELECT * FROM users WHERE id=?;
    '''
    result=cursor.execute(command,(user_id))
    user=result.fetchall()
    print(user)

def update_user_name(cursor,value,user_id):
    command='''
    UPDATE users SET name=? WHERE id=?;
    '''
    cursor.execute(command)

def delete_user(cursor):
    command='''
    DELETE FROM users;
    '''
    cursor.execute(command)

if __name__=='__main__':
    with sqlite3.connect('data.bd') as cursor:
        create_table_user(cursor)
        delete_user(cursor)
        add_user(cursor,User(name='Max', surname='Ivanov',gender='male'))
        add_user(cursor,User(name='Marina', surname='Ivanova',gender='female'))
        add_user(cursor,User(name='Ira', surname='Gubova',gender='female'))
        get_users_list(cursor)
        get_user(cursor,'1')
        update_user_name(cursor,'Misha',1)
        get_user(cursor,'1')


