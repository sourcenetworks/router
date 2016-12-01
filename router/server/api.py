registered_functions = []

def register(func):
    """Register a function to called when a request is inbound"""
    try:
        registered_functions.append(func)
    except SyntaxError:
        print("No function registered")

def request_notify(req):
    """Process request data and notify registered functions"""
    print("Request received of size %d" % len(req))

    for f in registered_functions:
        f(req)
