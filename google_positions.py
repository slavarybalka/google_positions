import urllib
import http.client
from urllib.parse import urlparse
import urllib.request
from urllib.error import URLError, HTTPError
import socket
from socket import timeout

import re
import time

clients_domain = "www.alawpro.com"
keyword = "jeff rudman"
simple_query = "https://www.google.com/search?num=100&ion=1&espv=&ie=UTF-8&q="
opener = urllib.request.FancyURLopener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
socket.setdefaulttimeout(10)


try:
    se_req = opener.open(simple_query + keyword.replace(' ','%20'))
    results = se_req.read()
    links = re.findall(b'<cite>([^"]+)</cite>', results)

except HTTPError as e:
    print('HTTP error:', e.code)
    pass
except URLError as e:
    print('We failed to reach a server:', e.reason)
    pass
except socket.timeout:
    print('socket timeout')
    pass
except http.client.BadStatusLine as e:
    print('HTTP error not recognized, error code not given')
    pass
except ValueError as e:
    print('Error:', e)
    pass


for i in links:
    print(i)
    if clients_domain in str(i):
        print("Website " + str(i) + " found at position " + str(int(links.index(i))+1) + " for keyword " + str(keyword))
        break
    else:
        pass
