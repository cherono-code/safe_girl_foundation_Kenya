from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')

mysql = MySQL(app)

@app.route('/safegirlfoundationke')
def safegirlfoundationke():
    return render_template('safegirlfoundationke.html')

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
         print(request.form)
        # Get form data
         first_name = request.form['firstName']
         last_name = request.form['lastName']
         email = request.form['email']
         phone_number = request.form['phoneNumber']
         donation_type = request.form['donationType']
         company_name = request.form['companyName']
         credit_card_number = request.form['creditCardNumber']
         cvv = request.form['cvv']
         expiration_date = request.form['expirationDate']
         billing_postal_code = request.form['billingPostalCode']
         donation_amount = request.form['donationAmount']
         custom_amount = request.form.get('customAmount')

        # Store data in the database
         cur = mysql.connection.cursor()
         cur.execute("""
            INSERT INTO donations (fullName, email, phoneNumber, donationType, companyName, creditCardNumber, cvv, expirationDate, billingPostalCode, donationAmount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (f"{first_name} {last_name}", email, phone_number, donation_type, company_name, credit_card_number, cvv, expiration_date, billing_postal_code, custom_amount if custom_amount else donation_amount))
         mysql.connection.commit()
         cur.close()

         return render_template('thank_you.html', full_name=f"{first_name} {last_name}")

    return render_template('donate.html')

@app.route('/saveDonor', methods=['POST'])
def save_donor():
    # Redirect POST requests to the /donate route
    return redirect(url_for('donate'), code=307)

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
