import sentencepiece as spm

# Caminho do corpus de treinamento
corpus_path = "C:/Users/Usuario/Desktop/ClodAI/src/utils/data/processed/final_training_data.txt"
model_prefix = "tokenizer"

# Treinar o modelo
spm.SentencePieceTrainer.train(
    input=corpus_path,
    model_prefix=model_prefix,
    vocab_size=1000,
    model_type='bpe',
    character_coverage=0.9995
)

print("Treinamento concluído! Arquivo tokenizer.model gerado!")