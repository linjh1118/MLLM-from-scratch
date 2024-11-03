import wandb
from datasets import load_dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments



# 加载数据集
# 将hf链接改成hf镜像链接
import os

# 指定数据集目录
data_dir = '/workspace/linjh/CoT_Factory/MLLM-from-scratch/assets/datasets/stanfordnlp/imdb/plain_text'

# 加载本地数据集
dataset = load_dataset('parquet', data_files={
    'train': f'{data_dir}/train-00000-of-00001.parquet',
    'test': f'{data_dir}/test-00000-of-00001.parquet',
    'unsupervised': f'{data_dir}/unsupervised-00000-of-00001.parquet'
})

# 1. zsh $ wandb login (later will prompt you input your wandb apikey)   2. wandb init, wandb log, (wandb finish).  3. You could watch the progress online.  
# 初始化wandb
wandb.init(project="simple-text-classification")
# 加载预训练模型和分词器
model_name = '/workspace/linjh/CoT_Factory/MLLM-from-scratch/assets/models/distilbert/distilbert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# 数据预处理
def tokenize_function(examples):
    return tokenizer(examples['text'], padding='max_length', truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# 准备数据集
small_train_dataset = tokenized_datasets['train'].shuffle(seed=42).select(range(3000))
small_eval_dataset = tokenized_datasets['test'].shuffle(seed=42).select(range(3000))

# 定义训练参数
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    logging_dir='./logs',
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=100,
    weight_decay=0.01,
    logging_steps=10,
    report_to='wandb'  # 使用wandb报告指标
)

# 定义Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset
)

# 开始训练
trainer.train()

# 结束wandb运行
wandb.finish()
