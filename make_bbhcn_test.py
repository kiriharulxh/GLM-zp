import os
import json

hm_dir = "/Users/liuxinghan/Downloads/bbh_translation/"
en_dir = "/Users/liuxinghan/Downloads/BBH_en_few_shot_cot/"
os.mkdir("/Users/liuxinghan/Downloads/bbhcn")
os.mkdir("/Users/liuxinghan/Downloads/bbhcn-choice")

# label_dic = {"(A)": 0, "(B)": 1, "(C)": 2, "(D)": 3}
for name in os.listdir(hm_dir):
    if name.startswith("gsm8k"):
        continue
    f = open(hm_dir+name)
    name = name.split(".jsonl")[0] + ".jsonl"
    g = open(en_dir+name)
    outs_choice = []
    outs = []
    lsf, lsg = f.readlines(), g.readlines()
    assert len(lsf) == len(lsg), name
    for line, aux in zip(lsf, lsg):
        info = json.loads(line)
        info_aux = json.loads(aux)
        if not info.get('question-en'):
            print(f"no en question: {name}")
            break
        # a = info["question-en"].strip(" ").split("\n")[0].strip()
        # b = info_aux["input"].split("\n\n")[-1].split("\n")[0].strip("Q")
        # if not a in b:
        #     for j in range(len(a)):
        #         if a[j] != b[j+2]:
        #             print(j)
        #             print(f"a: {a[j]} b: {b[j+2]}")
        #             print(f"a: {a[j-3:j+3]} b: {b[j-1: j+5]}")
        
        assert (info["question-en"].strip() in info_aux["input"].split("\n\n")[-1] or \
              all([ques.strip() in info_aux["input"].split("\n\n")[-1] for ques in info["question-en"].strip(" ").split("\n")]), "\n".join([name, line]) or \
              info["question-en"].replace("\xa0", " ").strip() in info_aux["input"].split("\n\n")[-1] or \
              all([ques.strip() in info_aux["input"].split("\n\n")[-1] for ques in info["question-en"].replace("\xa0", " ").strip(" ").split("\n")])),  "\n".join([name, line])
        

        inp = info["question-cn"]
        if not info.get("choices-cn"):
            print(f"no choice: {name}")
            break
        if name == "date_understanding.jsonl" and info["choices-cn"].startswith("error"):
            info["choices-cn"] = info["choices-en"]
        info["choices-cn"] = info["choices-cn"].replace("（", "(").replace("）", ") ")
        choices = info["choices-cn"].split("\n")
        try:
            if name == "boolean_expressions.jsonl":
                assert info["choices-cn"] == "假\n   真"
                choices = [c.strip() for c in choices]
            elif name == "navigate.jsonl":
                assert info["choices-cn"] == "不会\n   会"
                choices = [c.strip() for c in choices]
            elif name == "formal_fallacies.jsonl":
                assert info["choices-cn"] == "- 有效\n   - 无效"
                choices = ["有效", "无效"]
            elif name == "causal_judgement.jsonl" or name == "web_of_lies.jsonl":
                assert info["choices-cn"] == "否\n   是"
                choices = ["否", "是"]
            elif name == "sports_understanding.jsonl":
                assert info["choices-cn"] == "不合理\n   合理"
                choices = [c.strip() for c in choices]
            else:
                choices = [c.split(")")[1].strip() for c in choices]
        except:
            print("\n".join([name, line]))
            exit(0)
        if name == "boolean_expressions.jsonl":
            label_dic = {"假":0, "真":1}
            aux_dic = {"False": 0, "True": 1}
        elif name == "navigate.jsonl":
            label_dic = {"不会":0, "会":1}
            aux_dic = {"No": 0, "Yes": 1}
        elif name == "formal_fallacies.jsonl":
            label_dic = {"有效":0, "无效":1}
            aux_dic = {"valid": 0, "invalid": 1}
        elif name == "causal_judgement.jsonl" or name == "web_of_lies.jsonl":
            label_dic = {"否":0, "是":1}
            aux_dic = {"No": 0, "Yes": 1}
        elif name == "sports_understanding.jsonl":
            label_dic = {"不合理":0, "合理":1}
            aux_dic = {"no": 0, "yes": 1}
        else:
            label_dic = {'('+f'{chr(ord("A")+ i)}'+')' : i for i in range(len(choices))}
            aux_dic = label_dic
        if not info.get("answer"):
            assert aux_dic.get(info_aux["targets"][0]) is not None,  "\n".join([name, line, str(aux_dic), info_aux["targets"][0]])
            ans = aux_dic[info_aux["targets"][0]]
        else:
            ans = label_dic[info["answer"]]
        outs.append(
            json.dumps({"inputs_pretokenized": inp, "choices_pretokenized": choices, "label": ans}, ensure_ascii=False)
        )

        inp_choice = info["question-cn"]
        if not info["question-cn"].strip(" ").endswith("\n"):
            inp_choice += "\n"
        inp_choice += info["choices-cn"]
        assert not info["choices-cn"].endswith("\n"), name
        inp_choice += "\n"
        inp_choice += "答案: "
        choices_choice = [k for k in label_dic]
        ans_choice = ans
        outs_choice.append(
            json.dumps({"inputs_pretokenized": inp_choice, "choices_pretokenized": choices_choice, "label": ans_choice}, ensure_ascii=False)
        )
    f.close()

    if outs == []:
        continue
    with open(f"/Users/liuxinghan/Downloads/bbhcn/{name}", "w") as bbhcn:
        bbhcn.write("\n".join(outs))
    
    with open(f"/Users/liuxinghan/Downloads/bbhcn-choice/{name}", "w") as bbhcn_choice:
        bbhcn_choice.write("\n".join(outs_choice))

