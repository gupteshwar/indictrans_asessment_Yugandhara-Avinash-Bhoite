
class find:
	def enter_list(self):
		input_element=raw_input('Enter comma seperated elements -')
		mylist=[ x for x in input_element.split(',')]
		return mylist

	def find_reverse(self,x):
		x.reverse()
		return x
a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
print "Reverse of entered list : ",a.find_reverse(create_list)