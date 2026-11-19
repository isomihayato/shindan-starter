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
