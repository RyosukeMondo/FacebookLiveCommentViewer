# FacebookLiveCommentViewer

Chromeで表示中のFacebook Liveのコメントを集めて、setting.iniで指定したパスに保存するプログラムです。

## 使い方

### 必要なソフト
Chrome

### インストール方法

以下よりダウンロードし解凍する。

Windows版
https://github.com/RyosukeMondo/FacebookLiveCommentViewer/releases/download/v1.0/facebookAutomation-v1.0.zip

MacOS版
https://github.com/RyosukeMondo/FacebookLiveCommentViewer/releases/download/v1.0/facebookAutomation-v1.0macOs.zip

### 設定

setting.ini を開き、任意のパスに書き換える

[DEFAULT]
dst = C:\nico\comment.xml

### 初回起動時

facebookAutomation.exeを実行する
Chromeが起動し、Facebookのログイン画面が表示されるのでログインする。ログインができたら一度すべて閉じる。
次回以降、facebookにログインした状態になれば成功。

### 二回目以降

以下のような、Facebook LiveのURLをコピー（クリップボードに保持）

https://www.facebook.com/{userName}/videos/{ID}

facebookAutomation.exeを起動する。
設定ファイルで指定したパスに、毎秒ファイルが書き込まれる。

あとは、NiCommentGeneratorのような、comments.xmlをhtmlに表示するようなプログラムから読み込む。
https://github.com/totoraj930/NiCommentGenerator


