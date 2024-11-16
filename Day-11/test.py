# use case fetch the user details who raised pull requests
# api url  https://api.github.com/repos/OWNER/REPO/pulls
# talk to github api with module 
# convert json format to Dictionary
# fetch users from pool of data
import requests
import json
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
details = response.json() # json module automatically convert json to dictonary 
for i in range(len(details)):
    print(details[i]["user"]["login"])
