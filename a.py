from flask import Flask
from main import load_candidates
from main import get_by_pk
from main import get_by_skill
app = Flask(__name__)
@app.route("/")
def page_index():
    s = ''
    for candidat in load_candidates():
        s += Get_code_of_candidat(candidat)
    return s

@app.route("/candidates/<pk>")
def page_candidat(pk):
    candidat = get_by_pk(pk)
    s = ''
    s += Get_code_of_candidat(candidat)
    return s

@app.route("/skills/<skill_name>")
def page_skills(skill_name):
    s = ''
    for candidat in get_by_skill(skill_name):
        s += Get_code_of_candidat(candidat)
    return s

def Get_code_of_candidat(candidat):
    return f'''
    <img src="{candidat['picture']}" >
    <pre>
  Имя кандидата - <a href="/candidates/{candidat['pk']}">{candidat['name']}</a>
  Позиция кандидата - {candidat['position']}
  Навыки через запятую - {candidat['skills']}

</pre>'''

app.run()