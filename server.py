from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from apps.forms import ContactForm
from apps.mail import Mail
import sys
app = Flask(__name__)

app.secret_key = 'INSERT SECRET KEY HERE'
contact_receive_email = 'icepuente@gmail.com'

@app.route('/', methods=["GET"])
def home():
	return render_template('home.html', ip=str(request.remote_addr))

@app.route('/about', methods=["GET"])
def about():
	return render_template('about.html', ip=str(request.remote_addr))

@app.route('/resume', methods=["GET"])
def resume():
	return render_template('resume.html', ip=str(request.remote_addr))

@app.route('/projects', methods=["GET"])
def projects():
	return render_template('projects.html', ip=str(request.remote_addr))

@app.route('/contact', methods=["GET", "POST"])
def contact():
	form = ContactForm()

	if request.method == 'POST':
		if form.validate():
			mail = Mail(form.name.data, form.email.data, contact_receive_email,
			 form.subject.data, form.message.data)
			mail.send()
			flash('Successfully submitted message', 'success')
			return redirect(url_for('contact'))
		else:
			flash('All fields are required', 'error')
	return render_template('contact.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)


