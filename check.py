import requests
from time import sleep
from notifypy import Notify
from bs4 import BeautifulSoup

WAIT_TIME = 60

class Checker:
    def ___init__(self):
        self.RUNNING = True

    def Check(self, url: str, tag: str, frame):
        url = url
        tag = tag

        # Create a notification object
        notification = Notify()
        notification.urgency = "critical"
        notification.icon = "icon/icon.png"
        notification.title = "Listening..."
        
        # getting the initial page

        try:
            initial_request = requests.get(url)
        except:
            frame.Error("Url is unreachable. You may be blocked, the url isn't correct, the website is down or my code is shit ;)", "Network error")
            return

        # sending a notification
        notification.application_name = "Checker"
        notification.message = f"Checker is listening to changes in in {url}..."
        notification.send()
            
        # checking if the url is reachable
        if initial_request.status_code != 200:
            frame.Error(f"http status code = {initial_request.status_code}", "Error getting the url")
            return

        frame.Print("Website reached successfully")
        frame.Print("page saved to memory, you'll be notified for any change")
        init_list = BeautifulSoup(initial_request.text, features="html.parser").find_all(tag)

        i = 1
        # checking if the page changed
        while self.RUNNING:
            # waiting 
            sleep(WAIT_TIME)

            # getting the page
            req = requests.get(url)
            if req.status_code != 200:
                frame.Error(f"http status code = {req.status_code}", "Error getting the url")
                return

            # parsing the new page
            try:
                new_list = BeautifulSoup(req.text, features="html.parser").find_all(tag)
            except:
                frame.Error("Error parsing or searching through the page", "Parsing error")

            # checking the the page has changed
            if init_list != new_list:
                # Set the title and message for the notification
                notification.title = "Spotted a change in the web page"
                notification.message = f"Something changed in\n{url}"
                # Display the notification
                notification.send()
                
                init_list = new_list
            else:
                frame.Print(f"Attempt {i}")
            i = i + 1

