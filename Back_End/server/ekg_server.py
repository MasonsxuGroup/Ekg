from flask import Flask, render_template, request
import extraction as extract
app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/extract', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.get_json()
        result_dict = extract.load_customization(result['content'])
        return result_dict


if __name__ == '__main__':
    app.run(port=8080)
