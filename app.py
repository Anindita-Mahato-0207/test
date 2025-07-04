from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Welcome! Visit <a href="/get-data">/get-data</a> to fetch and display data.</h2>'

@app.route('/get-data')
def get_data():
    try:
        response = requests.get('https://interview.travarsa.net/test.php')
        
        if response.status_code == 200:
            data = response.json()
            return render_template('databases.html', data=data)
        else:
            return f"<h3>Failed to fetch data. Status code: {response.status_code}</h3>", 500
    except Exception as e:
        return f"<h3>Error occurred: {str(e)}</h3>", 500

if __name__ == '__main__':
    app.run()
