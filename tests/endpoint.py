from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

@app.route("/proxied")
def proxy():
    if "X-Forwarded-For" in request.headers:
        return "Proxied"
    else:
        return "Not proxied"

if __name__ == "__main__":
    app.run(host="::", port=5000)
