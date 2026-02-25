from flask import Flask, render_template, jsonify
from flask_cors import CORS  # Install via: pip install flask-cors

app = Flask(__name__)
CORS(app) # Allow test.html to communicate with the API

# Initialize data for all 12 boxes
# Default value is "0"
data_store = {f"box{i}": "0" for i in range(1, 13)}

@app.route('/')
def index():
    # Render the main dashboard
    return render_template('index.html')

@app.route('/test')
def test_page():
    # Render the testing tool page
    return render_template('test.html')

# API for Reading data
@app.route('/<box_id>/read', methods=['GET'])
def read_api(box_id):
    content = data_store.get(box_id, "N/A")
    return jsonify({box_id: content})

# API for Writing data
@app.route('/<box_id>/write/<content>', methods=['GET', 'POST'])
def write_api(box_id, content):
    if box_id in data_store:
        data_store[box_id] = content
        return jsonify({"status": "success", "box": box_id, "new_content": content})
    return jsonify({"status": "error", "message": "Box not found"}), 404

if __name__ == '__main__':
    # Run server on port 5050
    app.run(port=5050, debug=True)