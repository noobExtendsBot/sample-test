from faker import Faker
from random import uniform
from collections import defaultdict

fake = Faker()

class Terminal:
    def __init__(self, name, is_active=True):
        self.created_at = fake.date_time_this_decade()
        self.name = name
        self.is_active = is_active


class Telementry:
    def __init__(self, terminals, longitude, latitude):
        # terminals will be a list
        self.created_at = fake.date_time_this_decade()
        self.terminals = terminals
        self.longitude = longitude
        self.latitude = latitude


def generate_fake_telementry(terminals):
    longitude = uniform(-180, 180)  # Random longitude between -180 and 180

    # Generate latitude, ensuring some instances are in the Northern Hemisphere
    if len(terminals) < 3:
        # Random latitude between -90 and 90
        latitude = uniform(-90, 90)
    else:
        # Random latitude between 0 and 90 (Northern Hemisphere)
        latitude = uniform(0, 90)

    return Telementry(terminals, longitude, latitude)


if __name__ == "__main__":
    # Generate fake data for 10 people or Terminal (treating each as Person to user fake.name())
    people = [fake.name() for _ in range(10)]

    telementry_list = []
    # A list so that Telementry object can have multiple Terminal for the same object
    terminals = []

    for person in people:
        terminal = Terminal(person)
        terminals.append(terminal)

        telementry_list.append(generate_fake_telementry([terminal]))

    # Calculate average latitude and longitude for each unique Terminal name
    terminal_data = defaultdict(list)
    northern_terminals = []

    for telementry in telementry_list:
        for terminal in telementry.terminals:
            terminal_data[terminal.name].append((telementry.longitude, telementry.latitude))

            if telementry.latitude >= 0:
                northern_terminals.append(terminal.name)

    # Print average latitude and longitude for each unique Terminal name
    for name, coordinates in terminal_data.items():
        longitudes, latitudes = zip(*coordinates)
        average_longitude = sum(longitudes) / len(longitudes)
        average_latitude = sum(latitudes) / len(latitudes)

        print(f"Terminal Name: {name}")
        print(f"Average Longitude: {average_longitude}")
        print(f"Average Latitude: {average_latitude}")
        print()

    # Print Terminals in the Northern Hemisphere
    print("Terminals in the Northern Hemisphere:")
    for name in set(northern_terminals):
        print(name)
