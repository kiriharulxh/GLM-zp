

date_time_chinese = input("data-time-chinese: ")
date_time_chiflan = input("data-time-chiflan: ")

chinese = {
    "ZeroCLUE": {"cnt": [], "acc": []},
    "pclue_cls": {"cnt": [], "acc": []},
    "pclue_nli": {"cnt": [], "acc": []},
    "pclue_mrc": {"cnt": [], "acc": []},
    "ceval_choice": {"cnt": [], "acc": []},
    "ceval": {"cnt": [], "acc": []},
}

chiflan = chinese

for i in range(8):
    f = open(f"eval/heldout{i}-{date_time_chinese}-chinese.txt")
    g = open(f"eval/heldout{i}-{date_time_chiflan}-chiflan.txt")
    for line in f.readlines():
        if "|epoch: -1| metrics for multichoice-ZeroCLUE-test" in line:
            chinese["ZeroCLUE"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chinese["ZeroCLUE"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-pclue-cls-test" in line:
            chinese["pclue_cls"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chinese["pclue_cls"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-ceval-choiceonly-test" in line:
            chinese["ceval_choice"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chinese["ceval_choice"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-pclue-nli-test" in line:
            chinese["pclue_nli"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chinese["pclue_nli"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-pclue-mrc-test" in line:
            chinese["pclue_mrc"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chinese["pclue_mrc"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-ceval-test" in line:
            chinese["ceval"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chinese["ceval"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
    for line in g.readlines():
        if "|epoch: -1| metrics for multichoice-ZeroCLUE-test" in line:
            chiflan["ZeroCLUE"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chiflan["ZeroCLUE"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-pclue-cls-test" in line:
            chiflan["pclue_cls"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chiflan["pclue_cls"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-ceval-choiceonly-test" in line:
            chiflan["ceval_choice"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chiflan["ceval_choice"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-pclue-nli-test" in line:
            chiflan["pclue_nli"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chiflan["pclue_nli"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-pclue-mrc-test" in line:
            chiflan["pclue_mrc"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chiflan["pclue_mrc"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
        if "|epoch: -1| metrics for multichoice-ceval-test" in line:
            chiflan["ceval"]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chiflan["ceval"]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])

for name in chinese:
    print(f"{name}: ")
    sum_chin, sum_chif = 0, 0
    for i in range(8):
        assert chinese[name]["cnt"][i] == chiflan[name]["cnt"][i]
        print(f'{i}: chinese: {chinese[name]["acc"][i]}%    chiflan: {chiflan[name]["acc"][i]}%')
        sum_chin += eval(chinese[name]["acc"][i]) * eval(chinese[name]["cnt"][i])
        sum_chif += eval(chiflan[name]["acc"][i]) * eval(chinese[name]["cnt"][i])
    cnt = sum([cc for cc in chinese[name]["cnt"]])
    print(f'avg: chinese: {sum_chin/cnt}    chiflan: {sum_chif/cnt}')
