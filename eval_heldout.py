from copy import deepcopy

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

chiflan = deepcopy(chinese)

for i in range(8):
    f = open(f"eval/heldout{i}-{date_time_chinese}-chinese.txt")
    g = open(f"eval/heldout{i}-{date_time_chiflan}-chiflan.txt")
    for line in f.readlines():
        if "|epoch: -1| metrics for" in line:
            test_name = line.split("|epoch: -1| metrics for ")[1].split(": total")[0]
            if not chinese.get(test_name):
                chinese[test_name] = {"cnt": [], "acc": []}
            chinese[test_name]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chinese[test_name]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])
    for line in g.readlines():
        if "|epoch: -1| metrics for" in line:
            test_name = line.split("|epoch: -1| metrics for ")[1].split(": total")[0]
            if not chiflan.get(test_name):
                chiflan[test_name] = {"cnt": [], "acc": []}
            chiflan[test_name]["cnt"].append(line.split("total ")[1].split(" accuracy")[0])
            chiflan[test_name]["acc"].append(line.split("accuracy = ")[1].split(" %")[0])

for name in chinese:
    print(f"{name}: ")
    sum_chin, sum_chif = 0, 0
    for i in range(8):
        assert chinese[name]["cnt"][i] == chiflan[name]["cnt"][i]
        print(f'{i}: chinese: {chinese[name]["acc"][i]}%    chiflan: {chiflan[name]["acc"][i]}%')
        sum_chin += eval(chinese[name]["acc"][i]) * eval(chinese[name]["cnt"][i])
        sum_chif += eval(chiflan[name]["acc"][i]) * eval(chinese[name]["cnt"][i])
    cnt = sum([eval(cc) for cc in chinese[name]["cnt"]])
    print(f'avg: chinese: {sum_chin/cnt}    chiflan: {sum_chif/cnt}')
