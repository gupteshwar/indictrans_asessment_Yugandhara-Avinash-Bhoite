

class find:
	def enter_list(self):
		input_length = input("Enter length of list you want to enter : ")
		mylist=list()
		for i in range(input_length):
			input_element=input('Enter element for list :')
			mylist.append(input_element)
		return mylist

	def my_last(self,x):
		return x[-1]

a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
print "Last element of list :",a.my_last(create_list)