"""
Simulation program ADMM.
Assembly line for short study.

Medium arrival rate: 0.30
Medium service rate: 0.55
"""
from __future__ import division

import random
import numpy as np
import functools
import simpy
import csv
import os.path
from classes import Generator, Sink, Workstation, Monitor, Inventory

#Interarrival and service time.
def Arrival():
	return 1.0/0.3

def Service():
	return 1.0/0.55

if __name__ == '__main__':
	sim_id = 'ADMM'
	env = simpy.Environment()
	
	#Distribution
	Sampling = functools.partial(random.expovariate, 1.0)

	#Elements
	gen = dict()
	for i in range(3):
		gen[i] = Generator(env, "G" + str(i), interarr=Arrival)

	sink = dict()
	for i in range(3):
		sink[i] = Sink(env, "S" + str(i))

	ws= dict()
	for i in range(30):
		ws[i] = Workstation(env, "WS" + str(i), servtime=Service, rec_csv=True, csv_name=sim_id)

	#Monitor
	mon = dict()
	for i in range(30):
		mon[i] = Monitor(env, ws[i], Sampling())

	inv = Inventory(env, gen, sink, Sampling())

	#Routing

	#First line.
	gen[0].out = ws[0]
	ws[0].out = ws[1]
	ws[1].out = ws[2]
	ws[2].out = ws[3]
	ws[3].out = ws[4]
	ws[4].out = ws[5]
	ws[5].out = ws[6]
	ws[6].out = ws[7]
	ws[7].out = ws[8]
	ws[8].out = ws[9]
	ws[9].out = sink[0]

	#Second line.
	gen[1].out = ws[10]
	ws[10].out = ws[11]
	ws[11].out = ws[12]
	ws[12].out = ws[13]
	ws[13].out = ws[14]
	ws[14].out = ws[15]
	ws[15].out = ws[16]
	ws[16].out = ws[17]
	ws[17].out = ws[18]
	ws[18].out = ws[19]
	ws[19].out = sink[1]

	#Third line.
	gen[2].out = ws[20]
	ws[20].out = ws[21]
	ws[21].out = ws[22]
	ws[22].out = ws[23]
	ws[23].out = ws[24]
	ws[24].out = ws[25]
	ws[25].out = ws[26]
	ws[26].out = ws[27]
	ws[27].out = ws[28]
	ws[28].out = ws[29]
	ws[29].out = sink[2]  

	#Run!
	env.run(until=1000)

	#Concatanate lists.
	throughputs = []
	for i in sink:
		throughputs += sink[i].ttp

	utils = []
	for i in mon:
		utils += mon[i].util

	q = []
	for i in mon:
		q += mon[i].queue

	#Performance
	mean_throughput = np.mean(throughputs)
	var_throughput = np.var(throughputs)
	cap_util = np.mean(utils)
	wip = np.mean(inv.wiplevels)
	qlen = np.mean(q) #Mean queue size. An alternative performance measure not commonly used in manufacturing.

	#Performance CSV Writer
	save_path = '/Users/manuelschipper/Documents/spring_15/thesis/07-Test/simulations/REC_DATA'
	name_of_file = 'performance'
	complete_filename = os.path.join(save_path, name_of_file + '.csv')
	sectarget = open(complete_filename, 'a')
	try:
		write = csv.writer(sectarget)
		write.writerow((sim_id, mean_throughput, var_throughput, cap_util, wip, qlen))
	except:
		raise Exception('Error writing performance into CSV file')
	finally:
		sectarget.close()
