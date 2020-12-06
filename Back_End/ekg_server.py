from flask import Flask, render_template, request, jsonify
from goods import extraction

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/extract', methods=['POST', 'GET'])
def extract():
    if request.method == 'POST':
        result = request.get_json()
        result_dict = extraction.ExtractData.load_customization(
            result['content'])
        return jsonify(result_dict)


@app.errorhandler(Exception)
def handle_exception_error(e):
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8080)
