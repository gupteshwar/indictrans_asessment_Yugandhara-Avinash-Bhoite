
import random
class find:
	def enter_list(self):
		input_length = input("Enter length of list you want to enter : ")
		assert input_length>2, "List length should be more than 2"
		mylist=list()
		for i in range(input_length):
			input_element=input('Enter element for list :')
			mylist.append(input_element)
		return mylist

	def my_last_but_1(self,x):
		random_list=x[0:len(x)-1]
		return random.choice(random_list)

a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
print "Last but one element of list :", a.my_last_but_1(create_list)