# -*- coding:utf-8 -*-

##������:�û������whileѭ��
 #һ��input()
 #����whileѭ�������û�ѡ���ʱ�˳�/continue��break/�����б���ֵ�

	
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

##whileѭ�������޸��б�
sandwich_orders = ['aa','bb','cc','aa']
sandwich_finished = []

##forѭ���Ǳ����б����Ч��ʽ�������޸��б���python���Ը������е�Ԫ��
##�������н��sandwich_orderΪ[aa]��sandwich_finishedΪ[aa,bb]
##for sandwich in sandwich_orders:
	##print('I made your '+sandwich+' sandwich.')
	##sandwich_orders.pop()
	##sandwich_finished.append(sandwich)
	
##whileѭ�������б�֮���ƶ�Ԫ��
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made your '+sandwich+' sandwich.')
	sandwich_finished.append(sandwich)
	
for sandwich in sandwich_orders:
	print(sandwich)
print()
for sandwich in sandwich_finished:
	print(sandwich)

##whileѭ����ɾ���б���ض�ֵ
while 'aa' in sandwich_finished:
	sandwich_finished.remove('aa')
	
#whileѭ����ʹ���û���������ֵ�
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
		
