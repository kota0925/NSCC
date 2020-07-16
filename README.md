# NSCC

nitendo switch caputure copyの略です。適当に名前つけました。
switchでのクリップ動画、スクリーンショットをすべて同ディレクトリにファイルをコピー保存するプログラム

## 機能&仕様

- クリップ動画、スクリーンショットを選択したディレクトリにファイルのみをすべて保存します。
- CUI操作（GUIverは気が向いたら作るかも）
- switchのキャプチャのディレクトリパスは`F:\Nintendo\Album\~`になってます。
- 保存先のパスの入力は絶対パス推奨。
- 実行速度はかなり遅いです。（気が向けば改善させようと思います。）

## exe化したい人

各自でexe化してください。一応手順は以下に記載しておきます。(mac, linuxは知りません。)

1. pyinstallerがない人はインストールしてください。(pip, pythonとかがない人は各自その辺はぐぐってください。)

```
pip install pyinstaller
```

2. NSCCのディレクトリ内で以下のコマンドをたたいてください。

```
pyinstaller python main.py -onefile
```

これでexe化ができると思います。

## その他
- 開発言語　python3

