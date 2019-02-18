#question : 1.04 (*) Find the number of elements of a list.

class find:
	def enter_list(self):
		input_element=raw_input('Enter comma seperated elements -')
		mylist=[ x for x in input_element.split(',')]
		return mylist

	def find_lenth(self,x):
		return len(x)

a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
print "Length of entered list :",a.find_lenth(create_list)