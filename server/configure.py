from flask import Flask, send_from_directory
import os

app = Flask(__name__)

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), "static", "views")
)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_logon():
    print("Hit")
    root_dir = os.path.dirname((os.path.realpath(__file__)))
    return send_from_directory(os.path.join(root_dir, 'static', 'views'), "logon.html")

if __name__ == '__main__':
    app.run(host='::', port=80)
