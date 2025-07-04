from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL remote DB config
DB_CONFIG = {
    'host': 'your-remote-host.com',
    'user': 'your_username',
    'password': 'your_password',
    'port': 3306
}

@app.route('/show-databases')
def show_databases():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES")
        db_list = [row[0] for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        return render_template("databases.html", databases=db_list)
    except Exception as e:
        return f"<h3>Error connecting to database: {str(e)}</h3>", 500

if __name__ == '__main__':
    app.run()
