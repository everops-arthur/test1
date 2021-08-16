"""Sample Flask helloworld application."""
from flask import request
from flask_api import FlaskAPI


app = FlaskAPI(__name__)


@app.route("/helloworld", methods=['GET'])
def hello():
    """Return HTML hello message."""
    message = """
        <h3>Welcome to a simple flask application.</h3>  
        <p>Please add your name to the end of the url to get full message (e.g. helloworld/Goku).</p>
        """
    return message


@app.route("/helloworld/<string:name>/", methods=['GET'])
def hello_user(name):
    """Return JSON response object with user's name."""
    if request.method == 'GET':
        formatted_name = name.capitalize()
        return {"response": f"Hello {formatted_name}"}

        
@app.route('/<path:path>')
def catch_all(path):
    """Returns message to redirect user to valid endpoint."""
    return '<h1>Bad Request</h1>  <p>Only valid url is "/helloworld"<p>.'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)