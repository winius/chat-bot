import random

def main(vk, peer_id):
    vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message='🌐 Главное меню', keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read())