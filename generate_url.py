import os
import django
from django.urls import reverse
from bangazonapi.views import OrderView

# Set the Django settings module for the 'bangazon' project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bangazon.settings")
django.setup()

from bangazonapi.views import OrderView

# Replace 'pk_value' with the actual primary key you want to use
pk_value = 6  # Replace with the desired primary key
url = reverse('order-remove-order-item', kwargs={'pk': pk_value})

print(url)
