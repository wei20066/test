import sqlite3
 
DB_Name = 'test.db'# 连接数据库，如果不存在则会在当前目录创建
Table_Name = 'STUDENT' # 连接数据库，如果不存在则会在当前目录创建
conn = sqlite3.connect(DB_Name)
print('连接数据库%s成功' % (DB_Name))
try:	# 创建游标
	cursor = conn.cursor()	# 创建STUDENT表的SQL语句，默认编码为UTF-8    
	SQL = ''' CREATE TABLE %s ( SNO CHAR(10),SNAME VARCHAR(20) NOT NULL,PRIMARY KEY(SNO)) ''' % (Table_Name)	# 创建数据库表
	cursor.execute(SQL)	# 提交到数据库
	conn.commit()
	print('创建数据库表%s成功' % (Table_Name))
except Exception as e:
	print(e)    # 回滚
	conn.rollback()
	print('创建数据库表%s失败' % Table_Name)
#finally:    # 关闭数据库    
	#conn.close()
SQL = ''' INSERT INTO STUDENT VALUES('2016081111','张三'),('2016081112','李四'),('2016081113','王五'); ''' # 插入数据
try:
	cursor.execute(SQL) # 提交到数据库  
	conn.commit()    
	print('插入数据到表STUDENT成功')
except Exception as e:
	print(e)    # 回滚
	conn.rollback()
	print('插入数据到表STUDENT失败')
#finally:    # 关闭数据库
#	conn.close()
SQL = ''' SELECT * FROM STUDENT; '''  # 查询数据
try:
 	cursor.execute(SQL)     # 获取一条数据
 	one = cursor.fetchone()
 	print(one)     # 获取所有数据
 	for row in cursor.fetchall():
 		print(row) 
except Exception as e:
    print(e)
    print('查询数据失败')
finally:    # 关闭数据库    
 	conn.close()