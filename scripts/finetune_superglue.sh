DATA_ROOT=/dataset/fd5061f6/english_data/superglue
source config_tasks/model_blocklm_roberta_1.25.sh
source $1

CHECKPOINT_PATH="/dataset/fd5061f6/english_data/finetune_checkpoints"

MASTER_PORT=$(shuf -n 1 -i 10000-65535)
DISTRIBUTED_ARGS="--nproc_per_node 2 --nnodes 1 --node_rank 0 --master_addr localhost --master_port $MASTER_PORT"
DATESTR=$(date +"%m-%d-%H-%M")

mkdir logs
python -m torch.distributed.launch $DISTRIBUTED_ARGS finetune_gpt2.py \
       --finetune \
       --experiment-name ${EXPERIMENT_NAME} \
       --task ${TASK_NAME} \
       --data-dir ${DATA_PATH} \
       --save ${CHECKPOINT_PATH} \
       --seq-length ${MAX_SEQ_LEN} \
       --checkpoint-activations \
       --batch-size 8 \
       --eval-batch-size 16 \
       --save-epoch 5 \
       $MODEL_ARGS \
       $TRAIN_ARGS \
       $COMMON_ARGS \
       --epochs ${EPOCH_SINGLE} \
       --lr ${LR_SINGLE} \
       --overwrite \
       2>&1 | tee logs/log-${EXPERIMENT_NAME}.txt
