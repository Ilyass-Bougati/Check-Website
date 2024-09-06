import requests
from time import sleep
from notifypy import Notify
from bs4 import BeautifulSoup
from sys import argv

WAIT_TIME = 60


# Checking if the url exists
if len(argv) != 3:
    print("USAGE: python check.py [url] [tag]")
    exit(1)

ELEMENT   = argv[2]

# Create a notification object
notification = Notify()
# getting the initial page
url = argv[1]
print(f"Getting the provided url : ")
initial_request = requests.get(url)
# checking if the url is reachable
if initial_request.status_code != 200:
    print("Error getting the url")
    print(f"http status code = {initial_request.status_code}")

print("Website reached successfully")
print("page saved to memory, you'll be notified for any change")
init_list = BeautifulSoup(initial_request.text, features="html.parser").find_all(ELEMENT)

# checking if the page changed
i = 1
while True:
    # waiting 
    sleep(WAIT_TIME)

    # getting the page
    req = requests.get(url)
    if req.status_code != 200:
        print("Error getting the url")
        print(f"http status code = {req.status_code}")
    new_list = BeautifulSoup(initial_request.text, features="html.parser").find_all(ELEMENT)

    if init_list != new_list:
        # Set the title and message for the notification
        notification.title = "Spotted a change in the web page"
        notification.message = f"Something changed in\n{url}"
        notification.urgency = "critical"
        notification.icon = "icon/icon.png"
        # Display the notification
        notification.send()
        
        init_list = new_list
    else :
        print(f"Check {i}: Nothing changed", end="\r")

    i = i + 1

print(new_page)