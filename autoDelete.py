import os
import time
import shutil

# 脚本目的：自动删除指定文件夹下的相关文件夹 如批量删除node_modules依赖

def get_dirsize(dirPath):
    size = 0
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            try:
                name = os.path.join(root, file)
                temp = os.path.getsize(name)
                size += temp
            except IOError:
                error = "文件异常"
    return size / (1024*1024)

def auto_delete(file_dir,target,days):
    sum_size = 0
    for root, dirs, files in os.walk(file_dir):
        # 获取所有的目录
        for dir in dirs:
            if dir == target:
                abs_dir = os.path.join(root,dir)
                # 没必要扫子级的node_modules
                if(abs_dir.count(target) > 1):
                    break
                diff_time = (time.time() - os.path.getmtime(abs_dir))/60/60/24
                size = get_dirsize(abs_dir)
                if diff_time > days:
                    # 这行是清空文件夹的代码，建议先运行命令扫一遍，确保扫出来的文件都可以删除后，再取消注释。
                    # shutil.rmtree(abs_dir)
                    print("已经删除：%s"%(abs_dir))
                    print("文件夹大小：%.2fMB"%(size))
                    print("上次更新时间距离现在已经过去%.2f天"%(diff_time))
                    print("--------")
                    sum_size += size

    print("已自动删除%d天内未更新的%s文件夹，共节省%.2fMB空间"%(days,target,sum_size))

# 输入目录地址
root = "/Users/zengzhiqiang/Desktop"
# 输入文件夹名称
target = "node_modules"
# 最近30天修改过的文件夹 不删除node_modules
days = 300
auto_delete(root,target,days)

