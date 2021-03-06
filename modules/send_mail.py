#!/usr/bin/env python
import smtplib
import os
from generate_html import Generate_html
import datetime
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

class Gmailer(object):
  def __init__(self,user_preferences,search):
    # Login credentials
    self.gmail_user = os.environ["GMAIL_SERVER"]
    self.gmail_pwd = os.environ["GMAIL_PWD"]
    self.recipients = user_preferences.email
    self.search = search
    
    categories = {}
    with open(os.path.abspath("event_notification_app/modules/event_categories.csv"),'r') as f:
      reader = csv.reader(f)
      for row in reader:
        categories[row[1]]=row[0]
    categories_id = user_preferences.category_id#.split(",") No need split now since category_id is [110,111,etc.]
    # print categories_id
    list_of_categories = []
    for i in categories_id:  # i is an int
      list_of_categories += [categories[str(i)]] # categories{} only accept string keys
    self.category = ", ".join(list_of_categories)
    
    price = user_preferences.price
    if price == '':
      free_paid = 'All'
    elif price == 'free':
      free_paid = 'Free'
    elif price == 'paid':
      free_paid = 'Paid'
    self.free_paid = free_paid
    
    self.period = user_preferences.start_date_keyword.replace("_"," ")
    self.city = user_preferences.venue_city.title()
    self.first_name = user_preferences.first_name.title()

  
  def send_email(self):
    gmail_user = self.gmail_user
    gmail_pwd = self.gmail_pwd
    recipients = self.recipients
    to_who = recipients if type(recipients) is list else [recipients]
    # Create message container - the correct MIME type is multipart/alternative.
    message = MIMEMultipart('alternative')
    message['Subject'] = "Upcoming Events for the weekend!"
    message['From'] = "Shannon"
    message['To'] = ", ".join(to_who)

    # Create the body of the message (a plain-text and an HTML version).
    text = "Check out events happening in " + self.city + " " + self.period + "!"
    html = str(Generate_html(self.search,self.free_paid,self.category,self.period,self.city,self.first_name).generate_html())
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    
    message.attach(part1)
    message.attach(part2)
    # print "Attached message"
    # Prepare actual message
    # message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    #     """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    if html == "None": # Checks if HTML is generated. Returns "None" if no results found.
      print 'Events Report - NO RESULTS found %-20s | Name: %-15s | Email: %-30s' %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.first_name,self.recipients)
    else:
      try:
        # print "Connecting to SMTP"
        server = smtplib.SMTP('smtp.gmail.com',587) #587
        # print "Connected. Establishing ping.."
        server.ehlo()
        # print "ehlo"
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(gmail_user, recipients, message.as_string())
        server.close()
        print 'Events Report - SENT             %-20s | Name: %-15s | Email: %-30s' %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.first_name,self.recipients)  
      except:
        print 'Events Report - FAILED           %-20s | Name: %-15s | Email: %-30s' %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.first_name,self.recipients)