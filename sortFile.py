import os

# 文件目的：指定文件夹下，将文件按照文件容量降序排序，方便删除。

def dictionairy(key_value):
    new_kv = sorted(key_value.items(), key = lambda kv:(kv[1], kv[0]))
    for key in new_kv:
        print("文件名称：%s \r"%(key[0]))
        print("文件大小：%.2f MB"%(key[1]))
        print("--------------")

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024 * 1024)
    return round(fsize, 2)

def sort_file(file_dir):
    name_list = []
    size_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
        	name = os.path.join(root,file)
        	size = get_FileSize(name)
        	file_name = name.replace(file_dir,"")
        	name_list.append(file_name)
        	size_list.append(size)
        	
    obj = dict(zip(name_list,size_list))
    dictionairy(obj)

# 输入目录地址
root = os.getcwd()
sort_file(root)

