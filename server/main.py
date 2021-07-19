import flask
from service.country_service import getDetermineIntention
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app)

# app config

app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/api/get_information", methods=["GET"])
@cross_origin()
def sayHi():
    text = flask.request.args.get("text")
    data = getDetermineIntention(text)
    return flask.jsonify(data)


app.run()
