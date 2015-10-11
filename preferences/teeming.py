#!/usr/bin/env python
from .. import modules
from ..modules.config import Preferences

# Define preferences
pref_settings = Preferences(
  'San Francisco',
  '', # 'free','paid',''
  '110', # refer to list of category ids in /modules/event_categories.csv
  'next_week', # 'this_weekend', 'this_week', 'today','tomorrow','next_week','this_month'
  'teemingchew@gmail.com'
)
# Send the email based on preferences above
modules.main.event_notif(pref_settings).email()