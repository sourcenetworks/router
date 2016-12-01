from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

EXAMPLE_SERVER = "http://[::1]:5000"
PROXY = "http://[::1]:9000"

proxies = {"http": PROXY}

wallet = Wallet()
requests = BitTransferRequests(wallet)


def main():
    print("Call the example server directly")
    print("The goal here is to confirm that the example server is \
    reachable and can distinguish between a proxied and non-proxied \
    connection.")
    r = requests.get(url=EXAMPLE_SERVER + "/proxied")
    print(r.text)

    print("Call the example debug server through the proxy, paying 3000 satoshis per request")
    print("The goal here is to confirm that the example server was hit through a proxy.")
    r = requests.get(url=EXAMPLE_SERVER + "/proxied", proxies=proxies)
    print(r.text)

    print("Now call a real server at stanford.edu by paying the proxy some bitcoin")
    r = requests.get(url="http://httpbin.org/get", proxies=proxies)
    print(r.text)

if __name__ == '__main__':
    main()
