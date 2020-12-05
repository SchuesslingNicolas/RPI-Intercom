from flask import Flask, request
from flask_restful import Api, Resource

import playsound
import threading

app = Flask(__name__)
api = Api(app)

class Play(Resource):
    def post(self):
        data = request.get_json()
        if data is None:
            return {"error": "No URL sent"},400
        if "URL" not in data:
            return {"error": "Need to provide URL"},400
        x = threading.Thread(target=playAudio, args=(data["URL"],))
        x.start()
        return

def playAudio(path):
    playsound.playsound(path, True)


api.add_resource(Play,"/api/v1/play")

if __name__ == '__main__':
    app.run(debug=True, port=5100)
