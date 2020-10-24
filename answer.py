import prof
import back
import all_lunch
import all_rasp
import bells
import rasp
import news
import notify
import change_group

def send_message(vk, peer_id, text, admin_id):

    if text=='замены':
        news.main(vk, peer_id)

    elif text=='звонки':
        bells.main(vk, peer_id)

    elif text=='настройки':
        prof.main(vk, peer_id)

    elif text=='обеды':
        all_lunch.main(vk, peer_id)

    elif text=='расписание':
        text = 'none'
        rasp.main(vk, peer_id, text)

    elif text=='полное расп.' or text=='полное расписание':
        all_rasp.main(vk, peer_id)

    elif text=='назад':
        back.main(vk, peer_id)

    elif text=='сменить группу':
        change_group.main(vk, peer_id)

    elif text=='уведомления':
        notify.main(vk, peer_id)
    
    else:
        rasp.main(vk, peer_id, text)