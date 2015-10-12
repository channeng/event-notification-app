#!/usr/bin/env python
import event_notification_app.modules
from modules.config import Preferences
from ..subscribe.models import Subscriptions
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "..mysite.settings")

# your imports, e.g. Django models
from your_project_name.models import Subscriptions

# From now onwards start your script..

if __name__ == '__main__':
	for i in Subscriptions.objects.all():
		category_ids = []
		# i.event_categories.all()[0].category_id
		for event_cat in i.event_categories.all():
			category_ids += [event_cat.category_id]
		# Define preferences
		pref_settings = Preferences(
			i.city,
			i.event_type,
			category_ids,
			i.period,
			i.email
			)
		# Send the email based on preferences above
		print pref_settings
		# modules.main.event_notif(pref_settings).email()
