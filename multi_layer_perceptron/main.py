import math 

inputs = [[0,0], [0,1], [1,0], [1,1]]
outputs = [0, 1, 1, 0]

class Mlp:
    def __init__(self):
        self.final_output = [0,0,0,0]

    def train(self, inputs, outputs):
        """
        Primeiro passo é verificar se ele está acertando sempre 
        """

    def forward_pass(self):
        pass

    def backward_pass(self):
        pass

    def sigmoid(self, input):
        return 1/(1 + math.exp(-input))