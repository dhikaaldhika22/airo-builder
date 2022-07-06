from api import *
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def health_check():
    return "Morbin time"

@app.route("/personalize", methods = ["POST"])
def get_personalization():
    request_json = request.form.to_dict()
    argument_input = request_json.get('message')
    print("message: ", argument_input)
    result = kata_unused(argument_input)
    rmv_tandabaca = tanda_baca(result)
    response = predict(rmv_tandabaca)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)