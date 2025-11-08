import numpy as np


def sigmoid(x):
  # Our activation function: f(x) = 1 / (1 + e^(-x))
  return 1 / (1 + np.exp(-x))

class Neuron:
  def __init__(self,weights,bias):
    self.bias = bias
    self.weights = weights

  def feedforward(self, input):
    total = np.dot( input,self.weights) + self.bias
    return sigmoid(total)
  
weights =  np.array([0,2])
input = np.array([0,1])
bias  = 4 
neuron = Neuron(weights, bias)


print(neuron.feedforward(input))
