from datasets import DatasetDict, load_dataset
import csv
import json

def main():
    for split in ["train", "val", "test"]:
        input_file = csv.DictReader(open(f"train_df.csv"))

        with open(f'{split}.jsonl', 'w') as fout:
            for row in input_file:
                fout.write(json.dumps({'id': row['id'], 'text': row['text'], 'label': row['label'], 'sentiment': row['sentiment']})+"\n")
               

    """
    train_dset = load_dataset("csv", data_files="train_df.csv", split="train")
    val_dset = load_dataset("csv", data_files="val_df.csv", split="val")
    test_dset = load_dataset("csv", data_files="test_df.csv", split="test")
    raw_dset = DatasetDict()
    raw_dset["train"] = train_dset
    raw_dset["test"] = test_dset
    for split, dset in raw_dset.items():
        dset.to_json(f"{split}.jsonl")
    """

if __name__ == "__main__":
    main()
