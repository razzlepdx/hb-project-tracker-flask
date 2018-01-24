"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student-add-form")
def get_student_add_form():
    """ Show form to add a new student to database. """

    return render_template("new_student_form.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """ Add a student. """

    first = request.form.get("fname")
    last = request.form.get("lname")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    html = render_template("student_add_confirmation.html",
                           first=first,
                           last=last,
                           github=github)
    return html


@app.route("/student-search")
def get_student_form():
    """ Show form to search for a student. """

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    projects = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           github=github,
                           first=first,
                           last=last,
                           projects=projects)
    return html


@app.route("/project")
def get_project_info():
    """"""
    pass

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
