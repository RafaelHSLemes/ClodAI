import torch
print(torch.cuda.is_available())  # Deve retornar True
print(torch.cuda.device_count())  # Número de GPUs disponíveis
print(torch.cuda.get_device_name(0))  # Nome da GPU