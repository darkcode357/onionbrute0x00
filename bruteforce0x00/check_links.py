import socket
import urllib2

import socks  # SocksiPy module
import stem.process

SOCKS_PORT = 9050

# Set socks proxy and wrap the urllib module

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT)
try:
    socket.socket = socks.socksocket
except socket.error:
    print("erro")
# Perform DNS resolution through the socket

def getaddrinfo(*args):
  return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo

link = open("link1.txt", "r+")
dsa = link.readlines()
print("abrindo arquivos de urls....")
print("[+] listamos %i  url   [+]" % len(dsa))
print("[+] iniciando os tests [+]")
link.close()
link = open("link1.txt", "r+")

for url in link:
    print(url)
    try:
        dsa = urllib2.urlopen(url,timeout=10)
        print(dsa.getcode())
    except urllib2.URLError, e:
        print(e)
