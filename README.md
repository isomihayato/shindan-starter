# あさごはん診断：Flaskはじめてのハンズオン

Pythonの変数と `if` 文を少し知っている、Webアプリは初めての学生向けの90分教材です。
名前と気分を送信すると、おすすめの朝ごはんが表示されるアプリを作ります。

## 準備（授業前）

Python 3.10以上とGitをインストールし、このリポジトリのフォルダをターミナルで開きます。
Windows / PowerShellの場合：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

PowerShellで仮想環境を有効にできない場合は、実行ポリシーを変えず、次で実行できます。

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

ブラウザで http://127.0.0.1:5000 を開きます。終了はターミナルで `Ctrl+C` です。
サーバーを動かすターミナルとGit操作のターミナルを分けると便利です。
HTMLの変更後は保存してブラウザを再読み込みします。

## 章とブランチ

**`chapterN` は第N章の開始状態（前章までの完成版）です。**
自分のコードで進める人は、章が変わってもブランチを切り替える必要はありません。
第1章は完成版の体験なので、`chapter1` と `chapter2` のアプリコードは同じです。

| 章 | 時間 | 内容 | 開始ブランチ |
| --- | --- | --- | --- |
| 1 | 0〜10分 | 完成版を体験する | `chapter1` |
| 2 | 10〜25分 | 画面の文章を変える | `chapter2` |
| 3 | 25〜40分 | Pythonの値を画面に表示する | `chapter3` |
| 4 | 40〜60分 | フォームの回答を受け取る | `chapter4` |
| 5 | 60〜75分 | 気分によって結果を変える | `chapter5` |
| 6 | 75〜90分 | アレンジして友達と遊ぶ | `chapter6` |

`completed` は第6章のアレンジ例を含む完成版です。
第N章の基本課題の答えは次の章のブランチにあります。

## 途中から合流する方法

まずサーバーを `Ctrl+C` で止めます。以下は第3章から再開する例です。

```powershell
git status
git stash push -u -m "第2章までの自分の作業"
git switch chapter3
python app.py
```

`stash` は未コミットの変更と新しいファイルを一時保存します。
`.venv` などGitの管理対象外のものはそのまま残ります。
変更がない場合の `No local changes to save` は正常です。
**保存した変更は、合流先には戻さず、その章の開始状態から学習を再開します。**
合流後は、このブランチの `CHAPTER.md` を開き、指示された文章を1つ変更して動くか確認します。

保存した作業の確認：

```powershell
git stash list
git stash show -p 'stash@{0}'
```

自分の元のブランチへ戻って再開したい場合は、現在の変更も先に保存してから元のブランチへ戻り、
`git stash list` で該当する項目を確認して `git stash apply 'stash@{番号}'` を実行します。
`番号` は確認した数値に置き換えます。上書きの競合が出たら講師と一緒に確認します。

## 正解を切り替えずに見る

```powershell
git show chapter4:app.py
git diff chapter3 chapter4 -- app.py templates/form.html
```

この例は第3章で加える変更です。教材ファイルの差分を除いてコードを比較できます。

## 仕組みとファイル

- `app.py`：URLに応じてPythonを動かし、HTMLを返す。
- `templates/form.html`：最初の画面。第4章で回答フォームになる。
- `templates/result.html`：第4章以降で使う、配布済みの結果画面。
- `static/style.css`：色や余白など見た目の指定。
- `CHAPTER.md`：現在の章の課題。

ブラウザ → HTTPリクエスト → Flask → Python → HTML → ブラウザ、の順に処理が進みます。
GETは画面を開くとき、POSTはフォームの回答を送るときに使います。
CSSは完成済みの土台として配布します。第6章で自由に編集できます。

## 困ったとき

- `ModuleNotFoundError: flask`：起動と同じPythonで `python -m pip install -r requirements.txt` を実行。
- `TemplateNotFound`：`templates` のつづりと、その中のHTMLファイル名を確認。
- 変更が見えない：保存・ブラウザの再読み込み・起動したフォルダを確認。
- 起動時にポート使用中：別のターミナルで起動済みのアプリを `Ctrl+C` で止める。
- 第4章まで気分で結果が変わらない：想定どおりです。第5章で分岐を実装します。

## 講師用の進行

授業前に全員が初期画面を表示できるか確認します。
冒頭の完成版デモは `completed` で行い、停止後 `chapter1` に戻します。
各章の終了時に課題の確認を行い、合流する人だけ次章へ切り替えます。
追加課題の変更は後の章の動作確認も行ってください。
全員が切り替えた場合も、その章で学んだ箇所を1つ変更する時間を取ります。
学生への配布前に、作成した全ブランチを共有先リポジトリへpushしてください。
初回clone後にローカルにない章へ移る場合も、通常は `git switch chapter3` で
同名の `origin/chapter3` を追跡するローカルブランチが作られます。
