# Python Flask App
# Helper to POST data into Database
# Default MySQL Database connection 
# HTTP POST


# (c)2023 GESANG TECHNOLOGY
from flask import Flask, request
import datetime  # Import the datetime module
import mysql.connector

app = Flask(__name__)

@app.route('/arduino_post', methods=['POST'])
def arduino_post():
    if request.method == 'POST':
        suhu = request.form.get('suhu')
        kelembaban = request.form.get('kelembaban')
        pH = request.form.get('pH')

        # Get the current date and time from the PC
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # MySQL konektor
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='kopi'
        )
        cursor = conn.cursor()
        sql = "INSERT INTO sensor_data (tanggaljam, suhu, kelembaban, pH) VALUES (%s, %s, %d, %d)"
        values = (current_time, suhu, kelembaban, pH)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        return "OK"

if __name__ == '__main__':
    app.run(host='localhost', port=8080)  # Run Flask app on a specified host and port
