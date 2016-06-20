'''
Note taking app using Flask
'''

class NotesApplication(object):
	def __init__(self,author):
		self.author=author
		self.notes=[]

	def getAuthor(self):
		return self.author

	def create(self,note_content):
		self.notes.append(note_content)

	def alist(self):
		mystr=''
		for i in self.notes:
			mystr+= ("Note ID: {0}\n{1}\n\nBy Author {2}\n".format(self.notes.index(i),i,self.author))
		return mystr
			
	def get(self,note_id):
		return self.notes[note_id]

	def search(self,search_text):
		for x in self.notes:
			if search_text in x:
				print ("Showing results for search '{0}'\n\nNote ID: {1}\n{2}\n\nBy Author {3}".format(search_text,self.notes.index(x),x,self.author))

	def edit(self,note_id,new_content):
		self.notes[note_id]=new_content