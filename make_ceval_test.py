import pandas as pd
import os
import json
import random

root = "/Users/liuxinghan/Downloads/ceval-exam/val"
out = []
label_dic = {"A": 0, "B": 1, "C": 2, "D": 3}

shots = 0

for name in os.listdir(root):
    df = pd.read_csv(root + "/" + name, sep=',', encoding='utf-8')
    demos = pd.read_csv(root.replace('/val', '/dev') + "/" + name.replace('_val', '_dev'), sep=',', encoding='utf-8')
    demolist = []
    for _, instance in enumerate(demos.to_dict(orient="records")):
        demolist.append({"question": instance["question"], "A": instance["A"], "B": instance["B"], "C": instance["C"], "D": instance["D"], 
                         "answer": instance["answer"]})

    for i, instance in enumerate(df.to_dict(orient="records")):
        info = {}
        priming = ""
        ind = [j for j in range(len(demolist))]
        random.shuffle(ind)
        for st_ind in ind[:shots]:
            example = demolist[st_ind]
            priming += example["question"]
            choices = "\n".join([example["A"], example["B"], example["C"], example["D"]])
            priming += f'\n选项：\n{choices}\n答案：{example[example["answer"]]}\n\n'


        # if len(instance["question"].split("____")) != 2:
            # print(f'{name}: {instance["question"]}')
            # continue

        info["choices_pretokenized"] = [
            instance["A"], instance["B"], instance["C"], instance["D"]
        ]
        inst_choices = "\n".join(info["choices_pretokenized"])
        inp = priming + instance["question"] + f'\n选项：\n{inst_choices}\n答案：'

        info["inputs_pretokenized"] = inp
        info["label"] = label_dic[instance["answer"]]

        out.append(json.dumps(info, ensure_ascii=False))

with open("/Users/liuxinghan/Downloads/ceval-zero-test.jsonl", "w") as f:
    f.write("\n".join(out))


# for name in os.listdir(root):
#     df = pd.read_csv(root + "/" + name, sep=',', encoding='utf-8')
#     for i, instance in enumerate(df.to_dict(orient="records")):
#         info = {}
#         if len(instance["question"].split("____")) != 2:
#             # print(f'{name}: {instance["question"]}')
#             continue

#         info["inputs_pretokenized"] = instance["question"]
#         for j in ["A", "B", "C", "D"]:
#             info["inputs_pretokenized"] += f"\n{j}. {instance[j]}"
#         info["inputs_pretokenized"] += "\n"

#         info["choices_pretokenized"] = ["A", "B", "C", "D"]
#         info["label"] = label_dic[instance["answer"]]

#         out.append(json.dumps(info, ensure_ascii=False))

# with open("/Users/liuxinghan/Downloads/ceval-choiceonly-test.jsonl", "w") as f:
#     f.write("\n".join(out))
