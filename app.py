from flask import Flask, render_template  # Added render_template import
import requests

app = Flask(__name__)  # Initialize Flask app

@app.route('/get-data')
def get_data():
    response = requests.get('https://interview.travarsa.net/test.php')
    
    if response.status_code == 200:
        data = response.json()
        return render_template('databases.html', data=data)  # Pass data to template
    else:
        return "Failed to fetch data from cPanel API", 500