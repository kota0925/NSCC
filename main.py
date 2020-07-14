import os
import sys
import glob
import shutil
import re

def check_dir(dir):
    if not os.path.isdir(dir):
        print("ディレクトリが存在しません。終了するにはなにかキーを入力してください。")
        input()
        sys.exit()
    print('ディレクトリの存在を確認しました。')

print("switchのディレクトリを確認します。。。")
switch_dir = "F:\\Nintendo\\Album"
check_dir(switch_dir)

print("保存先のディレクトリを入力してください。")
save_dir = input()
#save_dir = re.sub('¥"', '', save_dir)
check_dir(save_dir)

files = glob.glob(switch_dir + '*\\*\\*\\*')
for file in files:
    if not shutil.copy(file, save_dir):
        print("ファイルのコピーに失敗しました。")
        print("ファイル名：" + file)
        print("終了するにはなにかキーを入力してください。")
        input()
        sys.exit()

print("完了しました。終了するにはなにかキーを入力してください。")
input()
sys.exit()