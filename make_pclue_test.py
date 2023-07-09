import json
import os

nli_out = []
cls_out = []
mrc_out =[]
allcnt = 0
cnt = 0
with open("/Users/liuxinghan/Downloads/PCLUE/datasets/pCLUE_test_public_1.json") as f:
    ls = f.readlines()
    for line in ls:
        info = json.loads(line)
        if info["type"] == "generate" or not info.get("answer_choices"):
            continue
        out_info = {}
        out_info["inputs_pretokenized"] = info["input"]
        out_info["choices_pretokenized"] = info["answer_choices"]
        try:
            out_info["label"] = info["answer_choices"].index(info["target"])
        except ValueError:
            continue

        if info["type"] == "nli":
            nli_out.append(json.dumps(out_info, ensure_ascii=False))
        elif info["type"] == "classify":
            cls_out.append(json.dumps(out_info, ensure_ascii=False))
        elif info["type"] == "mrc":
            mrc_out.append(json.dumps(out_info, ensure_ascii=False))


with open("/Users/liuxinghan/Downloads/pclue-nli-test.jsonl", "w") as f:
    f.write("\n".join(nli_out))

with open("/Users/liuxinghan/Downloads/pclue-cls-test.jsonl", "w") as f:
    f.write("\n".join(cls_out))

with open("/Users/liuxinghan/Downloads/pclue-mrc-test.jsonl", "w") as f:
    f.write("\n".join(mrc_out))
