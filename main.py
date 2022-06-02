import mysql.connector


def create_Schema():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Deniz35eren76."
    )
    myCursor = mydb.cursor()
    myCursor.execute("DROP DATABASE IF EXISTS SE_226")
    sql = '''CREATE DATABASE SE_226'''
    myCursor.execute(sql)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Deniz35eren76.",
        database="SE_226"
    )
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


def create_Table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Deniz35eren76.",
        database="SE_226"
    )
    myCursor = mydb.cursor()
    myCursor.execute("DROP TABLE IF EXISTS Marvel")
    sql = '''CREATE TABLE Marvel(
                  ID INT,
                  MOVIE VARCHAR(255),
                  DATE VARCHAR(255),
                  MCU_PHASE VARCHAR(220)
                )'''
    myCursor.execute(sql)


def insert(address):
    path = open('/Users/denizterziler/Desktop/marvel.txt')
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Deniz35eren76.",
            database="SE_226"
        )
        myCursor = mydb.cursor()
        while path:
            marvel = path.readline()
            if marvel == "":
                break
            splitLines = marvel.split()
            sql = """INSERT INTO Marvel(ID,MOVIE,DATE,MCU_PHASE) VALUES (%s,%s,%s,%s)"""
            record = (splitLines[0], splitLines[1], splitLines[2], splitLines[3])
            myCursor.execute(sql, record)
            mydb.commit()

    except mysql.connector.Error as error:
        print("Failed to insert into MySql Table {}".format(error))
    finally:
        if mydb.is_connected():
            myCursor.close()
            mydb.close()
            print("MYSQL connection is closed")


def print_all_movies():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Deniz35eren76.",
        database="SE_226"
    )
    myCursor = mydb.cursor()
    query = "SELECT * FROM Marvel"
    myCursor.execute(query)
    rows = myCursor.fetchall()
    for row in rows:
        print(row)

    mydb.close()


def delete_from_table(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Deniz35eren76.",
        database="SE_226"
    )
    myCursor = mydb.cursor()
    query = "DELETE FROM Marvel WHERE MOVIE = %s"
    data = (name,)
    myCursor.execute(query, data)
    mydb.commit()
    mydb.close()


def list_phase_2():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Deniz35eren76.",
        database="SE_226"
    )
    myCursor = mydb.cursor()
    query = "SELECT * FROM Marvel WHERE MCU_PHASE = 'Phase2'"
    myCursor.execute(query)
    rows = myCursor.fetchall()
    for row in rows:
        print(row)

    mydb.close()


def fix_Thor():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Deniz35eren76.",
        database="SE_226"
    )
    myCursor = mydb.cursor()
    query = "UPDATE Marvel SET DATE = 'November3,2017' WHERE MOVIE = 'Thor:Ragnarok'"
    myCursor.execute(query)
    mydb.commit()
    mydb.close()


def main():
    create_Table()
    insert('/Users/denizterziler/Desktop/marvel.txt')
    print("ALL MOVIES BEFORE ANY EXECUTION")
    print_all_movies()
    delete_from_table('TheIncredibleHulk')
    print("ALL MOVIES AFTER HULK DELETED")
    print_all_movies()
    print("PHASE 2 MOVIES")
    list_phase_2()
    fix_Thor()
    print("AFTER THOR HAS BEEN FIXED")
    print_all_movies()


if __name__ == '__main__':
    main()
