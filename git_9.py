#question : 1.09 (**) Pack consecutive duplicates of list elements into sublists.
#If a list contains repeated elements they should be placed in separate sublists.

class find:
	def enter_list(self):
		input_element=raw_input('Enter comma seperated elements -')
		mylist=[ x for x in input_element.split(',')]
		return mylist

	def get_sublist(self,x):
		prev=""
		return_list=[]
		flag=0
		for i in range(len(x)):
			if x[i]!=prev:
				if flag==0:
		 			sorted_list=[]
					sorted_list.append(x[i])
					prev=x[i]
				else:
					return_list.append(sorted_list)
					sorted_list=[]
					sorted_list.append(x[i])
					prev=x[i]
			elif x[i]==prev:
				sorted_list.append(x[i])
				prev=x[i]
				flag=1
			if i==len(x)-1:
				return_list.append(sorted_list)
		return return_list
a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
print a.get_sublist(create_list)