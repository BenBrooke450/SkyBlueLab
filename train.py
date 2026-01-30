import torch
import torch.nn as nn

# A "Tiny" Brain
model = nn.Linear(10, 1)
data = torch.randn(5, 10)

print("SkyBlueLab System Check...")
output = model(data)
print("Brain Output successful:", output)
print("GPU Available:", torch.cuda.is_available())