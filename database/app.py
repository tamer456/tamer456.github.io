from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Database connection settings
DB_HOST = 'your_host'
DB_NAME = 'your_database'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'

@app.route('/')
def index():
    # Connect to PostgreSQL
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()

    # Query credit card data
    cur.execute("SELECT * FROM credit_cards ORDER BY cashback_percentage DESC LIMIT 5")
    featured_cards = cur.fetchall()

    # Close database connection
    cur.close()
    conn.close()

    return render_template('index.html', featured_cards=featured_cards)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
