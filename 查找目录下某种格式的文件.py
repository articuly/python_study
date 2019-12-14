# coding:utf-8
import os


# 接受输入
def main():
    user_input = input('请输入路径、文件扩展名（和目标路经）：')
    args = user_input.strip().split(' ')
    if len(args) > 1:
        path = args[0]
        ext_name = args[1]
    if len(args) > 2:
        target_path = args[2]

    # 遍历文件
    for _dir, subdirs, files in os.walk(path):
        for file in files:
            # 列出符合扩展名的文件
            if len(args) == 2:
                if os.path.splitext(file)[1] == ext_name:
                    print(os.path.join(_dir, file))
            # 拷贝文件到另外目录
            if len(args) == 3 and os.path.splitext(file)[1] == ext_name:
                if not os.path.exists(target_path):
                    os.mkdir(target_path)
                print(os.path.join(_dir, file))
                os.system("copy {0} {1}".format(os.path.join(_dir, file), target_path))


while True:
    main()
