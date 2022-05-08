""" Run Ticket Counter Simulation module. """

from simulation import TicketCounterSimulation

print("Welcome to the Ticket Counter Simulation!")

number_of_minutes = int(input("Enter the number of minutes to simulate: "))
number_of_agents = int(input("Enter the number of ticket agents: "))
average_service_time = int(input("Enter the average service time per passenger: "))
average_time_between_arrivals = int(input("Enter the average time between passenger arrival: "))

simulation = TicketCounterSimulation(numAgents=number_of_agents,
                                     numMinutes=number_of_minutes,
                                     betweenTime=average_time_between_arrivals,
                                     serviceTime=average_service_time)

simulation.run()
simulation.printResults()
