from flask import Flask, render_template
app = Flask(__name__)

registered = False

@app.route("/")
def serve_logon():
    return render_template("logon.html")

def check_payment(request):
    if registered == False:
        app.run(host='::', port=8081)
        serve_logon()

    return
