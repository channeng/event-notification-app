from methods import Methods
from send_mail import Gmailer
import os

class event_notif(object):
  def __init__(self,Preferences):
    self.api_token = os.environ["EVENTB_TOKEN"]
    self.preference = Preferences
    self.search = Methods(self.api_token,self.preference).search_events()
  def email(self):
    Mailer = Gmailer(self.preference,self.search)
    Mailer.send_email()
  def print_search_results(self):
    results = self.search
    for i in results:
      print "Start: %s ; End: %s ; Event: %s" %(i["start"],i["end"],i["event_name"])
    print "Total = %s events found" %(len(results))