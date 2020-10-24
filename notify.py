import random
import shelve

def main(vk, peer_id):
    
    _id = str(peer_id)
    with shelve.open('profiles/5_notify/notify_data') as shlv:
        notify = shlv[str(peer_id)]

    if notify=='on':
        new_notify='off'
        message='🔇 Вы выключили уведомления'
    else:
        new_notify='on'
        message='🔊 Вы включили уведомления'

    with shelve.open('profiles/5_notify/notify_data') as shlv:
        shlv[_id] = new_notify

    vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/profile.json", "r", encoding="UTF-8").read())