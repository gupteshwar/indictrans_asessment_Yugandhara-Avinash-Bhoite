#question : 1.15 (**) Duplicate the elements of a list a given number of times.

class find:
	def enter_list(self):
		input_element=raw_input('Enter comma seperated elements -')
		mylist=[ x for x in input_element.split(',')]
		return mylist

	def get_duplicate(self,x,repeat):
		x=x*repeat
		return x
a=find()
create_list=a.enter_list()
i=int(input("How many times you want to duplicate the elements? : "))
print "Entered list : ",create_list
print "Reverse of entered list : ",a.get_duplicate(create_list,i)