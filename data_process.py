import argparse
import json
from pathlib import Path

import pandas as pd

END_OF_CONTEXT = "<|endofcontext|>"
END_OF_TEXT = "<|endoftext|>"


def main(args):
    input_csv: Path = args.input_csv
    output_jsonl: Path = args.output_jsonl

    data = pd.read_csv(input_csv)
    data = data.drop_duplicates().dropna()
    context = data["Context"]
    response = data["Response"]
    text = "Patient: Hello, " + context + END_OF_CONTEXT + "Doctor: Hi, " + response + END_OF_TEXT

    with open(output_jsonl, "w", encoding="utf8") as fp:
        for one_row in text:
            json.dump({"text": one_row}, fp)
            fp.write("\n")

    print(text.apply(str).apply(len).max())


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_jsonl", type=Path)
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
