import os
import shutil


def main():
    print("搜寻可清理之文件")
    egg_info: list = []
    for file in os.listdir():
        if file.endswith((".egg-info", ".spec")):
            egg_info.append(file)
            print(file)
    pycache: list = []
    for dirpath, dirnames, filenames in os.walk("./"):
        for dirname in dirnames:
            if dirname == "__pycache__":
                pycache.append(fn := os.path.join(dirpath, dirname))
                print(fn)
    print("执行删除操作")
    for file in ["build", "dist", "logs", "log", *egg_info, *pycache]:
        if os.path.isdir(file) and os.access(file, os.W_OK):
            shutil.rmtree(file)
        elif os.path.isfile(file) and os.access(file, os.W_OK):
            os.remove(file)
    print("完成")

if __name__ == "__main__":
    main()
