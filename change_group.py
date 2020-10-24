import random
import shelve

def main(vk, peer_id):
    
    _id = str(peer_id)
    message = '✏ Выберите ваше отделение'
    
    with shelve.open('profiles/2_branch/branch_data') as shlv:
        shlv[_id] = 'null'
    with shelve.open('profiles/3_course/course_data') as shlv:
        shlv[_id] = 'null'
    with shelve.open('profiles/4_group/group_data') as shlv:
        shlv[_id] = 'null'
    with shelve.open('profiles/5_notify/notify_data') as shlv:
        shlv[_id] = 'off'
        
    vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/branch.json", "r", encoding="UTF-8").read())