class Flight:

    def __init__(self, origin, destination, duration):
        self.orign = origin
        self.destination = destination
        self.duration = duration


def main():

    #Create Flight
    f = Flight(origin="New York", destination="Paris", duration=540)

    #Change the Value of the variable
    f.duration += 10

    #print flight details
    print(f.origin)
    print(f.destination)
    print(f.duration)
