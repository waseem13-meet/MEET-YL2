class Animal():
	 
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def sleep(self):
		print self.name +" of " + str(self.age) + " is sleeping "

	def eat(self,food):
		print self.name +" of " + str(self.age) + " is eating "+food
class bird(Animal):

	def __init__(self,name,age,wings):
		self.wings=wings
		Animal.__init__(self,name, age)
	def Fly(self):
		print  self.name +" of " + str(self.age) +" with " +self.wings+ " wings" +" is flying"	
class dog(Animal):
	def __init__(self,name,age):
		Animal.__init__(self,name, age)
		
#---------------------------------------------------------

p = Animal("Sub7i",17)
p.sleep()
p.eat("pizza")
x=Animal("ted", 2)
x.sleep()
x.eat("pizza")
z=bird("raven",11,"black")
z.Fly()
