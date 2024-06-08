from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Вставьте ваш API ключ от ipgeolocation.io
API_KEY = 'cab89dcff56241afb57fe55421355ebf'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_ip_info():
    ip = request.remote_addr
    
    response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip=185.24.76.184')
    data = response.json()
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
