from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("base_page/landing_page.html")


@app.route("/plan_parsing")
def plan_parsing():
    return render_template("plan_parsing/plan_parsing.html")
app.run(debug=True, port=5005)
