import json


def load_candidates():
    # загрузит данные из файла
    with open('a.json', 'r', encoding='utf-8') as dat:
        data = json.load(dat)
        return data


def get_all():
    # покажет всех кандидатов
    for candidat in load_candidates():
        return candidat['name']


def get_by_id(id):
    # вернет кандидата по pk
    for candidat in load_candidates():
        if candidat['id'] == int(id):
            return candidat


def get_by_skill(skill_name):
    # вернет кандидатов по навыку
    candidats_with_skill = []
    for candidat in load_candidates():
        if candidat['skills'].lower().find(skill_name.lower()) >= 0:
            candidats_with_skill.append(candidat)
    return candidats_with_skill


def get_by_name(name):
    # вернет кандидатов по имени
    candidats_with_name = []
    for candidat in load_candidates():
        if candidat['name'].lower().find(name.lower()) >= 0:
            candidats_with_name.append(candidat)
    return candidats_with_name
