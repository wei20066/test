import sqlite3
DB_Name = 'test.db'# 连接数据库，如果不存在则会在当前目录创建
conn = sqlite3.connect(DB_Name)
try: # 创建游标
	cursor = conn.cursor()    # 查询数据的SQL语句
	SELECT_SQL = ''' SELECT * FROM STUDENT; '''    # 删除数据的SQL语句
	DELETE_SQL = ''' DELETE FROM STUDENT WHERE SNO='%s' ''' % ('2016081111')     # 删除前
	print('删除前')
	cursor.execute(SELECT_SQL)
	for row in cursor.fetchall():
		print(row)    # 删除数据
	cursor.execute(DELETE_SQL)    # 提交到数据库
	conn.commit()     # 删除后    
	print('删除后')
	cursor.execute(SELECT_SQL)
	for row in cursor.fetchall():
	    print(row)
except Exception as e:
	print(e)    
	print('删除数据失败')
finally:    # 关闭数据库
		conn.close()
