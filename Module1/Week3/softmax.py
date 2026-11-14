from torch import nn
import torch
class Softmax(nn.Module): 
    def __init__(self): 
        super().__init__()
    def forward(self, parameters): 
        return torch.exp(parameters) / torch.sum(torch.exp(parameters))
class Softmax_stable(nn.Module):
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

    softmax_stable = Softmax_stable()
    output = softmax_stable(data)
    print(output)