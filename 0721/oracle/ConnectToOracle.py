import config
import cx_Oracle
def main():
    conn = cx_Oracle.connect(config.dblink)
    #print(config.dbname+'/'+config.dbpwd+'@'+config.dbhost+'/'+config.dbservs)
    #conn = cx_Oracle.connect('test/test@128.160.187.34/xe')
    curs = conn.cursor()
    sql = 'SELECT * FROM dual'  # sql语句
    rr= curs.execute(sql)
    row = curs.fetchone()
    print(row[0])
    assert row[0] == 'X' , '连接失败！'
    curs.close()
    conn.close()
if __name__ == '__main__':
    main()