import os
import sys
import glob

def check_dir(dir):
    if not os.path.exists(dir):
        print("ディレクトリが存在しません。終了するにはなにかキーを入力してください。")
        input()
        sys.exit()
    print('ディレクトリの存在を確認しました。')


print("switchのディレクトリを確認します。。。")
dir = "F:\\Nintendo\\Album"
check_dir(dir)

print("保存先のディレクトリを入力してください。")
save_dir = input()
check_dir(save_dir)
