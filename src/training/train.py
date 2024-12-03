from torch.utils.data import DataLoader, Dataset
from model.entrepreneurGPT import model, optimizer, criterion

# Definir o caminho do arquivo de texto com os dados pré-processados
DATA_FILE_PATH = 'C:/Users/Usuario/Desktop/ClodAI/src/utils/data/processed/final_training_data.txt'
num_epochs = 160

with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
    train_data = file.readlines()

class EntrepreneurDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

train_loader = DataLoader(EntrepreneurDataset(train_data), batch_size=32, shuffle=True)

for epoch in range(num_epochs):
    model.train()
    for batch in train_loader:
        src, tgt = batch['input'], batch['target']
        optimizer.zero_grad()
        output = model(src, tgt)
        loss = criterion(output.view(-1, output.size(-1)), tgt.view(-1))
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}")