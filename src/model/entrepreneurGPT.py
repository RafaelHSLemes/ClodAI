import torch
import torch.nn as nn

class EntrepreneurGPT(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_layers, batch_first):
        super(EntrepreneurGPT, self).__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.transformer =  nn.Transformer(d_model, nhead, num_layers, batch_first)
        self.fc_out = nn.Linear(d_model, vocab_size)

    def foward(self, src, tgt):
        src_emb = self.embedding(src)
        tgt_emb = self.embedding(tgt)
        transformer_out = self.transformer(src_emb, tgt_emb)
        return self.fc_out(transformer_out)
    
#Inicialização
model = EntrepreneurGPT(vocab_size=50000, d_model=512, nhead=8, num_layers=6, batch_first=True)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)