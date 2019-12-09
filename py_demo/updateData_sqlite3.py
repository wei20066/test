import sqlite3
DB_Name = 'test.db'# 连接数据库，如果不存在则会在当前目录创建
conn = sqlite3.connect(DB_Name)
try:    # 创建游标
    cursor = conn.cursor()    # 查询数据的SQL语句
    SELECT_SQL = ''' SELECT * FROM STUDENT; '''    # 修改数据的SQL语句
    UPDATE_SQL = ''' UPDATE STUDENT SET SNAME='%s' WHERE SNO='%s' ''' % ('李华', '2016081111')     # 修改前
    print('修改前')    
    cursor.execute(SELECT_SQL)    
    for row in cursor.fetchall():
    	print(row)    # 修改数据
    cursor.execute(UPDATE_SQL)    # 提交到数据库
    conn.commit()     # 修改后
    print('修改后')
    cursor.execute(SELECT_SQL)
    for row in cursor.fetchall():
   		print(row)
except Exception as e:
    print(e)
    print('修改数据失败')
finally:    # 关闭数据库
    conn.close()