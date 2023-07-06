import os
import sys
import django

# Adjust the project name
PROJECT_NAME = 'testsite'

# Set up Django environment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.join(BASE_DIR, PROJECT_NAME)
sys.path.append(PROJECT_PATH)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{PROJECT_NAME}.settings')
django.setup()

from django.db.models import Avg
from locations.models import Terminal

# Queryset to calculate average longitude and latitude for each terminal
terminals = Terminal.objects.annotate(
    avg_longitude=Avg('terminal_telementry__longitude'),
    avg_latitude=Avg('terminal_telementry__latitude')
).filter(avg_latitude__gte=0)

# Printing terminals with average position in the Northern Hemisphere
for terminal in terminals:
    print(f"Terminal Name: {terminal.name}")
    print(f"Average Longitude: {terminal.avg_longitude}")
    print(f"Average Latitude: {terminal.avg_latitude}")
    print()
