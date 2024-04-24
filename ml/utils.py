from __future__ import annotations

from pathlib import Path

import pandas as pd
from datasets import (
    Dataset,
    DatasetDict,
)
from transformers import (
    GPT2Tokenizer,
)


def generate_dataset(dataset_path: str | Path, tokenizer: GPT2Tokenizer) -> DatasetDict:
    data = pd.read_csv(dataset_path)
    # Drop the records which has missing values
    data = data.dropna()

    data["text"] = data["Context"] + " <SEP> " + data["Response"]
    dataset = Dataset.from_pandas(data)

    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)
    tokenized_datasets.set_format(type="torch", columns=["input_ids", "attention_mask"])

    train_test_dataset = tokenized_datasets.train_test_split(test_size=0.2)
    test_valid_dataset = train_test_dataset["test"].train_test_split(test_size=0.5)

    return DatasetDict({
        "train": train_test_dataset["train"],
        "validation": test_valid_dataset["test"],
        "test": test_valid_dataset["train"],
    })


__all__ = [
    "generate_dataset",
]
