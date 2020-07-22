import config
import cx_Oracle
conn = cx_Oracle.connect(config.dblink)
sql="update  test set col3 ='test' where id = '1'"
cursor=conn.cursor()
cursor.execute(sql)
conn.commit()
cursor.close ()
conn.close ()