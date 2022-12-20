import json

#pk = int(input())
#skill_name = input()
def load_candidates():
    #загрузит данные из файла
    with open('a.json', 'r', encoding='utf-8') as dat:
        data = json.load(dat)
    return data


def get_all():
    #покажет всех кандидатов
    for candidat in load_candidates():
        return candidat['name']




def get_by_pk(pk):
    #вернет кандидата по pk
    for candidat in load_candidates():
        if candidat['pk'] == int(pk):
            return candidat



def get_by_skill(skill_name):
    #вернет кандидатов по навыку
    candidats_with_skill = []
    for candidat in load_candidates():
        if candidat['skills'].lower().find(skill_name.lower()) >= 0 :
            candidats_with_skill.append(candidat)
    return candidats_with_skill


