from flask import Flask, render_template
from blog import article

app = Flask(__name__)

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse aliquet, nibh vitae consequat iaculis, libero eros lobortis nisi, quis elementum odio nunc efficitur mi. Nulla volutpat ante est, in lobortis tortor tincidunt id. Duis at neque lorem. Donec aliquet mi id sem commodo porttitor."""
first = article( "gamedev", text, "Maxim Poliak" )
second = article( "truest", text, "Romchek 228" )
third = article( "superArticle", text, "kakoyto lox" )


@app.route("/")
def hello_world():
	return render_template( "index.html", posts = [
		first.getPost(), 
		second.getPost(), 
		third.getPost() ] )

if __name__ == '__main__':
	app.run(debug=True)