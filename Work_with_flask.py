from flask import Flask
from main import load_candidates
from main import get_by_id
from main import get_by_skill
from main import get_by_name

app = Flask(__name__)


@app.route("/")
def page_index():
    s = ''
    for candidat in load_candidates():
        s += Get_code_of_candidat(candidat)
    return s


@app.route("/candidates/<id>")
def page_candidat(id):
    candidat = get_by_id(id)
    s = ''
    s += Get_code_of_candidat(candidat)
    return s


@app.route("/skills/<skill_name>")
def page_skills(skill_name):
    s = ''
    for candidat in get_by_skill(skill_name):
        s += Get_code_of_candidat(candidat)
    return s


@app.route("/search/<name>")
def page_name(name):
    s = ''
    for candidat in get_by_name(name):
        s += Get_code_of_candidat(candidat)
    return s



def Get_code_of_candidat(candidat):
    return f'''
    <img src="{candidat['picture']}" >
    <pre>
    Имя кандидата - <a href="/candidates/{candidat['id']}">{candidat['name']}</a>
    Позиция кандидата - {candidat['position']}
    Навыки через запятую - {candidat['skills']}

    </pre>'''


app.run()
