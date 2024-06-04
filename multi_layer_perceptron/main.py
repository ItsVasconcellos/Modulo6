import math 
import numpy as np
from itertools import cycle

inputs = [[0,0], [0,1], [1,0], [1,1]]
outputs = [0, 1, 1, 0]

class Mlp:
    def __init__(self, input_len, output_len):
        self.input_len = input_len
        self.expected_output_len = output_len
        self.final_output = np.zeros(input_len)  # Initialize as NumPy array

        self.bias_hidden = np.random.rand(2)
        self.bias_output_hidden = np.random.rand(1)

        self.weight_hidden = np.random.uniform(size=(self.input_len, 2)) 
        self.weight_output_hidden = np.random.uniform(size=(2, self.expected_output_len))

    def train(self, inputs, outputs, epochs=100):
        self.inputs = np.array(inputs)  # Ensure inputs is a NumPy array
        self.expected_outputs = outputs
        for epoch in range(epochs):
            accuracy = 0
            for train, target in zip(self.inputs, self.expected_outputs):
                self.forward_pass(self.inputs)
                if np.round(self.final_output[0]) == target:
                    accuracy += 1
                self.backward_pass(learning_rate=0.1)  # Fixed learning rate
     
    def forward_pass(self, inputs):
        self.inputs = np.array(inputs)
        self.hidden_outputs = np.dot(self.inputs,self.weight_hidden) + self.bias_hidden 
        self.hidden_outputs_classified = self._sigmoid(self.hidden_outputs)
        self.output = np.dot(self.hidden_outputs_classified, self.weight_output_hidden) + self.bias_output_hidden 
        self.final_output = self._sigmoid(self.output)
        self.final_output = self.final_output.flatten()
        self.final_output = [int(round(x)) for x in self.final_output]
        return self.final_output

    def backward_pass(self, learning_rate):
        output_error = np.subtract(self.final_output, self.expected_outputs)
        output_error = output_error.reshape(4, 1)  # Reshape for matrix multiplication
        hidden_error = np.dot(output_error, self.weight_output_hidden.T) * self._delsigmoid(self.hidden_outputs_classified)

        self.weight_output_hidden -= learning_rate * np.dot(self.hidden_outputs_classified.T, output_error)
        self.bias_output_hidden -= learning_rate * output_error.sum()
        self.weight_hidden -= learning_rate * np.dot(self.inputs.T, hidden_error)
        self.bias_hidden -= learning_rate * hidden_error.sum()

        
    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _delsigmoid(self, x):
        return x * (1 - x)

mlp = Mlp(2, 1)
mlp.train(inputs, outputs, epochs=1000)  
for input_data in inputs:
    output = mlp.forward_pass(input_data)
    print(f"Input: {input_data} -> Output: {output}")