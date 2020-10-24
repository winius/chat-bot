import random
import shelve

def main(vk, peer_id, text, admin_id):
    
    _id = str(peer_id)
    with shelve.open('profiles/3_course/course_data') as shlv:
        course = shlv[_id]
        
    groups = ['20АП1-1','20ИС1-1','20ИС1-3','20ИС-11','20ИС1-2Д','20ИС1-3Д','20СА1-1','20СА1-2Д','20ИНФ1-1','20ИНФ-11','20ПИ1-2Д','20ЗИО1-2Д','20КСК-11',
              '29АП1-1','29АП-11','29ИС1-1','29ИС1-2','29ИС1-2Д','29ИС-11','29СА2-1','29СА1-1Д','29ИНФ2-1','29ИНФ-11','29ПИ2-1Д','29ЗИО1-1','29КСК-11',
              'АП3-1','38АП-11','ИС3-1','ИС3-3','ИС3-1Д','38ИС-11','38ИС-13','СА3-2','ИНФ3-1','3ИНФ-11','ПИ3-2Д','ЗИО3-2Д','38КСК-11',
              'АП4-1','П4-1','П4-3','ПИ4-2Д','СА4-2Д']
    
    if text.upper() in groups:
        with shelve.open('profiles/4_group/group_data') as shlv:
            shlv[_id] = text
        with shelve.open('profiles/5_notify/notify_data') as shlv:
            shlv[_id] = 'on'
        message = '✅ Регистрация завершена'
        vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read())
    
    else:
        message = '💡 Ошибка. Группа не найдена.\nВоспользуйтесь кнопками ниже'
        vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/group."+course+".json", "r", encoding="UTF-8").read())