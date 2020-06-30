#第九章：类和实例
 #一、创建和使用
 #二、继承
 #三、导入类：类似导入函数


##创建和使用
class Car():
	
	#初始化函数：（--init--）设置类属性
	def __init__(self,make,model,year):
		'''初始化描述汽车的属性'''
		self.make = make
		self.model = model 
		self.year = year
		#给属性设置默认值
		self.odometer_reading = 0
		
	#类里面的方法
	def get_description_name(self):
		'''返回整洁的描述信息'''
		long_name = str(self.year)+' '+self.make+' '+self.model
		return long_name.title()
		
	#修改属性的值（两种方法：直接修改/通过方法修改）
		
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_description_name())


##继承
 #父类必须和子类在同一文件中，且位于子类前面{父类名作为参数}
 #子类的--init--方法{调用父类--init--，不用传递self参数}
 #子类定义属性和方法
 #重写父类方法
 #将实例用作属性

class ElectricCar(Car):
	def ___init__(self,make,model,year):
		super().__init__(make,model,year)
		#子类属性
		self.battery_size = 70

