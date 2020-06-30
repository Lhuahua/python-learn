##第四、五章：操作列表，if语句
##一、for循环遍历列表
##二、创建数值列表,统计计算min/max/sum
    ##list(range(a,b，c)) {包首不包尾}/append()/列表解析
##三、列表切片{包首不包尾，下标从0开始}：复制列表{a=b[:]}
##四、元组：不可变列表（），不可改值，可重新初始化赋值
##五、if语句
	##条件测试：==/！=/and/or/in/not in
	##if语句 
		##if 条件测试：
			##do somthing
	##if/if-else/if-elif-else


values = []
values2 = []

for value in range(1,11):
		values.append(value**3)

##列表解析：列表名=[表达式 for循环]		注意：没有冒号
values2=[value**3 for value in range(1,11)]

for value in values2:
	print(value)
	
##分片
print("The three items in the list are")
for value in values[0:3]:
	print(value)

##元组
foods = ('ppp','sasa','dada')
