CUDA_VISIBLE_DEVICES='0' python imagenet_attack.py --data_dir /home/pc/lxn/data/imagenet/train/ --uaps_save ./uaps_save/spgd/ --batch_size 250 --alpha 10 --epoch 20 --spgd 1 --num_images 10000 --model_name vgg16 --Momentum 0 --cross_loss 0