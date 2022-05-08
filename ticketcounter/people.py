""" Module for the People class. """


class Passenger:
    """Used to store and manage information related to an airline passenger."""

    def __init__(self, idNum, arrivalTime):
        """Initializes the passenger's id number and arrival time."""
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    def idNum(self):
        """Gets the passenger's id number."""
        return self._idNum

    def timeArrived(self):
        """Gets the passenger's arrival time."""
        return self._arrivalTime


class TicketAgent:
    """Used to store and manage information related to an airline ticket agent."""

    def __init__(self, idNum):
        """Initializes the ticket agent's id number."""
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    def idNum(self):
        """Gets the ticket agent's id number."""
        return self._idNum

    def isFree(self):
        """Returns True if the ticket agent is free to assist a passenger."""
        return self._passenger is None

    def isFinished(self, curTime):
        """Returns True if the ticket agent has finished helping the passenger."""
        return self._passenger is not None and self._stopTime <= curTime

    def startService(self, passenger, stopTime):
        """Indicates the ticket agent has begun assisting a passenger."""
        self._passenger = passenger
        self._stopTime = stopTime

    def stopService(self):
        """Indicates the ticket agent has finished assisting a passenger."""
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger
