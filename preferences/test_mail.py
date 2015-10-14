#!/usr/bin/env python
from .. import modules
from ..modules.config import Preferences

# Define preferences
pref_settings = Preferences(
  'shannon',
  'San Francisco',
  'free', #d'
  ['102','103','109','119'],
  'this_weekend', # or 'this_week', 'today','tomorrow','next_week','this_month'
  'channeng@hotmail.com'
)

# Send the email based on preferences above
# modules.main.event_notif(pref_settings).email()

# Prints results to terminal
modules.main.event_notif(pref_settings).print_search_results()
