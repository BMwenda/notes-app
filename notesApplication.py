'''
Programming logic assignment: notes taking app
'''

class NotesApplication(object):
	def __init__(self,author):
		self.author=author
		self.notes=[]

	def getAuthor(self):
		return self.author

	def create(self,note_content):
		self.notes.append(note_content)

	def list(self):
		for i in self.notes:
			print ("Note ID: {0}\n{1}\n\nBy Author {2}".format(self.notes.index(i),i,self.author))
			

	def get(self,note_id):
		return self.notes[note_id]

	def search(self,search_text):
		for x in self.notes:
			if search_text in x:
				print ("Showing results for search '{0}'\n\nNote ID: {1}\n{2}\n\nBy Author {3}".format(search_text,self.notes.index(x),x,self.author))

	def edit(self,note_id,new_content):
		self.notes[note_id]=new_content

note1=NotesApplication("Banks")
note2=NotesApplication("Bonny")
for i in range(4):
	note1.create("Note {0}".format(i))

note1.edit(0,"First message")
#print(note2.search('ot'))
print(note1.list())
#print(note1.get(0))
