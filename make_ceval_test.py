import pandas as pd
import os
import json

root = "/Users/liuxinghan/Downloads/ceval-exam/val"
out = []
label_dic = {"A": 0, "B": 1, "C": 2, "D": 3}
for name in os.listdir(root):
    df = pd.read_csv(root + "/" + name, sep=',', encoding='utf-8')
    for i, instance in enumerate(df.to_dict(orient="records")):
        info = {}
        if len(instance["question"].split("____")) != 2:
            # print(f'{name}: {instance["question"]}')
            continue

        info["inputs_pretokenized"] = instance["question"].replace("____", "[MASK]")
        info["choices_pretokenized"] = [
            instance["A"], instance["B"], instance["C"], instance["D"]
        ]
        info["label"] = label_dic[instance["answer"]]

        out.append(json.dumps(info, ensure_ascii=False))

with open("/Users/liuxinghan/Downloads/ceval-test.jsonl", "w") as f:
    f.write("\n".join(out))
