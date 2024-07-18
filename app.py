from flask import Flask, render_template, request

app = Flask(__name__)

def transpose_column_encrypt(message, key):
    message = message.replace(" ", "").upper()
    num_rows = len(message) // key + (len(message) % key != 0)
    matrix = [['' for _ in range(key)] for _ in range(num_rows)]
    index = 0
    for r in range(num_rows):
        for c in range(key):
            if index < len(message):
                matrix[r][c] = message[index]
                index += 1
    encrypted_message = ""
    for c in range(key):
        for r in range(num_rows):
            if matrix[r][c] != '':
                encrypted_message += matrix[r][c]
    return encrypted_message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    key = int(request.form['key'])
    encrypted_message = transpose_column_encrypt(message, key)
    return render_template('index.html', message=message, key=key, encrypted_message=encrypted_message)

if __name__ == '__main__':
    app.run(debug=True)