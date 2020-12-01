from aiohttp import ClientSession
import urllib.request
import socket
import urllib.error
import lxml.html
import asyncio

def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({'https': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('https://www.google.com/')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False

def write_file(list):
    with open("good_proxy", "w") as outfile:
        outfile.write("\n".join(str(item) for item in list))
def open_file():
    with open('proxies.txt',"r") as f:
        lines = f.read().splitlines()
        return lines


async def main():
    socket.setdefaulttimeout(120)

    proxyList = open_file()
    goodproxy = []
    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
            print("Bad Proxy %s" % (currentProxy))
        else:
            print("%s is working" % (currentProxy))
            goodproxy.append(currentProxy)
    write_file(goodproxy)

asyncio.run(main())