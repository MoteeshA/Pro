from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Flask-Mail for email sending
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use your SMTP server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")  # Your email
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")  # Your email password or app-specific password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")

mail = Mail(app)

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/buy', methods=['GET'])
def buy_page():
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
        return "Your order has been submitted successfully."
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
