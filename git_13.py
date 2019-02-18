#question - 1.13 (**) Run-length encoding of a list (direct solution).
# Implement the so-called run-length encoding data compression method directly. I.e. don't explicitly create the sublists containing the duplicates, as in problem 1.09, but only count them. As in problem 1.11, simplify the result list by replacing the singleton terms [1,X] by X.

class find:
	def enter_list(self):
		input_element=raw_input('Enter comma seperated repeated elements -')
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
	def subcount(self,nested):
		new_list=[]
		for i in nested:
			if len(i)>1:
				sub_list=[]
				sub_list.append(len(i))
				sub_list.append(i[0])
				new_list.append(sub_list)
			else:
				new_list.append(i[0])
		return new_list

a=find()
create_list=a.enter_list()
print "Entered list : ",create_list
slist= a.get_sublist(create_list)
print a.subcount(slist)