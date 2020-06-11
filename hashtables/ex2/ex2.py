#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    trip_dict = {}

    route = [None] * length

    for t in tickets:
        trip_dict[t.source] = t.destination

    cur = "NONE"

    for i in range(length):
        route[i] = trip_dict.get(cur)
        cur = route[i]
    return route
