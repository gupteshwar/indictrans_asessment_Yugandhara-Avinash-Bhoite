
class find:
	def enter_list(self):
		input_length = input("Enter length of list you want to enter : ")
		mylist=list()
		for i in range(input_length):
			input_element=input('Enter element for list :')
			mylist.append(input_element)
		return mylist

	def my_element(self,x,pos):
			return x[pos-1]


a=find()
create_list=a.enter_list()
enter_position=int(input('Enter the index to get assigned element :')) 
print "Entered list : ",create_list
print format("Element at index %d is %s"%(enter_position,a.my_element(create_list,enter_position)))