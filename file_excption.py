##第十章：文件和异常
 #一、文件读取数据
 #二、写入文件
 #三、异常
 #四、数据存储（JSON）
 
##文件的读取
 #with关键字：open()返回的文件对象只在with代码块可用，即代码块执行完即关闭文件
 #read()：返货对象
 #readline（）：返回列表
with open('learning.txt') as file_object:
	contex = file_object.read()
print(contex)
	
with open('learning.txt') as f:
	for line in f:
		print(line.strip())

with open('learning.txt') as f:
	lines = f.readlines()
for line in lines:
	print(line.strip())
#字符串的操作
for line in lines:
	if 'c' in line:
		line.replace('c','cccc')
	print(line.strip())

##写入文件
 #读取模式（r）/写入模式（w）{清空原文件}/附加模式（a）/读取和写入模式（r+）
 #write()
with open('learning.txt','a') as f:
	 f.write('\ndadadada')
	 
##异常
 #try-except-else
 #ZeroDivisionError/FileNotoundError/ValueError
 #pass语句，在代码块中python什么都不做 
str1 = input('Input a num! ')
str2 = input('Input another num! ')
try:
	num1 = int(str1)
	num2 = int(str2)
except ValueError:
	print('Erro')
else:
	print(num1+num2)
 
##存储数据：将python数据结构存储到文件中
 #读入文件：json.dump(obj,f_obj)
 #读到内存：obj = json.load(f_obj)
import json
numbers = [1,2,3,4,5]
with open('number.json','w') as f_obj:
	json.dump(numbers,f_obj)
