import random
import shelve

def main(vk, peer_id):
    
    with shelve.open('profiles/2_branch/branch_data') as shlv:
        branch = shlv[str(peer_id)]
    with shelve.open('profiles/3_course/course_data') as shlv:
        course = shlv[str(peer_id)]
    with shelve.open('profiles/4_group/group_data') as shlv:
        group = shlv[str(peer_id)]
    with shelve.open('profiles/5_notify/notify_data') as shlv:
        notify = shlv[str(peer_id)]
    
    if notify=='on':
        noty='🔊 Уведомления включены'
    else:
        noty='🔇 Уведомления выключены'
    
    message = '📋 Профиль\n\n' + branch + ' ' + course + '\nГруппа: ' + group.upper() + '\n\n' + noty
    vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/profile.json", "r", encoding="UTF-8").read())
