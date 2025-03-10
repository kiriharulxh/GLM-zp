MODEL_TYPE="GLM-10B-chinese"
MODEL_ARGS="--block-lm \
            --cloze-eval \
            --task-mask \
            --num-layers 48 \
            --hidden-size 4096 \
            --num-attention-heads 64 \
            --max-position-embeddings 2048 \
            --tokenizer-type ChineseSPTokenizer \
            --load-pretrained ${CHECKPOINT_PATH}/GLM-10B-chinese-customization_07-10-10-45"