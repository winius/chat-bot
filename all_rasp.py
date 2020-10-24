import shelve
import random

def main(vk, peer_id):
    sm = '📆'

    with shelve.open('profiles/4_group/group_data') as shlv:
        group = shlv[str(peer_id)]

    url_group = 'groups/' + group + '/all.txt'
    with open(url_group, encoding='utf-8') as f:
        try:
            data = f.readlines()
        except:
            next
    for k in range(25):
        try:
            data[k] = data[k].replace('\n','')
        except:
            next

    message = 'Расписание группы ' + group + '\n\n' + sm + ' Понедельник\n' + data[0] + '\n' + data[1] + '\n' + data[2] + '\n' + data[3] + '\n' + data[4] + '\n\n'
    message = message + sm + ' Вторник\n' + data[5] + '\n' + data[6] + '\n' + data[7] + '\n' + data[8] + '\n' + data[9] + '\n\n'
    message = message + sm + ' Среда\n' + data[10] + '\n' + data[11] + '\n' + data[12] + '\n' + data[13] + '\n' + data[14] + '\n\n'
    message = message + sm + ' Четверг\n' + data[15] + '\n' + data[16] + '\n' + data[17] + '\n' + data[18] + '\n' + data[19] + '\n\n'
    message = message + sm + ' Пятница\n' + data[20] + '\n' + data[21] + '\n' + data[22] + '\n' + data[23] + '\n' + data[24]

    vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message)