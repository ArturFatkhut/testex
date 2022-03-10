from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])

def takeJson():
    name = request.args['name']
    message = request.args['message']
    return "Hello {}! {}!".format(name, message)

if __name__ == "__main__":
    app.run()

