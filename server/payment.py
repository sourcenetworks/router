from flask import Flask

app = Flask(__name__, static_url_path="/templates/views/")

registered = False

@app.route('/')
def serve_logon():
    return send_static_file("logon.html")

def check_payment(request):
    if registered == False:
        serve_logon()

    return
