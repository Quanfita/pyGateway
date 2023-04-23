from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/test1', methods=['POST'])
def test():
    print(request.url)
    return jsonify({'code': 200, 'msg': 'ok'})

if __name__ == '__main__':
    app.run(port=8001,debug=True)