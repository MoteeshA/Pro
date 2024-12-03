from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # From environment variable
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")  # From environment variable
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")  # From environment variable

app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = MAIL_DEFAULT_SENDER
mail = Mail(app)

@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/MiniProject/templates/buy.html')
def buy():
    if request.method == 'POST':
        return redirect(url_for('send_email'))
    return render_template('buy.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    # Get customer details from the form
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')

    # Create an email message
    msg = Message("Customer Order Details", recipients=[os.getenv("YOUR_EMAIL")])
    msg.body = f"""
    Customer Details:
    Name: {name}
    Email: {email}
    Phone: {phone}
    Address: {address}
    """
    
    try:
        # Send the email
        mail.send(msg)
        # After sending the email, redirect to a confirmation page
        return render_template('confirmation.html', name=name)
    except Exception as e:
        # If there's an error, render an error page
        return render_template('error.html', error_message=str(e))

@app.route('/send_contect', methods=['POST'])
def send_contact():
    # Get customer details from the form
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    message = request.form.get('message')

    # Create an email message
    msg = Message("Customer Order Details", recipients=[os.getenv("YOUR_EMAIL")])
    msg.body = f"""
    Customer Details:
    Name: {name}
    Email: {email}
    Address: {address}
    Message: {message}
    reaching out to inquire about the Service.

    Next Steps:
------------
1. One of our customer service representatives will contact you shortly to discuss the details of your inquiry.
2. If you need immediate assistance, please feel free to contact our support team at srisaigeneshente@gmail.com.
3. We recommend checking our website for more information on the services we offer and to track your inquiry status.


    """
    
    try:
        # Send the email
        mail.send(msg)
        # After sending the email, redirect to a confirmation page
        return render_template('contact.html', name=name)
    except Exception as e:
        # If there's an error, render an error page
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True,port=5001)
