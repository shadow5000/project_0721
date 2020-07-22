import config
import cx_Oracle
def main():
    conn = cx_Oracle.connect(config.dblink)
    sql='select * from TEST'
    cursor=conn.cursor()
    cursor.execute(sql)
    rows= cursor.fetchall()
    # print(type(rows))
    # print(rows)
    # for row in rows :
    #     print('%d') % (row[0])
    for row in rows :
        print ('%d,%s,%s,%s' %(row[0],row[1],row[2],row[3]))
    print('Number of rows returned: %d' %(cursor.rowcount))
    cursor.execute ("SELECT * FROM TEST")
    while (1):
      row = cursor.fetchone()
      if row == None:
        break
      print ("%d, %s, %s, %s" % (row[0], row[1], row[2], row[3]))
    print ("Number of rows returned: %d" % (cursor.rowcount))
    cursor.close ()
    conn.close ()
if __name__ == '__main__':
    main()