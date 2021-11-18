"""
    Stores informatation about the total number of attendees for a given date
"""
class Participants:
    def __init__(self,date,total):
        self.date = date
        self.total = total
    
    """
        Implements the greater then or  '>'  for this class.
    """
    def __gt__(self,other):
        # If two dates have same number of attendees then we chose the one with an 
        # earlier date
        if self.total == other.total:
            return self.date < other.date
        
        # Else we return the one with more attendees
        return self.total > other.total