import MySQLdb

connection = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='python_db')
    
cursor = connection.cursor()
 
# ここに実行したいコードを入力します
cursor.execute("SELECT * FROM sample")
rows = cursor.fetchall()
for row in rows:
  print (row)

# 保存を実行
connection.commit()
 
# 接続を閉じる
connection.close()