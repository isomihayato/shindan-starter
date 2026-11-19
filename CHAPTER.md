# 第3章：Pythonの値を画面に表示する

時間：25〜40分。現在のブランチは `chapter3`、この章の開始状態です。

1. `app.py` の `home()` に `name = "ひなた"` を追加します。
2. 戻り値を `return render_template("form.html", name=name)` に変えます。
3. `templates/form.html` のカード内を `<p>{{ name }}さん、ようこそ！あさごはん診断へ。</p>` に変えます。
4. Pythonの名前を変えて画面を確認します。

確認：Pythonの変数がHTMLの `{{ name }}` に渡る流れを説明しましょう。
追加課題：好きな食べ物もPythonから渡して表示しましょう。

この章の基本課題の完成版は `chapter4` です。
