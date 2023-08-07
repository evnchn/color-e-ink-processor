from flask import Flask, request
from display import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(filename)
            decimal_number = request.form.get('decimal_number')
            if decimal_number:
                update_image(filename, float(decimal_number))
            return 'File uploaded successfully.'

    return '''
    <!doctype html>
    <html>
    <body>
        <h1>Upload a file</h1>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file"><br><br>
            <label for="decimal_number">Decimal Number:</label>
            <input type="number" name="decimal_number" step="0.01" min="-999.99" max="0" required><br><br>
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0')