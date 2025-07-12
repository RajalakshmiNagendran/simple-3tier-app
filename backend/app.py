from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def home():
        return jsonify({'message': 'Hello from Backend with SQLite!'})

if __name__ == '__main__':
   app.run(host='0.0.0.0')

