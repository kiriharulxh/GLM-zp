DATESTR=$(date +"%m-%d-%H-%M")

nohup bash scripts/evaluate_chiflan-heldout-0.sh config_tasks/model_blocklm_10B_chiflan.sh &> eval/heldout0-${DATESTR}-chiflan.txt &
nohup bash scripts/evaluate_chiflan-heldout-1.sh config_tasks/model_blocklm_10B_chiflan.sh &> eval/heldout1-${DATESTR}-chiflan.txt &
nohup bash scripts/evaluate_chiflan-heldout-2.sh config_tasks/model_blocklm_10B_chiflan.sh &> eval/heldout2-${DATESTR}-chiflan.txt &
nohup bash scripts/evaluate_chiflan-heldout-3.sh config_tasks/model_blocklm_10B_chiflan.sh &> eval/heldout3-${DATESTR}-chiflan.txt &
nohup bash scripts/evaluate_chiflan-heldout-4.sh config_tasks/model_blocklm_10B_chiflan.sh &> eval/heldout4-${DATESTR}-chiflan.txt &
nohup bash scripts/evaluate_chiflan-heldout-5.sh config_tasks/model_blocklm_10B_chiflan.sh &> eval/heldout5-${DATESTR}-chiflan.txt &
nohup bash scripts/evaluate_chiflan-heldout-6.sh config_tasks/model_blocklm_10B_chiflan.sh &> eval/heldout6-${DATESTR}-chiflan.txt &
nohup bash scripts/evaluate_chiflan-heldout-7.sh config_tasks/model_blocklm_10B_chiflan.sh &> eval/heldout7-${DATESTR}-chiflan.txt &

