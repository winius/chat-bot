import random
import shelve
from datetime import datetime

def main(vk, peer_id):
    
    sm = '🍕'
    now = datetime.today().strftime('%A')
    
    if now=='Monday' or now=='Tuesday' or now=='Wednesday' or now=='Thursday' or now=='Friday':
        
        with shelve.open('profiles/2_branch/branch_data') as shlv:
            branch = shlv[str(peer_id)]
        with shelve.open('profiles/3_course/course_data') as shlv:
            course = shlv[str(peer_id)]
        
        if branch=='ОУИТ':
            if course=='1 курс':
                message=sm + ' [' + course + '] 12:00 - 12:30' 
            if course=='2 курс':
                message=sm + ' [' + course + '] 10:30 - 10:50'
            if course=='3 курс':
                message=sm + ' [' + course + '] 14:00 - 14:20'
            if course=='4 курс':
                message=sm + ' [' + course + '] 13:10 - 13:30'

            url = 'news/lunch_day.txt'
            with open(url, encoding='utf-8') as f:
                data = f.readlines()
            
            lunch_day = data[1].replace('\n','')
            lunch_number = int(data[0].replace('\n',''))
            today = datetime.today().strftime("%Y-%m-%d")

            if lunch_day != today:
                if lunch_number == 10:
                    lunch_number = 1
                else:
                    lunch_number += 1
                    
                with open(url, 'w', encoding='utf-8') as file:
                    print(lunch_number, file=file)
                    print(today, file=file)
            
            url = 'news/lunch_links.txt'
            with open(url, encoding='utf-8') as f:
                links = f.readlines()

            lunch_link = links[lunch_number]
            vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, attachment=lunch_link, keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read())
        
    #     if branch=='ОП':
    #         if course=='1 курс':
    #             message=sm + ' ' + course + '\n\n12:00 - 12:20' 
    #         if course=='2 курс':
    #             message=sm + ' ' + course + '\n\n13:20 - 13:40'
    #         if course=='3 курс':
    #             message=sm + ' ' + course + '\n\n10:20 - 10:40'
    #         if course=='4 курс':
    #             message=sm + ' ' + course + '\n\n13:40 - 14:00'
        
    else:
        message = '❌ Расписание всех обедов на сегодня не найдено'  
        vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read())