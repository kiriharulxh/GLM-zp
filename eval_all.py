import os
from rouge import Rouge

rr = Rouge()
for name in os.listdir():
    if name.endswith('.hyps') and name.startswith('dev'):
        with open(name, 'r') as f:
            lsf = f.readlines()
        with open('cgd.ref', 'r') as g:
            lsg = g.readlines()
        scores = rr.get_scores(lsf, lsg, avg=True)
        print(f'{name.split(".")[0]}: {str(scores)}')

