class Flight():
    # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add a passenger to the flight:
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(4)

people = ["Zu Chen", "Steve", "Khoi", "Dick"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight succesfully!")
    else:
        print(f"Sorry, Our Flights are Full Right Now! Thank you {person}!")

