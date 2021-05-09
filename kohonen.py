import numpy as np

class Kohonen(object):

	def __init__(self, h, w, dim, alpha0=0.5, sigma = 1.2):
		self.shape = (h,w,dim)
		self.som= np.array([[ (j/h, i/w) for i in range(w) ] for j in range(h)])
		self.data = []
		self.alpha0 = alpha0
		self.sigma = sigma
		self.lamb = 300

		self.steps = 300
		self.step = 0

	def train(self, training_data): 
		self.data = training_data
		for t in range(self.steps):
			index = np.random.choice(range(len(self.data)))

			best_neuron = self.find_best_neuron(self.data[index])
			self.update_som(best_neuron, self.data[index], t)

	def train_step(self, training_data): 
		self.data = training_data
		index = np.random.choice(range(len(self.data)))
		best_neuron = self.find_best_neuron(self.data[index])
		self.update_som(best_neuron, self.data[index], self.step)
		self.step += 1


	def find_best_neuron(self, start):
		neuron_list = []
		for x in range(self.shape[0]):
			for y in range(self.shape[1]):
				self.som[x, y]
				dist = np.linalg.norm(start - self.som[x, y])
				neuron_list.append(((x,y),dist))

		neuron_list.sort(key=lambda x:x[1])
		return neuron_list[0][0]

	def update_som(self, best_neuron, data_point, step):
		for x in range(self.shape[0]):
			for y in range(self.shape[1]):
				dist_to_best_neuron = np.linalg.norm(np.array(best_neuron) - np.array([x,y]))
				self.update_cell((x,y), data_point, step, dist_to_best_neuron)

	def update_cell(self, cell, data_point, t, dist):
		self.som[cell] += self.alpha(t) * self.G(dist)*(data_point - self.som[cell])

	def alpha(self, t):
		return self.alpha0 * np.exp(-t/self.lamb)
  
	def G(self, dist):
		return np.exp(-dist**2/(2*self.sigma**2))