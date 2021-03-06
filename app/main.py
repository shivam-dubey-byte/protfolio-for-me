from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

#with open('config.json','r') as c:
#	params=json.load(c)['params']
#	data=json.load(c)['data']
date = datetime.now()
experience = date.year-2019
c={
	"params":
	{
		"local_uri":"mysql://root:@localhost/portfolio",
		"pro_uri":"mysql://upma5o7dhdq9pzi:shivamR@J-123@eu-az-sql-serv1.database.windows.net/ddwhvui12qtl0cl"
	},
	"data":{
		"name":"Shivam Raj Dubey",
		"header":"Web Developer - Freelancer - Full Stack Developer",
		"option1":"Portfolio",
		"option2":"About",
		"option3":"Contact",
		"t-loc":"Location",
		"loc":"India, Asia",
		"email":"admin@theshivam.tech",
		"about-me":"Web Developer, Freelancer, Full Stack Developer",
		"copyright":"Shivam Raj Dubey 2021",
		"about-p1-div1":"This is Shivam Raj Dubey. Freelancer, Web Developer, Full Stack Developer. I know the languages Python, C#, Core Java. I have worked with the python framework Flask.",
		"about-p2-div2":"If you wanna have your digital presence than you can contact me for any Web Development works.",
		"about-p3-div2":"Web Developer | New to AI | FullStack Developer | Python | Flask | C# | Java | JavaScript | Freelancer",
		"por-topic1":"I know many languages, 'Python' is one of them. Write now am working with this language. And I have a good hands on this. I'm the certified Developer in Python.",
		"por-topic2":"I'm a good WebDeveloper. I have a good practice on this. I have created some of the website in production.",
		"por-topic3":"I'm a good experienced in flask framework and I'm mainly work with this framework only.",
		"por-topic4":"I'm a good Programmer.",
		"por-topic5":"I have also good hands on Java-Core. So, I can also work with java frameworks.",
		"por-topic6":"I have a experience of '"+ str(experience) + " Years'.",
		"por-h1":"Python",
		"por-h2":"Full Stack Developer",
		"por-h3":"Flask",
		"por-h4":"Programming",
		"por-h5":"Java",
		"por-h6":"experience"




	},
	"links":{
		"facebook":"https://www.facebook.com/profile.php?id=100027876074853",
		"twitter":"https://twitter.com/ShivamRajDubey2",
		"linkedin":"https://www.linkedin.com/in/shivam-raj-dubey-5610361ba/",
		"img":{
		"por-img1":"",
		"por-img2":"",
		"por-img3":"",
		"por-img4":"",
		"por-img5":"",
		"por-img6":""
		}
	}
 }
params = c['params']
data = c['data']
links = c['links']

local_server= True

app = Flask(__name__)

db = SQLAlchemy(app)

if (local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['pro_uri']



class Message(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100),unique=False,nullable=False)
    message = db.Column(db.String(200),unique=False,nullable=False)
    phone_num = db.Column(db.VARCHAR(12),unique=True,nullable=False)
    date = db.Column(db.String(12),unique=False,nullable=False)

try:
	@app.route("/")
	def home():
		try:
			return render_template('index.html',data=data,links=links,submit='/sentMessage')
		except:
			return redirect('/error')
	@app.route('/sentMessage', methods=['POST'])
	def __message__():
		try:
			name=request.form.get('name')
			email=request.form.get('email')
			phone_num=request.form.get('phone')
			message=request.form.get('message')
			enter=Message(name=name,email=email,phone_num=phone_num,message=message,date=str(datetime.now()))
			print('1')
			db.session.add(enter)
			print('2')
			db.session.commit()
			return 'Working'
		except:
			return redirect('/error')
	@app.route('/error')
	def __error__():
		return render_template('error.html')
	@app.route("/<string>")
	def _redirect_(string):
		return redirect('/')
except:
	@app.route('/error')
	def __error__():
		return render_template('error.html')

if __name__=='__main__':
    app.run(debug=True)
'''
	name = request.form.get('name')
	email = request.form.get('email')
	phone = request.form.get('phone')
	message = request.form.get('message')
	print(name + email + phone + message)
    name = db.Column(db.String(100), unique=False,nullable=False)
    email = db.Column(db.String(100),unique=False,nullable=False)
    phone_num = db.Column(db.VARCHAR(12),unique=False,nullable=False)
    message = db.Column(db.String(200),unique=False,nullable=False)
    date = db.Column(db.String(12),unique=False,nullable=False) '''
