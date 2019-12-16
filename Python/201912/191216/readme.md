### 企画概要
* 「ファイル整理ツール」<br>
フォルダ内の各ファイルを拡張子で種類分けし、同じディレクトリ内に抽出したファイルを格納するフォルダを作成してまとめる。

### 仕様
* メニューからディレクトリの指定、リロード、実行、ファイルの種類選択、終了が可能。
* ファイルの種類はテキスト、エクセル、スライド、画像、音、動画、圧縮、プログラムで大別し、選択が可能。<br>
FILE_TYPES= ['text', 'excel', 'slide', 'image', 'music', 'movie', 'compress', 'program']
* 大別した種類ごとに拡張子を登録しており、拡張子毎に選択が可能。<br>
TEXT_TYPES= ['doc', 'docx', 'odt', 'rtf', 'pdf', 'txt']<br>
EXCEL_TYPES= ['xlsx', 'csv', 'tsv', 'xls']<br>
SLIDE_TYPES= ['pptx', 'ppt', 'odp']<br>
IMAGE_TYPES = ['gif', 'png', 'bmp', 'jpeg', 'jpg', 'tga', 'tif', 'ppm']<br>
MUSIC_TYPES = ['mp3', 'wav', 'wma', 'asf', 'aac', 'flac', 'm4a']<br>
MOVIE_TYPES = ['mp4', 'mpg', 'mpeg', 'wmv', 'avi', 'mkv']<br>
COMPRESS_TYPES = ['zip', 'lzh', '7z', 'cab', 'tar', 'rar']<br>
PROGRAM_TYPES = ['c', 'cpp', 'h', 'cs', 'py', 'js', 'bat', 'php', 'java']
* メニューのHelpまたはiボタンからツールの使い方を確認することが可能。
* エントリーウィジェットからディレクトリの指定、拡張子検索、フォルダ名の入力が可能。
* ディレクトリの指定はファイルダイアログ、使い方や実行確認はメッセージボックスを使用。
* ディレクトリを指定すると、対象のディレクトリを別ウィンドウで表示。
* チェックした種類のファイルをスクロールリストボックスウィジェットでファイル名を一覧表示。
* 一覧のファイルは拡張子を選択チェックし、ReLoadすることで更新可能。
* 一覧の中からマウス左クリックでファイル選択を行い、選択状態で右クリックまたはPickUpボタンでPickUpリストに入れることが可能。
* ExecutionボタンでPickUpリスト内のファイルを入力したフォルダ名内に格納してまとめる。<br>
その際に確認ダイアログを表示して実行確認を行う。<br>
フォルダ名が未入力では、Executionボタンを押しても警告ダイアログを表示して実行できない。
* 拡張子検索は正規表現で行う。

### 使用ライブラリフレームワーク
1. re
1. os
1. subprocess
1. tkinter
1. PyInstaller

### 進捗
* 完成→実行ファイル「organizefiles.exe」
* 添付ファイル「organizefiles.py」参照