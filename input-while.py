# -*- coding:utf-8 -*-

##第七章:用户输入和while循环
 #一、input()
 #二、while循环：让用户选择何时退出/continue、break/处理列表和字典

	
age=int(input('How old are you? '))
price = 0
while age > 0:
	if age < 3:
		price = 0
	elif age < 13:
		price = 10
	else:
		peice = 15
	print('Price is '+str(price)) 
	age=int(input('How old are you? '))

##while循环用来修改列表
sandwich_orders = ['aa','bb','cc','aa']
sandwich_finished = []

##for循环是遍历列表的有效方式，但是修改列表导致python难以跟踪其中的元素
##如下运行结果sandwich_order为[aa]，sandwich_finished为[aa,bb]
##for sandwich in sandwich_orders:
	##print('I made your '+sandwich+' sandwich.')
	##sandwich_orders.pop()
	##sandwich_finished.append(sandwich)
	
##while循环：在列表之间移动元素
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made your '+sandwich+' sandwich.')
	sandwich_finished.append(sandwich)
	
for sandwich in sandwich_orders:
	print(sandwich)
print()
for sandwich in sandwich_finished:
	print(sandwich)

##while循环：删除列表的特定值
while 'aa' in sandwich_finished:
	sandwich_finished.remove('aa')
	
#while循环：使用用户输入填充字典
holiday={}
flag = True
while flag:
	name = input('What is your name? ')
	place = input('Which place you want to go? ')
	holiday[name] = place
	repeat = input('Any one?(yes or no)')
	if repeat == 'no':
		flag = False

for name,place in holiday.items():
	print(name+' want to visit '+place)
		
