import random
import shelve

def main(vk, peer_id):
    
    with shelve.open('profiles/3_course/course_data') as shlv:
        course = shlv[str(peer_id)]
        
    smile = '⏰'
    
    if course=='1 курс':
        message = smile + ' ' + course + '\n8:45 вход №1\n\n[1 пара] 9:00 - 10:30\n[2 пара] 10:50 - 12:00\n[3 пара] 12:30 - 14:00\n[4 пара] 14:10 - 15:20'
    if course=='2 курс':
        message = smile + ' ' + course + '\n8:45 вход №2\n\n[1 пара] 9:00 - 10:30\n[2 пара] 10:50 - 12:20\n[3 пара] 12:30 - 14:00\n[4 пара] 14:10 - 15:30'
    if course=='3 курс':
        message = smile + ' ' + course + '\n9:00 вход №1\n\n[1 пара] 9:15 - 10:35\n[2 пара] 10:50 - 12:20\n[3 пара] 12:30 - 14:00\n[4 пара] 14:20 - 15:40'
    if course=='4 курс':
        message = smile + ' ' + course + '\n9:00 вход №2\n\n[1 пара] 9:15 - 10:35\n[2 пара] 10:50 - 12:20\n[3 пара] 12:30 - 14:10\n[4 пара] 14:20 - 15:40'

    vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read())