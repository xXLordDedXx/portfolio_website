from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
Bootstrap5(app)

mail = Mail(app)
app.config['MAIL_SERVER'] = os.environ.get('server_')
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('username_')
app.config['MAIL_PASSWORD'] = os.environ.get('password_')
mail.init_app(app)

@app.route('/')
def main_site():
	return render_template("index.html")

@app.route('/portfolio')
def portfolio_site():
	return render_template("portfolio.html")

@app.route('/contact', methods=["GET", "POST"])
def contact_site():
	if request.method == "POST":
		name = request.form.get('name')
		email = request.form.get('email')
		message = request.form.get('message')

		my_address = ['wiktor.gronostaj03@gmail.com']
		subject = f"New contact form from portfolio website"

		msg = Message("dupa", sender=os.environ.get('username_'), recipients=['wiktor.gronostaj03@gmail.com'])
		msg.body = """ 
		From: %s <%s> 
		%s 
		""" % (name, email, message)
		mail.send(msg)
		return redirect(url_for('contact_site'))
	return render_template("contact.html")

if __name__ == "__main__":
	app.run(debug=False)  
	