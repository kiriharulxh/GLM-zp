DATESTR=$(date +"%m-%d-%H-%M")

nohup bash scripts/evaluate_chiflan-heldout-0.sh config_tasks/model_blocklm_10B_chinese.sh &> eval/heldout0-${DATESTR}-chinese.txt &
nohup bash scripts/evaluate_chiflan-heldout-1.sh config_tasks/model_blocklm_10B_chinese.sh &> eval/heldout1-${DATESTR}-chinese.txt &
nohup bash scripts/evaluate_chiflan-heldout-2.sh config_tasks/model_blocklm_10B_chinese.sh &> eval/heldout2-${DATESTR}-chinese.txt &
nohup bash scripts/evaluate_chiflan-heldout-3.sh config_tasks/model_blocklm_10B_chinese.sh &> eval/heldout3-${DATESTR}-chinese.txt &
nohup bash scripts/evaluate_chiflan-heldout-4.sh config_tasks/model_blocklm_10B_chinese.sh &> eval/heldout4-${DATESTR}-chinese.txt &
nohup bash scripts/evaluate_chiflan-heldout-5.sh config_tasks/model_blocklm_10B_chinese.sh &> eval/heldout5-${DATESTR}-chinese.txt &
nohup bash scripts/evaluate_chiflan-heldout-6.sh config_tasks/model_blocklm_10B_chinese.sh &> eval/heldout6-${DATESTR}-chinese.txt &
nohup bash scripts/evaluate_chiflan-heldout-7.sh config_tasks/model_blocklm_10B_chinese.sh &> eval/heldout7-${DATESTR}-chinese.txt &

