DATA_ROOT=/root/data
CHECKPOINT_PATH="/share/lxh"
DATESTR=$(date +"%m-%d-%H-%M")

source $1    # Model
source $2    # Task

NUM_WORKERS=1
NUM_GPUS_PER_WORKER=1
HOST_FILE_PATH="./hostfile"
MP_SIZE=1
MASTER_PORT=$(shuf -n 1 -i 10000-65535)

OPTIONS_NCCL="NCCL_DEBUG=info NCCL_IB_DISABLE=0 NCCL_NET_GDR_LEVEL=2"
DISTRIBUTED_ARGS="${OPTIONS_NCCL} deepspeed --include="localhost:1" --master_port ${MASTER_PORT} --num_nodes ${NUM_WORKERS} --num_gpus ${NUM_GPUS_PER_WORKER}"

EXPERIMENT_NAME=${EXPERIMENT_NAME}_${DATESTR}
mkdir logs
run_cmd="${DISTRIBUTED_ARGS} finetune_glm.py \
       --deepspeed \
       --deepspeed_config config_tasks/config_blocklm_10B_cnndm.json \
       --finetune \
       --task ${TASK_NAME} \
       --data-dir ${DATA_PATH} \
       --checkpoint-activations \
       --num-workers 1 \
       --no-load-optim \
       --no-load-lr-scheduler \
       $MODEL_ARGS \
       $TRAIN_ARGS \
       $COMMON_ARGS \
       $TASK_ARGS \
       --fp16 \
       --model-parallel-size ${MP_SIZE} \
       --epochs 0 \
       --eval-valid \
       --eval-batch-size 4 \
       --overwrite \
       2>&1"

echo ${run_cmd}
eval ${run_cmd}
