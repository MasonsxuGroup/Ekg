from flask import Flask, render_template, request, jsonify
from gevent.pywsgi import WSGIServer
from Back_End.goods import extraction

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


@app.route('/api/figure', methods=['GET', 'POST'])
def figure():
    if request.method == 'GET':
        figure_data_dict = extraction.ExtractData.load_figure_data()
        return jsonify(figure_data_dict)


@app.errorhandler(Exception)
def handle_exception_error(e):
    return render_template('index.html')


if __name__ == "__main__":
    http_server = WSGIServer(('0.0.0.0', 5500), app)
    http_server.serve_forever()
    print('======>>>EkgServer is listening<<<======')
