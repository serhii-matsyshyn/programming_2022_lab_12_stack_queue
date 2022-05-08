"""Implementation of the main simulation class."""
import random

from llistqueue import Queue
from people import TicketAgent, Passenger
from ticketcounter_array import Array


class TicketCounterSimulation:
    """ Class for the simulation. """

    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        """ Initialize the simulation. """
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        """Run the simulation using the parameters supplied earlier."""
        print()
        print("Simulation starting...")
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    def printResults(self):
        """Print the simulation results."""
        passangers_in_line = (len(self._passengerQ) +
               sum([1 for agent in self._theAgents if not agent.isFree()]))
        numServed = self._numPassengers - passangers_in_line
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Simulation results:")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line (or still served) = %d" %
              passangers_in_line)
        print("The average wait time was %4.2f minutes." % avgWait)

    def _handleArrival(self, curTime):
        """Handles an arrival event."""
        if random.random() <= self._arriveProb:
            self._numPassengers += 1
            passenger = Passenger(self._numPassengers, curTime)
            print(f"Time {passenger.timeArrived(): >4}: Passenger {passenger.idNum()} arrived.")
            self._passengerQ.enqueue(passenger)

    def _handleBeginService(self, curTime):
        """Handles a begin service event."""
        if not self._passengerQ.isEmpty():
            # Find free manager
            for agent in self._theAgents:
                if agent.isFree():
                    # Assign passenger to manager
                    passenger = self._passengerQ.dequeue()
                    agent.startService(passenger, curTime + self._serviceTime)
                    print(f"Time {curTime: >4}: Agent {agent.idNum()} started serving passenger {passenger.idNum()}.")
                    break

    def _handleEndService(self, curTime):
        """Handles an end service event."""
        for agent in self._theAgents:
            if not agent.isFree():
                if agent.isFinished(curTime):
                    passenger = agent.stopService()
                    self._totalWaitTime += (curTime - passenger.timeArrived())
                    print(f"Time {curTime: >4}: Agent {agent.idNum()} stopped serving passenger {passenger.idNum()}.")
                    break


if __name__ == '__main__':
    simulation = TicketCounterSimulation(numAgents=2, numMinutes=25, betweenTime=2, serviceTime=3)
    simulation.run()
    simulation.printResults()
