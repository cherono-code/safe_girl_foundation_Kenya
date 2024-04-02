from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField, DecimalField
from wtforms.validators import InputRequired, Email

app = Flask(__name__)
app.config.from_pyfile('config.py')

# MySQL configurations
app.config['MYSQL_USER'] = 'cherono@123'
app.config['MYSQL_PASSWORD'] = '888'
app.config['MYSQL_DB'] = 'donation_database'
app.config['MYSQL_HOST'] = 'localhost'

# Add Flask-WTF CSRF secret key
app.config['SECRET_KEY'] = '1111'

mysql = MySQL(app)

# Define a simple form using Flask-WTF for illustration
class DonationForm(FlaskForm):
    fullName = StringField('Full Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    phoneNumber = StringField('Phone Number')  # Adjust based on your requirements
    donationType = RadioField('Donation Type', choices=[('oneTime', 'One Time'), ('monthly', 'Monthly')], validators=[InputRequired()])
    companyName = StringField('Company Name')  # Adjust based on your requirements
    creditCardNumber = StringField('Credit Card Number', validators=[InputRequired()])
    cvv = StringField('CVV', validators=[InputRequired()])
    expirationDate = StringField('Credit Card Expiration Date', validators=[InputRequired()])
    billingPostalCode = StringField('Billing Postal Code', validators=[InputRequired()])

    # Add more fields as needed...

    donationAmount = SelectField('Donation Amount', choices=[
        ('55', 'USD$55'), ('25', 'USD$25'), ('45', 'USD$45'), ('200', 'USD$200')
    ], validators=[InputRequired()])
    
    customAmount = DecimalField('Custom Amount')  # Adjust based on your requirements

    donationFrequency = SelectField('Donation Frequency', choices=[
        ('oneTime', 'One Time'), ('monthly', 'Monthly')
    ], validators=[InputRequired()])

    submit = SubmitField('Donate')

# Define routes
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/about_us')
def about_us():
    return render_template('aboutus.html')

@app.route('/safe_girl_center')
def safe_girl_center():
    return render_template('safe_girl_center.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        # Get form data
        full_name = request.form['fullName']
        email = request.form['email']
        phone_number = request.form['phoneNumber']
        donation_type = request.form['donationType']
        company_name = request.form['companyName']
        credit_card_number = request.form['creditCardNumber']
        cvv = request.form['cvv']
        expiration_date = request.form['expirationDate']
        billing_postal_code = request.form['billingPostalCode']
        donation_amount = request.form['donationAmount']
        donation_frequency = request.form['donationFrequency']

        # Store data in the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO donations (fullName, email, phoneNumber, donationType, companyName, creditCardNumber, cvv, expirationDate, billingPostalCode, donationAmount, donationFrequency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (full_name, email, phone_number, donation_type, company_name, credit_card_number, cvv, expiration_date, billing_postal_code, donation_amount, donation_frequency))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('donate'))
    return render_template('donate.html')

@app.route('/saveDonor', methods=['POST'])
def save_donor():
    # Retrieve form data
    full_name = request.form.get('fullName')
    email = request.form.get('email')
    phone_number = request.form.get('phoneNumber')
    donation_type = request.form.get('donationType')
    company_name = request.form.get('companyName')
    credit_card_number = request.form.get('creditCardNumber')
    cvv = request.form.get('cvv')
    expiration_date = request.form.get('expirationDate')
    billing_postal_code = request.form.get('billingPostalCode')
    donation_amount = request.form.get('donationAmount')
    custom_amount = request.form.get('customAmount')

    # Do something with the form data (e.g., save to the database)

    return render_template('thank_you.html', full_name=full_name)

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/our_books')
def our_books():
    return render_template('our_books.html')

if __name__ == '__main__':
    app.run(debug=True)
