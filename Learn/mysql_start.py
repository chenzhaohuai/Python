import mysql.connector
from IPython import display

conn = mysql.connector.connect(user='root3', password='root3', host = '172.18.7.141',port='3306' , database='zsy_cloud_business')

cursor = conn.cursor()

cursor.execute('select * from exam')

values = cursor.fetchall()

for x in values:
  print(x)
# display(values)