import torch
from torch import nn


class Softmax(nn.Module): 
    def __init__(self): 
        super().__init__()

    def forward(self, parameters): 
        return torch.exp(parameters) / torch.sum(torch.exp(parameters))

    
class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, parameters):
        max_element = torch.max(parameters) 
        return torch.exp(parameters - max_element)/ torch.sum(torch.exp(parameters - max_element))


if __name__ == "__main__": 
    data = torch.tensor([1, 2, 1000000000000000]) 
    softmax = Softmax() 
    output = softmax(data)
    print(output, "\n\n")

    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    print(output)