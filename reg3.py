import random
import shelve

def main(vk, peer_id, text):
    
    _id = str(peer_id)
    courses = ['1 курс', '2 курс', '3 курс', '4 курс']
    
    if text in courses:
        with shelve.open('profiles/3_course/course_data') as shlv:
            shlv[_id] = text
        with shelve.open('profiles/3_course/course_data') as shlv:
            course = shlv[_id]
        message = '☑ Выберите вашу группу'
        vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/group."+course+".json", "r", encoding="UTF-8").read())
    
    else:
        message = '💡 Ошибка. Курс не найден.\nВоспользуйтесь кнопками ниже'
        vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/course.json", "r", encoding="UTF-8").read())