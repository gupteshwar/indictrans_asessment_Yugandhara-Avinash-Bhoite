#question : 1.12 (**) Decode a run-length encoded list.
# Given a run-length code list generated as specified in problem 1.11. Construct its uncompressed version.

class find:
	def decompress(self,x):
		new_list=[]
		for i in x:
			l=i[0]
			if len(i)>1:
				while l>0:
					new_list.append(i[1])
					l=l-1
			else:
				new_list.append(i[0])
		return new_list
	

a=find()
create_list=[[4,'a'],'b',[2,'c'],[2,'a'],'d',[4,'e']]
print a.decompress(create_list)
