
class find:
	def enter_list(self):
		input_element=raw_input('Enter comma seperated elements -')
		mylist=[ x for x in input_element.split(',')]
		return mylist

	def find_reverse(self,x):
		prev=""
		sorted_list=[]
		for i in x:
			if i!=prev:
				sorted_list.append(i)
			prev=i 
		return sorted_list
a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
print a.find_reverse(create_list)