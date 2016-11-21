# -*- coding: utf-8 -*-

import os
import hashlib
import time

path = r".\file"
file_type = r".jpg"
i = 0
d = 0
w = 0


def GetMd5(file_name):
    m = hashlib.md5()
    n = 1024 * 8
    inp = open(file_name, 'rb')
    while True:
        buf = inp.read(n)
        if buf:
            m.update(buf)
        else:
            break
    return m.hexdigest()


def Change_File_name(i, d, w):
    s = time.time()
    for file_path in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_path)):
            new_name = GetMd5(os.path.join(path, file_path))
            if not os.path.exists(os.path.join(path, new_name + file_type)):
                i += 1
                os.rename(os.path.join(path, file_path), os.path.join(path, new_name + file_type))
                print("重命名文件%s为%s" % (file_path, new_name + file_type))
            elif new_name + file_type == file_path:
                w += 1
                print("跳过文件:%s" % file_path)
                continue
            else:
                d += 1
                print '文件已经存在，删除重复文件%s' % file_path
                os.remove(path + "\\" + file_path)
    e = time.time()
    print("-------------------------------------------------------------------------------")
    print("操作内容： 重命名文件：%s 个， 删除文件：%s 个, 未改变文件：%s 个, 耗时： %s 秒" % (i, d, w, e-s))
    print("-------------------------------------------------------------------------------")


if __name__ == "__main__":
    Change_File_name(i, d, w)
