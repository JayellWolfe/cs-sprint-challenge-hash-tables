#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    flts = {}
    rte = [None] * length 
    for i in range(0, length):
        c = tickets[i]
       
        flts[c.source] = c.destination
    
    rte[0] = flts["NONE"]
    rte[1] = flts[rte[0]]
    
    if length > 2:
        for i in range(2, length):
            rte[i] = flts[rte[i - 1]]
    return rte
