class Graph:
	def __init__(self):
		self.graph = {}

	def insert_edge(self, u, v):
		""" Ensure we are processing integer first no matter the entry (file or manual call) """
		integerU = int(u)
		integerV = int(v)
		""" if u and v are the same, we must ignore the edge """
		if integerU == integerV:
			return
		list = self.graph.setdefault(integerU, [])
		if integerV not in list:
			list.append(integerV)
		else:
			print("Edge "+str(u)+"<-->"+str(v)+" already present")
			return
		list = self.graph.setdefault(integerV, [])
		""" No need to check for the existence there as if it was existing we would already have returned """
		list.append(integerU)
		""" If we did not returned yet, then v was added to the list of vertex available from u
			and u from the vertex available from v """
		print("Edge "+str(u)+"<-->"+str(v)+" added")

	def incident_edges(self, u):
		""" Ensure we are processing integer first no matter the entry
			As we are calling it manually it should always be integer
			But it makes it easier to call """
		integerU = int(u)
		""" Retrieve either the current vertex associated with u
			Or an empty list """
		list = self.graph.setdefault(integerU, [])
		""" Return the count """
		print("The number of incident edges for ["+str(u)+"] is "+str(len(list)))

	def incident_edges_list(self, u):
		""" Ensure we are processing integer first no matter the entry
			As we are calling it manually it should always be integer
			But it makes it easier to call """
		integerU = int(u)
		""" Retrieve either the current vertex associated with u
			Or an empty list """
		list = self.graph.setdefault(integerU, [])
		""" Return the list """
		print("The incident edges for ["+str(u)+"] are:")
		for node in list:
			print(str(u)+"<-->"+str(node))

	def edge_count(self):
		count=0
		for key in self.graph:
			# Retrieve the associated vertex
			list= self.graph.get(key)
			""" For every vertex accessible from that vertex we can count it as an edge
				Therefore we just add it to the final count.
				However as the graph is undirected, we will need to divide the final result by 2 in the end
				as a 0 <--> 1 edge will appear with key 0 and with key 1 """ 
			for vertex in list:
				count= count+1
		count= count/2
		print("The total number of edges for the graph is ["+str(count)+"]")


if __name__ == '__main__':
	graph = Graph()
	""" Read the file and insert the edge into the graph using the insert_edge function """
	with open('karate.edgelist.txt', 'r') as f:
		for l in f:
			""" The file contains empty lines at the end of it that we should ignore """
			if l.strip():
				n1, n2 = l.split()
				graph.insert_edge(n1,n2)
	
	""" Let's print some result after having loaded the file """
	print("*************** After file load ****************")
	graph.incident_edges(0)
	graph.incident_edges_list(0)
	graph.edge_count()
	
	""" Now add some existing edges """
	print("*************** Adding an existing edge ****************")
	graph.insert_edge(0,10)

	""" Now add some new edges """
	print("*************** Adding a new edge ****************")
	graph.insert_edge(0,17)
	graph.incident_edges(0)
	graph.incident_edges_list(0)
	graph.edge_count()