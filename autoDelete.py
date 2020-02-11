import os
import time
import shutil

# 脚本目的：自动删除指定文件夹下的相关文件夹 如批量删除node_modules依赖

def format(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))

def get_dirsize(dirPath):
   size = 0
   for root, dirs, files in os.walk(dirPath):
      size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
   return size / (1024*1024)


def auto_delete(file_dir,target,days):
    sum_size = 0
    for root, dirs, files in os.walk(file_dir):
        for dir in dirs:
            # 获取所有的目录
            if dir == target:
                abs_dir = os.path.join(root,dir)
                diff_time = (time.time() - os.path.getmtime(abs_dir))/60/60/24
                size = get_dirsize(abs_dir)
                if diff_time > days:
                    shutil.rmtree(abs_dir)
                    print("已经删除：%s"%(abs_dir))
                    print("文件夹大小：%.2fMB"%(size))
                    print("上次更新时间距离现在已经过去%.2f天"%(diff_time))
                    print("--------")
                    sum_size += size
    print("已自动删除%d天内未更新的%s文件夹，共节省%.2fMB空间"%(days,target,sum_size))

# 输入目录地址
root = os.getcwd()
# 输入文件夹名称
target = "node_modules"
# 最近30天修改过的文件夹 不删除node_modules
days = 0
auto_delete(root,target,days)

