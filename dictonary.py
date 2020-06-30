##第六章：字典
##一、字典的定义
##二、遍历字典:items()/keys(){默认，sorted()顺序遍历}/vlaues(){set()可以剔除重复项}
##三、嵌套:列表中嵌套字典，字典中嵌套列表

##定义
friends={
	'first_name' :'aaa',
	'last_name' :'aaa',
	'age' : 1,
	'city' : 'aaa',
}

print(friends['age'])

##遍历
for key,value in friends.items():
	print('My friend"s '+key+' is '+str(value))

##嵌套：字典列表
teachers={
	'first_name' :'bbb',
	'last_name' :'bbb',
	'age' : 1,
	'city' : 'bbb'
}
brothers={
	'first_name' :'ccc',
	'last_name' :'ccc',
	'age' : 1,
	'city' : 'ccc',
}
peoples = [friends,teachers,brothers]
for people in peoples:
	print(people)

##嵌套：字典中存储列表
favorite_place = {
	'a':['aa','aaa','aaaa'],
	'b':['bb','bbb','bbbb'],
	'c':['cc','ccc','cccc']
}
for name,places in favorite_place.items():
	print(name.title()+' favorite places are ')
	for place in places:
		print(place)
