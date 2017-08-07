import pymysql as mariadb

from config import botconfig

def insert_stats(user_id, user_name, file_id, file_path, imgur_link):
    conn = mariadb.connect(user=botconfig.db_user, passwd=botconfig.db_pass, db=botconfig.db_name, host=botconfig.db_host)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users_stats (user_id, user_name, file_id, file_path, imgur_link) VALUES (%s,%s,%s,%s,%s)", (user_id, user_name, file_id, file_path, imgur_link))
    conn.commit()
    cursor.close()
    conn.close()