from flask_restful import Resource


class MainAPI(Resource):

    def post(self):
        return {}, 200
    
    def get(self):
        return {}, 200
