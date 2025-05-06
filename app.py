from flask import Flask, render_template, request, redirect, url_for
import os
from parser import parse_legacy_data

print("Flask app file is executing...")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    records = parse_legacy_data(filepath)
    return render_template('result.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
