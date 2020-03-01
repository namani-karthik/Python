import MySQLdb
conn=MySQLbd.connect(host='localhost',database='World',user='root',password='123')

cursor=conn.cursor()

cursor.execute('select * from emptab')

row=cursor.fetchone()

while row is not none:
    print(row)
    row=cursor.fetchone()

cursor.close()
conn.close()
