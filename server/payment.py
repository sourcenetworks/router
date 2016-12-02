from flask import Flask
app = Flask(__name__, static_url_path='templates/views')

registered = False

def check_payment(request):
    if register == False:
        return app.send_static_file("logon.html")

    return
