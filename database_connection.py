import pymysql

donation_db_connection = pymysql.connect(
    host='localhost',
    user='mac',
    password='888',
    database='donation_database',
    port=3306,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

