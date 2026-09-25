from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/upi")
@app.route("/upi.html")
def upi():
    return render_template("upi.html")


@app.route("/qr")
@app.route("/qr.html")
def qr():
    return render_template("qr.html")


@app.route("/apps")
@app.route("/apps.html")
def apps():
    return render_template("apps.html")


@app.route("/benefits")
@app.route("/benefits.html")
def benefits():
    return render_template("benefits.html")


@app.route("/guide")
@app.route("/guide.html")
def guide():
    return render_template("guide.html")


@app.route("/safety")
@app.route("/safety.html")
def safety():
    return render_template("safety.html")


@app.route("/quiz", methods=["GET", "POST"])
@app.route("/quiz.html", methods=["GET", "POST"])
def quiz():

    score = None

    if request.method == "POST":

        answers = {
            "q1": "correct",
            "q2": "correct",
            "q3": "correct",
            "q4": "correct",
            "q5": "correct"
        }

        score = 0

        for question, correct_answer in answers.items():

            user_answer = request.form.get(question)

            if user_answer == correct_answer:
                score += 1

    return render_template("quiz.html", score=score)


if __name__ == "__main__":
    app.run(debug=True)