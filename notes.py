from flask import Flask
from notesApplication import NotesApplication

app = Flask(__name__)

@app.route('/')
def getList():
	obj = NotesApplication("Mark Twain")
	for i in range(1,5):
		obj.create("Content {0}".format(i))
	return obj.alist()

if __name__=='__main__':
	app.run(debug=True)