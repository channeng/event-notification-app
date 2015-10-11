from eventbrite import Eventbrite
from datetime import datetime

# user = eventbrite.get_user()
# my_id = user['id']

class Methods(object):
  
  def __init__(self,api_token,user_preferences=''):
        self.api_token = api_token
        self.user_preferences = user_preferences

  def search_events(self):
    preferences = self.user_preferences
    eventbrite = Eventbrite(self.api_token)
    events = eventbrite.event_search(**{
        'venue.city': preferences.venue_city,
        'price' : preferences.price, 
        'categories' : preferences.category_id,
        'start_date.keyword': preferences.start_date_keyword
      })
    list_of_events = []
    for i in events["events"]:
      try:
        list_of_events += [{
          'event_name':i['name']['text'] if len(i['name']['text'])<50 else i['name']['text'][:50]+"...",
          'description':i['description'].get("text","")[:150]+"..." if i['description'].get("text","") != None else "",
          'start':datetime.strptime(i['start']['local'],"%Y-%m-%dT%H:%M:%S").strftime("%a, %d %b, %I:%M %p"),
          'end':datetime.strptime(i['end']['local'],"%Y-%m-%dT%H:%M:%S").strftime("%a, %d %b, %I:%M %p"),
          'url':i['url'],
          'logo':i['logo']['url']
        }]
      except TypeError:
        list_of_events += [{
          'event_name':i['name']['text'] if len(i['name']['text'])<50 else i['name']['text'][:50]+"...",
          'description':i['description'].get("text","")[:150]+"..." if i['description'].get("text","") != None else "",
          'start':datetime.strptime(i['start']['local'],"%Y-%m-%dT%H:%M:%S").strftime("%a, %d %b, %I:%M %p"),
          'end':datetime.strptime(i['end']['local'],"%Y-%m-%dT%H:%M:%S").strftime("%a, %d %b, %I:%M %p"),
          'url':i['url']
        }]
    return list_of_events

  def get_subcategories(self):
    # Get full list of subcategories
    eventbrite = Eventbrite(self.api_token)
    categories = []
    # Paginate 4 pages of responses
    for x in range(4):
      subcategories = eventbrite.get_subcategories(**{'page': str(x+1)})
      for i in subcategories["subcategories"]:
        categories += [{
          "sub_name":i["name"],
          "sub_id":i["id"],
          "parent_name":i["parent_category"]["short_name"],
          "parent_id":i["parent_category"]["id"]
        }]
    return categories

# Run 'python methods.py' in terminal to get list of subcategories
if __name__ == '__main__':
    import os
    api_token = os.environ["EVENTB_TOKEN"]
    api = Methods(api_token)
    categories = api.get_subcategories()
    for i in categories:
      print "%-20s: %-5s -- %-20s: %-5s" %(i["parent_name"],i["parent_id"],i["sub_name"],i["sub_id"])