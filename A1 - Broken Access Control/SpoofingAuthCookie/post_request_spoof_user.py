import requests
import sys

try:
   #Assign script parameters to variables
   sessionID = sys.argv[1]
   username = sys.argv[2]
   password = sys.argv[3]
   #Define request body
   body='username='+str(username)+'&password='+str(password)
   #Define request headers
   headers = {
		 'Accept': '*/*',
		 'Accept-Encoding':'gzip, deflate, br',
		 'Accept-Language':'en-US,en;q=0.5',
		 'Connection':'keep-alive',
		 'Content-Type':'application/x-www-form-urlencoded',
		 'Cookie':'JSESSIONID='+str(sessionID),
		 'Origin':'http://localhost:8080',
		 'Referer':'http://localhost:8080/WebGoat/start.mvc',
		 'Sec-Fetch-Dest':'empty',
		 'Sec-Fetch-Mode':'cors',
		 'Sec-Fetch-Site':'same-origin',
		 'User-Agent':'any',
		 'X-Requested-With':'XMLHttpRequest',
      }
   #Send post request to retrieve user cookie 
   response = requests.post('http://localhost:8080/WebGoat/SpoofCookie/login',body,timeout=5, headers=headers)
   data = response.json()
   print(data)

except Exception as error:
  print("An exception occured:", error)
