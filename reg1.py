import random
import shelve

def main(vk, peer_id):
    
    _id = str(peer_id)
    message = '⚠ Регистрация. Выберите ваше отделение'
    vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/branch.json", "r", encoding="UTF-8").read())
    
    with open("profiles/num_users.txt", "r", encoding='utf-8') as f:
        num_users_data = f.readlines()
    num_users = str(num_users_data[0]).replace("\n","")
    
    with shelve.open('profiles/1_id/id_data') as shlv:
        shlv[_id] = num_users
    with shelve.open('profiles/2_branch/branch_data') as shlv:
        shlv[_id] = 'null'
    with shelve.open('profiles/3_course/course_data') as shlv:
        shlv[_id] = 'null'
    with shelve.open('profiles/4_group/group_data') as shlv:
        shlv[_id] = 'null'
    with shelve.open('profiles/5_notify/notify_data') as shlv:
        shlv[_id] = 'off'
        
    with open("profiles/num_users.txt", 'w', encoding='utf-8') as file:
        print(str(int(num_users) + 1).replace("\n",""), file=file)