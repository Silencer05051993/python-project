from flask import Flask
from flask import make_response, request

from com.dimageshare.service.text_classify_service import TextClassificationService

app = Flask(__name__)


@app.route('/api/classification', methods=['GET'])
def classification_text():
    str = request.args.get('str')
    service = TextClassificationService()
    result = service.make_result(str)

    response = make_response(result.encode("utf-8"))
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Token'
    return response

if __name__ == '__main__':
    app.run()
