# 第4章：フォームの回答を受け取る

時間：40〜60分。現在のブランチは `chapter4`、この章の開始状態です。

1. 下のフォームで `templates/form.html` の `<div class="card">...</div>` を置き換えます。
2. `app.py` を下のコードに変更します。`request` とPOST用ルートが増え、`home()` は名前を渡さない形に戻ります。
3. HTMLの `name` 属性と `request.form` のキーが対応することを確認します。
4. 名前と気分を入力して診断します。結果画面のHTMLは配布済みです。

この章では気分に関係なく同じメニューです。第5章で分岐します。
確認：入力した名前が結果に出て、リンクで最初の画面に戻れること。
追加課題：名前の入力例（placeholder）を変更しましょう。

## フォーム

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

## app.py の完成例

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
