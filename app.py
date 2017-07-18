from flask import Flask, render_template
import random
app = Flask(__name__)

fortunes = ["You will marry a wealthy person from a foreign land", 
"You will have 10 children",
"Your greatest desire shall come true on June 1, 2022",
"You will travel to many countries",
"You will win a prestigious award",
"You will be famous for inventing something",
"You will have many friends"];


conditions = ["if you work hard.",
"if you are kind.",
"if you smile a lot.",
"if you have an open mind."]


names=["hala","roaa","arwa","khaled","bakiza","odai","hadi","mo7ammed","ishan","seirra","noura","rori"]

@app.route("/")
def homepage ():
	return render_template("homepage.html")

@app.route("/howlucky")
def randomly ():
	return render_template("theluckypage.html" ,
	 luckk= (random.choice(fortunes)  +" " + random.choice(conditions)+ ", your babys name is " + random.choice(names)))
	

	

@app.route("/contactme")
def contact ():
	return render_template("contectme.html",
		num =str(random.randint(0000000,9999999)))

	


	

if __name__ == "__main__":
	app.run()