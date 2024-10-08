from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer

# Load the dataset
news = load_dataset('multi_news', split='test',trust_remote_code=True)

# Convert to pandas DataFrame
news.to_pandas()

# Split the dataset into training and testing sets
train_news = news.train_test_split(test_size=0.2)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained('t5-small')

# Define the prefix
prefix = "summarize: "

# Define the preprocessing function
def preprocess_function(examples):
    inputs = [prefix + doc for doc in examples["document"]]
    model_inputs = tokenizer(inputs, max_length=1024, truncation=True)
    labels = tokenizer(text=examples["summary"], max_length=128, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Tokenize the dataset
tokenized = train_news.map(preprocess_function, batched=True)

# Create the data collator
data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model='t5-small')

# Load the model
model = AutoModelForSeq2SeqLM.from_pretrained('t5-small')

# Define the training arguments
training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=10,
    per_device_eval_batch_size=10,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=10,
    fp16=True,
)

# Create the trainer
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized['train'],
    eval_dataset=tokenized['test'],
    tokenizer=tokenizer,
    data_collator=data_collator
)

# Train the model
trainer.train()

# Define the prediction function
def pred(document):
    device = model.device
    tokenized = tokenizer([document], return_tensors='pt')
    print(tokenized)
    tokenized = {k: v.to(device) for k, v in tokenized.items()}
    results = model.generate(**tokenized, max_length=128)
    results = results.to('cpu')
    pred = tokenizer.decode(results[0], skip_special_tokens=True)
    return pred

# Test the prediction function
document = "National Archives Yes, it's that time again, folks. It's the first Friday of the month, when for one ever-so-brief moment the interests of Wall Street, Washington and Main Street are all aligned on one thing: Jobs. A fresh update on the U.S. employment situation for January hits the wires at 8:30 a.m. New York time offering one of the most important snapshots on how the economy fared during the previous month. Expectations are for 203,000 new jobs to be created, according to economists polled by Dow Jones Newswires, compared to 227,000 jobs added in February. The unemployment rate is expected to hold steady at 8.3%. Here at MarketBeat HQ, we’ll be offering color commentary before and after the data crosses the wires. Feel free to weigh-in yourself, via the comments section. And while you're here, why don't you sign up to follow us on Twitter. Enjoy the show. ||||| Employers pulled back sharply on hiring last month, a reminder that the U.S. economy may not be growing fast enough to sustain robust job growth. The unemployment rate dipped, but mostly because more Americans stopped looking for work. The Labor Department says the economy added 120,000 jobs in March, down from more than 200,000 in each of the previous three months. The unemployment rate fell to 8.2 percent, the lowest since January 2009. The rate dropped because fewer people searched for jobs. The official unemployment tally only includes those seeking work. The economy has added 858,000 jobs since December _ the best four months of hiring in two years. But Federal Reserve Chairman Ben Bernanke has cautioned that the current hiring pace is unlikely to continue without more consumer spending."
human_summary = """– The unemployment rate dropped to 8.2% last month, but the economy only added 120,000 jobs, when 203,000 new jobs had been predicted, according to today's jobs report. Reaction on the Wall Street Journal's MarketBeat Blog was swift: "Woah!!! Bad number." The unemployment rate, however, is better news; it had been expected to hold steady at 8.3%. But the AP notes that the dip is mostly due to more Americans giving up on seeking employment."""

# Get the summary
summary = pred(document)
print(summary)



