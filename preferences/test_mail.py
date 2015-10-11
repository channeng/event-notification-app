#!/usr/bin/env python
from .. import modules
from ..modules.config import Preferences

# Define preferences
pref_settings = Preferences(
  'San Francisco',
  'free', # or 'paid'
  '102,103,109,119',
  'this_weekend', # or 'this_week', 'today','tomorrow','next_week','this_month'
  'channeng@hotmail.com'
)
# Send the email based on preferences above
modules.main.event_notif(pref_settings).email()