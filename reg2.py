import random
import shelve

def main(vk, peer_id, text):
    
    _id = str(peer_id)
    branches = ['оуит']
    
    if text in branches:
        with shelve.open('profiles/2_branch/branch_data') as shlv:
            shlv[_id] = text.upper()
        message = '☑ Выберите ваш курс'
        vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/course.json", "r", encoding="UTF-8").read())
    
    else:
        message = '💡 Ошибка. Отделение не найдено.\nВоспользуйтесь кнопками ниже'
        vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/branch.json", "r", encoding="UTF-8").read())