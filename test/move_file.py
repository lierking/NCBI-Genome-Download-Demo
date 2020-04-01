import shutil
import os

path = input()
copy_path = input()
os.makedirs(copy_path, exist_ok=True) if copy_path != path else print('不能原地移动')

for i in range(1, 48):
    for dirpath, dirnames, filenames in os.walk(path + f'{i}pd/'):
        for file in filenames:
            if 'fan' not in path + f'{i}pd/' + file:
                try:
                    shutil.copytree(f'{path}{i}pd/', f'{copy_path}{i}pd/')  # 移动目录
                    shutil.copy(path+f'{i}pd/'+file, copy_path+f'{i}pd/'+file)  # 移动文件
                except:
                    pass
