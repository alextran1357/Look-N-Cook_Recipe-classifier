from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset
import pandas as pd
from sklearn.model_selection import train_test_split

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')

# Setup the training arguments
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# data
class CustomDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item
    def __len__(self):
        return len(self.labels)

def tokenize_data(df, tokenizer):
    return tokenizer(df["Text"].tolist(), padding=True, truncation=True, return_tensors='pt')

file_path = "data/binary_class_sentences.csv"
df = pd.read_csv(file_path, header=None, names=['Text', 'Label'])
train_dataset, eval_dataset = train_test_split(df)

# Grab labels
train_labels = train_dataset["Label"].tolist()
eval_labels = eval_dataset["Label"].tolist()

# Tokenize data
tokenized_train_dataset = tokenize_data(train_dataset, tokenizer)
tokenized_eval_dataset = tokenize_data(eval_dataset, tokenizer)

# Apply labels to tokenized data
train_dataset = CustomDataset(tokenized_train_dataset, train_labels)
eval_dataset = CustomDataset(tokenized_eval_dataset, eval_labels)


training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs'
)

# Initialize trainer
trainer=Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset
)

trainer.train()