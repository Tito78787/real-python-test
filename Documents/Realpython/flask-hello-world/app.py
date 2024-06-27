from flask import Flask
app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

def hello_world():
    return "Hello world!?!?!?!?!"

@app.route
def search():
	return("Hello")

@app.route("/test/<search_query>")
def	search(search_query):
	return search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"
# #Running on http://localhost:5000/integer/1.		

@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "correct"
# ##http://localhost:5000/float/1.1.
@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"
##http://localhost:5000/path/just/a/random/path  

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name)
	else :
		return "Not found", 404
if __name__ == "__main__":
	app.run()
		# http://localhost:5000/name/michael.
		
