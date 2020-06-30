##第八章：函数
 #一、定义
 #二、传递实参：位置实参、关键字实参、设置默认值、实参变可选、传递任意数量的实参、传递列表
 #三、返回值：return()，返回字典
 #四、函数封装：import
 
def favorite_book(title,price=11):
     """文档字符串"""
     print('One of my favorite book is '+title+'. The price is '+ str(price))

##位置实参调用函数
favorite_book('dad',21)
##关键字实参调用函数
favorite_book(title='dad',price=21)
##设置默认值（等号两边不要有空格）
favorite_book('sas')
##让实参变可选：设置默认值为空字符串

##返回字典,结合7while循环（8-7）
def make_album(singer,album_name,num=''):
    '''创建一个描述音乐专辑的字典'''
    album={'singer':singer,'album_name':album_name}
    if num:
        album['num'] = num
    return album
msg = 'yes'
while msg == 'yes':
    singer = input('Input the name og singer! ')
    album_name = input('Input the name of album! ')
    album = make_album(singer,album_name)
    print(album)
    msg = input('Continue?')
    
album2 = make_album('bb','eerff',10)
print(album2)

##传递任意数量的实参
 #*toppings：创建一个空元组，将接收到的所有实参值都装到元组中
 #**usr_info：创建空字典，将接收的所有名称-值对封装到字典中
 
 ##函数模块化调用(放在文件开头)
  #import module_name as new_name//////module_name.function_name()
  #from module_name import function_name as new_name/// function_name()
  #from module_name import *
