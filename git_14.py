#question : 1.14 (*) Duplicate the elements of a list.

class find:
	def enter_list(self):
		input_element=raw_input('Enter comma seperated elements -')
		mylist=[ x for x in input_element.split(',')]
		return mylist

	def get_duplicate(self,x):
		x=x*2
		return x
a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
print "Reverse of entered list : ",a.get_duplicate(create_list)