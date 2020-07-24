#to_date('2013-2-26 11:07:25' , 'yyyy-mm-dd hh24:mi:ss')
data_list=['000001', '华夏成长混合', '2020-07-23', '1.4460', '1.4289', '-1.19', '2020-07-24 09:36']
print(data_list)
print(type(data_list))

str1="to_date('"+data_list[2]+"' ,'yyyy-mm-dd')"

str2="to_date('"+data_list[-1]+" ','yyyy-mm-dd hh24:mi:ss')"
print("str1: %s" %str2 )
print("str1类型：%s" %type(str2))
print('-------------------------------------------')


# data_list=data_list[0:-1]
# print(data_list)
# print(type(data_list))
# print('--------------------------------------------')

data_list[2]=str1
data_list[-1]=str2
print(data_list)
print(type(data_list))


insert_sql='insert into fund_'+'tm'+' values'+str(tuple(data_list))
insert_sql=insert_sql.replace('"','')
print('insert_sql:',insert_sql)