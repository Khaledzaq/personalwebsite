from flask import Flask, render_template , request
import random 
import dataset
# db = dataset.connect('postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4')
# info_table = db["userinfo_user"]

# user_table = db["khaledzaq_user"]
# user_table.insert(dict(name='khaled zaqout' , age= 14 , country= 'palestine'))
# user_table.insert(dict(name="khaled alhendawi" , age=16 , country='palestine'))
# user_table.insert(dict(name='hala barka' , age= 35, country='UK'))
# user_table.insert(dict(name='reana saed' , age= 25, country='USA'))
# for user in user_table:
# 	print ("id : " + str(user['id']) + " the name is " + str(user['name']) + " the age is " + str(user['age']) + " the country is " + str(user['country']))
# 	print (user_table.find_one(name = "khaled zaqout"))


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

@app.route("/wecode")
def wecode ():
	return render_template("wecode.html")

@app.route("/access")
def access():
	return render_template("access.html")

@app.route("/yes")
def yes():
	return render_template("yes.html")

@app.route("/viewthedata", methods= ["POST"])
def hello ():
	user_name = request.form["firstname"]
	user_lastname = request.form["lastname"]
	user_message = request.form["message"]
	user_gender = request.form["gender"]
	# info_table.insert(dict(firname="user_name" , lasname="user_lastname", message="user_message" , gender= "user_info"))
	# return info_table.find_one(firname="khaled")
	
	return render_template("veiwtheuser.html" ,
		username= user_name,
		userlastname=user_lastname,
		usermessage=user_message,
		usergender=user_gender
		) 
	#+ (user_name + " " + user_lastname + " "+ user_message + " " + user_gender)
	

	

if __name__ == "__main__" :
	app.run()
	
	# for user in info_table :
	# 	print ("the name is " + str(info_table['firname']) + " "+ str(info_table['lasname']) + "the message is " + str(info_table['message']) + " " + "the gender is " + str(info_table['gender'] )
	# 	#print (user_table.columns)
	# 	#print (db.tables) 
	# 	app.run()
	# 