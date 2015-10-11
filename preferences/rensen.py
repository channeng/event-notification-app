#!/usr/bin/env python
from .. import modules
from ..modules.config import Preferences

# Define preferences
pref_settings = Preferences(
  'San Francisco',
  '', # 'free','paid',''
  '101,102,107,108,109,116', # refer to list of category ids in /modules/event_categories.csv
  'this_weekend', # 'this_weekend', 'this_week', 'today','tomorrow','next_week','this_month'
  'horensen@live.com'
)
# Send the email based on preferences above
modules.main.event_notif(pref_settings).email()