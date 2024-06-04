import math 
import numpy as np
from itertools import cycle

inputs = [[0,0], [0,1], [1,0], [1,1]]
outputs = [0, 1, 1, 0]

class Mlp:
    def __init__(self,input,output):
        self.input_len = input 
        self.expected_output_len = output
        self.final_output = [0] * input
        self.total = 0

        self.bias_hidden = np.random.rand(1)
        self.bias_output_hidden = np.random.rand(1)

        # self.weight_hidden = np.random.rand()
        # self.weight_output_hidden = numpy.random

    def train(self,inputs, outputs):
        self.inputs = inputs
        self.expected_outputs = outputs
        """
        Primeiro passo é verificar se ele está acertando sempre 
        """
        self.forward_pass
        # for train, target in cycle(zip(self.inputs, self.expected_outputs)):
        #     print('teste')
        #     if self.final_output == self.expected_output and self.total == len(self.final_output):
        #         break
        #     self.forward_pass


    def forward_pass(self):
        self.hidden_outputs = np.dot(self.weight_hidden,self.inputs) + self.bias_hidden 
        self.hidden_outputs_classified = self._sigmoid(self.hidden_outputs)
        self.output = np.dot(self.weight_output_hidden) + self.bias_output_hidden 
        self.final_output = self._sigmoid(self.output)
    def backward_pass(self):
        pass

        
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _delsigmoid(self, x):
        return x * (1 - x)

mlp = Mlp(2,1)
mlp.train(inputs,outputs)