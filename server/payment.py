from flask import send_static_file

app = Flask(__name__, static_url_path="/templates/views/")

registered = False

def serve_logon():
    return send_static_file("logon.html")

def check_payment(request):
    if registered == False:
        serve_logon()

    return
