import pymysql.cursors

config = {'host': '127.0.0.1',
          'port': 3306,
          'user': 'root',
          'password': '',
          'db': 'test',
          'charset': 'utf8mb4',
          'cursorclass': pymysql.cursors.DictCursor}
connection = pymysql.connect(**config)

try:
    with connection.cursor() as cursor:
        sql = 'select t.id,t.name,t.mobile,t.birthday,t.add,t.amount from mh_user t where t.birthday>"2018-08-01"'
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
    connection.commit()
finally:
    connection.close()


