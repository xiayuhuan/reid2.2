python demo.py --query_index 600

python demo1.py --query_index 2
['c5s2_118574_05', 'c5s1_001526_02', 'c6s1_014626_03', 'c1s1_002401_02', 'c5s3_034190_01', 'c6s2_112243_04', 'c5s1_009476_01', 'c6s1_014651_03']
所查询图片2中行人出现的信息：
1位置：摄像头c5, 时间：11:19:03
2位置：摄像头c5, 时间：10:01:01
3位置：摄像头c6, 时间：10:09:45
4位置：摄像头c1, 时间：10:01:36
5位置：摄像头c5, 时间：10:22:47
6位置：摄像头c6, 时间：11:14:49
7位置：摄像头c5, 时间：10:06:19
8位置：摄像头c6, 时间：10:09:46


所查询图片2中行人出现的信息：
1位置：摄像头c5小区E, 时间：11:19:03
2位置：摄像头c5小区E, 时间：10:01:01
3位置：摄像头c6小区F, 时间：10:09:45
4位置：摄像头c1小区A, 时间：10:01:36
5位置：摄像头c5小区E, 时间：10:22:47
6位置：摄像头c6小区F, 时间：11:14:49
7位置：摄像头c5小区E, 时间：10:06:19
8位置：摄像头c6小区F, 时间：10:09:46

1.pip install -r requirements.txt
2.python prepare.py
3.python train.py --gpu_ids 0 --name ft_ResNet501 --train_all --batchsize 32  --data_dir ./Market/pytorch/
4.python test.py --gpu_ids 0 --name ft_ResNet501 --test_dir ./Market/pytorch/  --batchsize 32 --which_epoch 59
5.python demo1.py --query_index 2
