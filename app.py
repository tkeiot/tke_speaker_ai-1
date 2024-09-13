from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Giá trị mặc định cho các thông số
parameters = {
    'param1': 'Giá trị 1',
    'param2': 'Giá trị 2',
    'param3': 'Giá trị 3'
}

@app.route('/')
def index():
    return render_template('index.html', parameters=parameters)

@app.route('/update', methods=['POST'])
def update_parameters():
    # Lấy các giá trị từ form và cập nhật các thông số
    parameters['param1'] = request.form['param1']
    parameters['param2'] = request.form['param2']
    parameters['param3'] = request.form['param3']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='192.168.0.32', port=5000, debug=True)




