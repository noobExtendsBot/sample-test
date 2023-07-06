from django.core.management.base import BaseCommand
from faker import Faker
from random import uniform
from locations.models import Terminal, Telementry

fake = Faker()

class Command(BaseCommand):
    help = 'Generates fake Telementry data'

    def handle(self, *args, **options):
        # Generate fake data for 10 people
        people = [fake.name() for _ in range(10)]

        for person in people:
            terminal = Terminal.objects.create(name=person)
            telementry = self.generate_fake_telementry(terminal)
            telementry.save()

    def generate_fake_telementry(self, terminal):
        longitude = uniform(-180, 180)  # Random longitude between -180 and 180
        latitude = uniform(-90, 90)     # Random latitude between -90 and 90
        return Telementry.objects.create(terminal=terminal, longitude=longitude, latitude=latitude)
