import os
import fnmatch
import threading

print("Loading modules...")
from two1router.apps.bitcoin import bitcoin
from two1router.proxy import server

# Execute configuration
print("Configuring network...")
os.system("./two1router/network/config.sh")

pid = os.fork()
if pid == 0:  # child
    print("Starting bitcoin app...")
    bitcoin.run()
else:  # parent
    print("Starting server...")
    server.serve_forever()
