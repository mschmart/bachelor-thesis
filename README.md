# Synchronization in manufacturing systems.

In my bachelor thesis we attempt to gain a more profound understanding on how does synchronization emerges and affects manufacturing systems.

It is in line with the ongoing research goal outlined in:

Chankov, S. M., Becker, T., & Windt, K. (2014). Towards Definition of Synchronization in Logistics Systems. Procedia CIRP, 17, 594-599.

We conduct an exploratory study for which I have programmed computer simulations of manufacturing systems. It is primarly implemented using the SimPy module in Python. We use the Simpy.Store container to model a queueing station in this case representing an abstraction of a work system. The files classes.py contain scalable Python classes to simulate dynamic queueing systems. The mm1.py file models an M/M/1 queue. More complex manufacturing system networks can be found in the preliminary_experiments subdirectory.

Future commits will include raw synchronization data and analysis programs.

Please contact me for further details.
