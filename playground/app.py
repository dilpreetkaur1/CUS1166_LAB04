from flask import Flask, render_template

app = Flask(__name__)

class_roster = [("Grace", "F", "Senior"),
                ("John", "B", "Senior"),
                ("Cindy", "C", "Junior"),
                ("Sarah", "A", "Senior"),
                ("Brianna", "A", "Freshman"),
                ("Chelsea", "B", "Sophomore"),
                ("Tommy", "D", "Senior"),
                ("Toby", 'A', "Freshman"),
                ("Tina", "B", "Senior")]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)


@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == '__main__':
    app.run()
