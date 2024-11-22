from flask import Flask, render_template, redirect, request
import pymysql
from datetime import datetime

app = Flask(__name__)

# Configure MySQL settings individually (not recommended for Flask apps)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MySql46.@'
app.config['MYSQL_DB'] = 'attendance_app'

# Connect to MySQL directly using pymysql
mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

@app.route('/')
def index():
    # Connect to the MySQL database using pymysql to fetch attendance data
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM attendance")
    all_attendance = cursor.fetchall()  # Fetch all records
    cursor.close()
    
    return render_template('index.html', attendance=all_attendance)

@app.route('/add', methods=['POST'])
def add_attendance():
    if request.method == 'POST':
        name = request.form['name']
        timestamp = datetime.now()
        
        # Insert the new attendance record into the database
        cursor = mysql.cursor()
        cursor.execute("INSERT INTO attendance (name, timestamp) VALUES (%s, %s)", (name, timestamp))
        mysql.commit()  # Commit the transaction
        cursor.close()
        
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
