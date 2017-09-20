import pymysql as mariadb

from config import botconfig

def insert_stats(user_id, user_name, file_id, file_path, imgur_link):
    conn = mariadb.connect(user=botconfig.db_user, passwd=botconfig.db_pass, db=botconfig.db_name, host=botconfig.db_host)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users_stats (user_id, user_name, file_id, file_path, imgur_link) VALUES (%s,%s,%s,%s,%s)", (user_id, user_name, file_id, file_path, imgur_link))
    conn.commit()
    cursor.close()
    conn.close()

def get_stats(user_id):
    conn = mariadb.connect(user=botconfig.db_user, passwd=botconfig.db_pass, db=botconfig.db_name, host=botconfig.db_host)
    cursor = conn.cursor()
    cursor.execute("SELECT count(id) FROM users_stats WHERE user_id = " + str(user_id))
    result = []
    for row in cursor:
        result.append(row[0])
    cursor.execute("SELECT count(id) FROM users_stats WHERE user_id = " + str(user_id) + " AND imgur_link LIKE 'http%'")
    for row in cursor:
        result.append(row[0])
    cursor.close()
    conn.close()
    return result

def get_global_stats(user_id):
    conn = mariadb.connect(user=botconfig.db_user, passwd=botconfig.db_pass, db=botconfig.db_name, host=botconfig.db_host)
    cursor = conn.cursor()
    cursor.execute("SELECT count(id) FROM users_stats ")
    result = []
    for row in cursor:
        result.append(row[0])
    cursor.execute("SELECT count(id) FROM users_stats WHERE imgur_link LIKE 'http%'")
    for row in cursor:
        result.append(row[0])
    cursor.close()
    conn.close()
    return result
