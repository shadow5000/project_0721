import config
import cx_Oracle
conn = cx_Oracle.connect(config.dblink)
cursor = conn.cursor ()
cursor.execute ("CREATE TABLE TEST(ID INT, COL1 VARCHAR(32), COL2 VARCHAR(32), COL3 VARCHAR(32))")
cursor.execute ("INSERT INTO TEST (ID, COL1, COL2, COL3)VALUES(1, 'a', 'b', 'c')")
cursor.execute ("INSERT INTO TEST (ID, COL1, COL2, COL3)VALUES(2, 'aa', 'bb', 'cc')")
cursor.execute ("INSERT INTO TEST (ID, COL1, COL2, COL3)VALUES(3, 'aaa', 'bbb', 'ccc')")
conn.commit()
cursor.close ()
conn.close ()