from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path="/templates/views/")

registered = False

@app.route('/')
def serve_logon():
    return app.send_static_file("logon.html")

def check_payment(request):
    if registered == False:
        app.run()
        serve_logon()

    return
