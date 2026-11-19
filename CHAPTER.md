# あさごはん診断：全章まとめ

第1章から第6章までの課題・確認ポイント・追加課題をまとめています。
このファイルは `completed` ブランチにあります。
**各 `chapterN` ブランチは第N章の開始状態（前章までの完成版）です。**
自分のコードで進める人は、そのまま次の章へ進めます。
環境準備と作業を退避してブランチを切り替える手順は `README.md` を参照してください。

## 目次

- [第1章：完成版を体験する（0〜10分）](#chapter1)
- [第2章：画面の文章を変える（10〜25分）](#chapter2)
- [第3章：Pythonの値を画面に表示する（25〜40分）](#chapter3)
- [第4章：フォームの回答を受け取る（40〜60分）](#chapter4)
- [第5章：気分によって結果を変える（60〜75分）](#chapter5)
- [第6章：アレンジして友達と遊ぶ（75〜90分）](#chapter6)

<a id="chapter1"></a>

## 第1章：完成版を体験する

時間：0〜10分。開始ブランチ：`chapter1`（この章の開始状態）。

1. 講師が `completed` を起動して、名前と気分を入力します。
2. 気分を変えると結果も変わることを確かめます。
3. 今日作る流れを確認します：ブラウザ → Flask → Python → HTML。
4. 自分のPCで `python app.py` を実行し、初期画面を開きます。

この章ではコードを変更しません。次は第2章へ進みます。

この章の基本課題の完成版は `chapter2` です。

<a id="chapter2"></a>

## 第2章：画面の文章を変える

時間：10〜25分。開始ブランチ：`chapter2`（この章の開始状態）。

1. `templates/form.html` の見出し `<h1>` と説明文 `<p class="lead">` を探します。
2. 説明文を「朝ごはんで、今日を楽しく始めよう！」に変更します。
3. 保存し、ブラウザを再読み込みします。

確認：自分で変更した文章が出れば成功です。
追加課題：見出しも好きな文章に変更しましょう。

この章の基本課題の完成版は `chapter3` です。

<a id="chapter3"></a>

## 第3章：Pythonの値を画面に表示する

時間：25〜40分。開始ブランチ：`chapter3`（この章の開始状態）。

1. `app.py` の `home()` に `name = "ひなた"` を追加します。
2. 戻り値を `return render_template("form.html", name=name)` に変えます。
3. `templates/form.html` のカード内を `<p>{{ name }}さん、ようこそ！あさごはん診断へ。</p>` に変えます。
4. Pythonの名前を変えて画面を確認します。

確認：Pythonの変数がHTMLの `{{ name }}` に渡る流れを説明しましょう。
追加課題：好きな食べ物もPythonから渡して表示しましょう。

この章の基本課題の完成版は `chapter4` です。

<a id="chapter4"></a>

## 第4章：フォームの回答を受け取る

時間：40〜60分。開始ブランチ：`chapter4`（この章の開始状態）。

1. 下のフォームで `templates/form.html` の `<div class="card">...</div>` を置き換えます。
2. `app.py` を下のコードに変更します。`request` とPOST用ルートが増え、`home()` は名前を渡さない形に戻ります。
3. HTMLの `name` 属性と `request.form` のキーが対応することを確認します。
4. 名前と気分を入力して診断します。結果画面のHTMLは配布済みです。

この章では気分に関係なく同じメニューです。第5章で分岐します。
確認：入力した名前が結果に出て、リンクで最初の画面に戻れること。
追加課題：名前の入力例（placeholder）を変更しましょう。

### フォーム

```html
<form class="card" method="post" action="{{ url_for('diagnose') }}">
      <label class="q">
        <span class="qtitle">Q1. なまえを教えてください</span>
        <input type="text" name="name" placeholder="ひなた" required>
      </label>
      <fieldset class="q">
        <legend class="qtitle">Q2. いまのきぶんは？</legend>
        <div class="pills">
          <label><input type="radio" name="mood" value="wakuwaku" checked><span>わくわく</span></label>
          <label><input type="radio" name="mood" value="shaki"><span>しゃきっと</span></label>
          <label><input type="radio" name="mood" value="nonbiri"><span>のんびり</span></label>
        </div>
      </fieldset>
      <button type="submit">診断する</button>
    </form>
```

### app.py の完成例

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/diagnose", methods=["POST"])
def diagnose():
    name = request.form.get("name", "").strip() or "ゲスト"
    mood = request.form.get("mood", "wakuwaku")
    menu = {
        "name": "パンケーキ",
        "color": "pink",
        "desc": "ふんわり甘い朝ごはんで、一日を楽しく始めよう！",
    }
    return render_template("result.html", name=name, menu=menu)


if __name__ == "__main__":
    app.run(debug=True)

```

この章の基本課題の完成版は `chapter5` です。

<a id="chapter5"></a>

## 第5章：気分によって結果を変える

時間：60〜75分。開始ブランチ：`chapter5`（この章の開始状態）。

1. `diagnose()` 内の固定の `menu` を `if` / `elif` / `else` に置き換えます。
2. `mood == "shaki"` なら「おにぎり」、色は `green`。
3. `mood == "nonbiri"` なら「おかゆ」、色は `blue`。
4. それ以外は「パンケーキ」、色は `pink`。
5. それぞれの `menu` に `name`（メニュー名）、`color`（色）、`desc`（説明文）を用意します。

フォームの `value` とPythonで比較する文字列を同じにしましょう。
確認：3つの気分すべてで違う結果が出ること。
追加課題：結果の説明文を自分らしく変更しましょう。

この章の基本課題の完成版は `chapter6` です。

<a id="chapter6"></a>

## 第6章：アレンジして友達と遊ぶ

時間：75〜90分。開始ブランチ：`chapter6`（この章の開始状態）。

1. 質問、メニュー名、結果の説明、CSSの色を自由に変えます。
2. 同じPCで友達と交代して診断します。
3. どの回答がどの結果になるか、友達に説明します。

確認：改造後も3つの気分すべてで動くこと。
追加課題：気分を1つ増やし、HTMLの選択肢とPythonの条件の両方を変更しましょう。
完成例は `completed` にあります。アレンジに唯一の正解はありません。

## 完成例の確認

`completed` では、名前と気分から3種類の朝ごはんを提案します。
第6章のアレンジ例として、見出しの補足とパンケーキの名前・説明を変更しています。
3つの選択肢をすべて試し、リンクで最初の画面に戻れることを確認しましょう。
