from flask import render_template


registered = False

def serve_logon():
    return render_template("logon.html")

def check_payment(request):
    if registered == False:
        serve_logon()

    return
