from flask import Flask
from flask import make_response

from com.dimageshare.service.user_service import UserService

app = Flask(__name__)


@app.route('/api/kmeans-clustering', methods=['GET'])
def clustering():
    service = UserService()
    result = service.make_result()

    response = make_response(result.encode("utf-8"))
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Token'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5593)
