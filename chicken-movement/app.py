from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# configure email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'phonexaung@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')

# create a mail instance
mail = Mail(app)


# define a route for form submission
@app.route('/submit-form', methods=['POST'])
def submit_form():
    # get form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # send email
    msg = Message('New form submission', sender=email, recipients=['phonexaung@gmail.com'])
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    mail.send(msg)

    return 'Form submitted successfully'


if __name__ == '__main__':
    app.run(debug=True)