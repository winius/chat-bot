import time
import vk_api
import shelve
import random
import requests
import config, answer
import reg1, reg2, reg3, reg4
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def main():

    vk_session = vk_api.VkApi(token=config.token)
    longpoll = VkBotLongPoll(vk_session, config.group_id)
    vk = vk_session.get_api()
    admin_id = config.admin_id

    try:
        print("Выполняется включение")
        vk.messages.send(peer_id=admin_id, random_id=random.getrandbits(32), message="Бот работает")
        
        for event in longpoll.listen():
            
            if event.type == VkBotEventType.MESSAGE_NEW:
                
                text = event.obj.text.lower()
                peer_id = event.obj.peer_id
                user_info = vk.users.get(user_ids=peer_id)
                full_name = user_info[0]['first_name'] + ' ' + user_info[0]['last_name'] 
                print(full_name + ' >> ' + text)
                
                if text=='27042001':
                    break

                if event.from_user:

                    try:
                        with shelve.open('profiles/1_id/id_data') as shlv:
                            users = list(shlv.items())
                        with shelve.open('profiles/2_branch/branch_data') as shlv:
                            branch = shlv[str(peer_id)]
                        with shelve.open('profiles/3_course/course_data') as shlv:
                            course = shlv[str(peer_id)]
                        with shelve.open('profiles/4_group/group_data') as shlv:
                            group = shlv[str(peer_id)]
                        
                        list_users = [ ]
                        for user in users:
                            list_users.append(user[0])
                        
                        if str(peer_id) in list_users and branch=='null' and course=='null' and group=='null':
                            reg2.main(vk, peer_id, text)
                        elif str(peer_id) in list_users and branch!='null' and course=='null' and group=='null':
                            reg3.main(vk, peer_id, text)
                        elif str(peer_id) in list_users and branch!='null' and course!='null' and group=='null':
                            reg4.main(vk, peer_id, text, admin_id)
                        elif str(peer_id) in list_users and branch!='null' and course!='null' and group!='null':
                            try:
                                answer.send_message(vk, peer_id, text, admin_id)
                            except:
                                vk.messages.markAsRead(peer_id=peer_id)
                                vk.messages.send(peer_id=admin_id, random_id=random.getrandbits(32), forward_messages=event.obj.id)
                        else:
                            reg1.main(vk, peer_id)
                    
                    except:
                        reg1.main(vk, peer_id)

    except requests.exceptions.ReadTimeout:
        vk.messages.send(peer_id=admin_id, random_id=random.getrandbits(32), message="Timeout")
        print("Переподключение через 3 секунды...")
        time.sleep(3)
        print("Переподключение...")
        main()
    
    except Exception as e:
        vk.messages.send(peer_id=admin_id, random_id=random.getrandbits(32), message=e.__class__)
        print("Переподключение через 3 секунды...")
        time.sleep(3)
        print("Переподключение...")
        main()
        
    except (ConnectionError, TimeoutError) as e:
        vk.messages.send(peer_id=admin_id, random_id=random.getrandbits(32), message=+e.__class__)
        print("Переподключение через 3 секунды...")
        time.sleep(3)
        print("Переподключение...")
        main()
main()