import os
import random
import json

shots = 0

for name in os.listdir("/Users/liuxinghan/Downloads/held-out-ZeroCLUE/"):
    if not "demo" in name:
        continue
    f_demo = open("/Users/liuxinghan/Downloads/held-out-ZeroCLUE/" + name)
    demos = f_demo.readlines()
    f_zero = open("/Users/liuxinghan/Downloads/held-out-ZeroCLUE/" + name.replace("demo", "test"))
    zeros = f_zero.readlines()
    ind = [i for i in range(len(demos))]
    few_out = []
    if not "chid" in name:
        for line in zeros[:int(len(zeros)/2)]:
            random.shuffle(ind)
            info = json.loads(line)
            demo = ""
            info["inputs_pretokenized"] = info["inputs_pretokenized"].replace('这两句话的语义是', '\n这两句话的语义是')
            info["inputs_pretokenized"] = info["inputs_pretokenized"].replace('与下面的关键词', '\n与下面的关键词')
            info["inputs_pretokenized"] = info["inputs_pretokenized"].replace('这段内容是关于', '\n这段内容是关于')
            info["inputs_pretokenized"] = info["inputs_pretokenized"].replace('这段描述的学科是', '\n这段描述的学科是')
            info["inputs_pretokenized"] = info["inputs_pretokenized"].replace('这句话的情感是', '\n这句话的情感是')
            for st_ind in ind[:shots]:
                shot = demos[st_ind]
                info_shot = json.loads(shot)
                if "ocnli" in name:
                    info_shot["inputs_pretokenized"] = info_shot['inputs_pretokenized'].replace('这两句话的语义是', '\n这两句话的语义是')
                    
                if "csl.jsonl" in name:
                    info_shot["inputs_pretokenized"] = info_shot['inputs_pretokenized'].replace('与下面的关键词', '\n与下面的关键词')
                    
                if "tnews" in name:
                    info_shot["inputs_pretokenized"] = info_shot['inputs_pretokenized'].replace('这段内容是关于', '\n这段内容是关于')
                    
                if "csldcp" in name:
                    info_shot["inputs_pretokenized"] = info_shot['inputs_pretokenized'].replace('这段描述的学科是', '\n这段描述的学科是')
                    
                if "bustm" in name:
                    info_shot["inputs_pretokenized"] = info_shot['inputs_pretokenized'].replace('这两句话的语义是', '\n这两句话的语义是')
                    
                if "iflytek" in name:
                    info_shot["inputs_pretokenized"] = info_shot['inputs_pretokenized'].replace('这段内容是关于', '\n这段内容是关于')
                    
                if "eprstmt" in name:
                    info_shot["inputs_pretokenized"] = info_shot['inputs_pretokenized'].replace('这句话的情感是', '\n这句话的情感是')
                    
                
                demo += info_shot['inputs_pretokenized']
                demo += "\n"
                demo += f"选项：{'，'.join(info_shot['choices_pretokenized'])}\n答案：{info_shot['choices_pretokenized'][info_shot['label']]}\n\n"
            inp = demo + info["inputs_pretokenized"] + f"\n选项：{'，'.join(info['choices_pretokenized'])}\n答案："
            info["inputs_pretokenized"] = inp
            few_out.append(json.dumps(info, ensure_ascii=False))
    else:
        for line in zeros[:int(len(zeros)/2)]:
            random.shuffle(ind)
            info = json.loads(line)
            demo = ""
            for st_ind in ind[:shots]:
                shot = demos[st_ind]
                info_shot = json.loads(shot)
                demo += info_shot['inputs_pretokenized'].replace("[MASK]", "____")
                demo += "\n下划线中应当填入哪个成语？\n"
                demo += f"选项：{'，'.join(info_shot['choices_pretokenized'])}\n答案：{info_shot['choices_pretokenized'][info_shot['label']]}\n\n"
            inp = demo + info["inputs_pretokenized"].replace("[MASK]", "____") + f"\n下划线中应当填入哪个成语？\n选项：{'，'.join(info['choices_pretokenized'])}\n答案："
            info["inputs_pretokenized"] = inp
            few_out.append(json.dumps(info, ensure_ascii=False))
    with open(f'/Users/liuxinghan/Downloads/held-out-ZeroCLUE-0/{name.replace("demo", "test")}', 'w') as f:
        f.write("\n".join(few_out))