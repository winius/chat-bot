import random
import vk_api
import os

def main(vk, peer_id):
    with open('news/name_of_news.txt', encoding='utf-8') as f:
        data = f.readlines()
    name_of_news = data[0].replace('\n', '')
    
    smile = '📝'
    attachment = [ ]
    directory = "news/relevant/"
    files = os.listdir(directory)
    
    for i in files:
        upload = vk_api.VkUpload(vk)
        photo = upload.photo_messages(directory+i)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment.append(f'photo{owner_id}_{photo_id}_{access_key}')
                    
    message=smile + ' ' + name_of_news
    vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, attachment=attachment)