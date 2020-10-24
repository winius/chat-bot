import random
import datetime
import shelve

def main(vk, peer_id, text):
    sm = '📆'
    week = datetime.datetime.today().strftime('%A')
    whatnow = int(datetime.datetime.today().strftime('%H'))

    ################################################################## опеределяем группу
    if text=='none':
        with shelve.open('profiles/4_group/group_data') as shlv:
            group = shlv[str(peer_id)]
    else:
        group = text

    ################################################################## опеределяем числитель/знаменатель
    a = '2020-08-17'
    b = datetime.datetime.today().strftime("%Y-%m-%d")
    a = a.split('-')
    b = b.split('-')
    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
    bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
    cc = bb-aa
    dd = str(cc)
    colvo = int(dd.split()[0])
    colvo = colvo // 7
    colvo = colvo % 2
    chz = 'none'
    chzn = 'none'
    if (colvo == 0):
        chz = 'ЧИСЛИТЕЛЬ'
        chzn = 'ЗНАМЕНАТЕЛЬ'
    else:
        chz = 'ЗНАМЕНАТЕЛЬ'
        chzn = 'ЧИСЛИТЕЛЬ'

    ################################################################## считываем определенное расписание
    url_group = 'groups/' + group + '/' + str(colvo) + '.txt'
    with open(url_group, encoding='utf-8') as f:
        data = f.readlines()
    for k in range(25):
        try:
            data[k] = data[k].replace('\n','')
        except:
            next

    if (colvo==0):
        url_group = 'groups/' + group + '/1.txt'
        with open(url_group, encoding='utf-8') as f:
            datan = f.readlines()
        for k in range(25):
            try:
                datan[k] = datan[k].replace('\n','')
            except:
                next
    if (colvo==1):
        url_group = 'groups/' + group + '/0.txt'
        with open(url_group, encoding='utf-8') as f:
            datan = f.readlines()
        for k in range(25):
            try:
                datan[k] = datan[k].replace('\n','')
            except:
                next

    ################################################################## записываем расписание в ответ
    if (whatnow < 18):
        if (week == 'Monday'):
            message = 'Расписание группы ' + group + '\n' + chz + '\n\n' + sm + ' Сегодня понедельник\n' + data[0] + '\n' + data[1] + '\n' + data[2] + '\n' + data[3] + '\n' + data[4] + '\n\n' + sm + ' Завтра\n' + data[5] + '\n' + data[6] + '\n' + data[7] + '\n' + data[8] + '\n' + data[9]
        if (week == 'Tuesday'):
            message = 'Расписание группы ' + group + '\n' + chz + '\n\n' + sm + ' Сегодня вторник\n' + data[5] + '\n' + data[6] + '\n' + data[7] + '\n' + data[8] + '\n' + data[9] + '\n\n' + sm + ' Завтра\n' + data[10] + '\n' + data[11] + '\n' + data[12] + '\n' + data[13] + '\n' + data[14]
        if (week == 'Wednesday'):
            message = 'Расписание группы ' + group + '\n' + chz + '\n\n' + sm + ' Сегодня среда\n' + data[10] + '\n' + data[11] + '\n' + data[12] + '\n' + data[13] + '\n' + data[14] + '\n\n' + sm + ' Завтра\n' + data[15] + '\n' + data[16] + '\n' + data[17] + '\n' + data[18] + '\n' + data[19]
        if (week == 'Thursday'):
            message = 'Расписание группы ' + group + '\n' + chz + '\n\n' + sm + ' Сегодня четверг\n' + data[15] + '\n' + data[16] + '\n' + data[17] + '\n' + data[18] + '\n' + data[19] + '\n\n' + sm + ' Завтра\n' + data[20] + '\n' + data[21] + '\n' + data[22] + '\n' + data[23] + '\n' + data[24]
        if (week == 'Friday'):
            message = 'Расписание группы ' + group + '\n' + chz + '\n\n' + sm + ' Сегодня пятница\n' + data[20] + '\n' + data[21] + '\n' + data[22] + '\n' + data[23] + '\n' + data[24] + '\n\n' + chzn + '\n' + sm + ' Понедельник\n' + datan[0] + '\n' + datan[1] + '\n' + datan[2] + '\n' + datan[3] + '\n' + datan[4]
        if (week == 'Saturday' or week == 'Sunday'):
            message = 'Расписание группы ' + group + '\n' + chzn + '\n\n' + sm + ' Понедельник\n' + datan[0] + '\n' + datan[1] + '\n' + datan[2] + '\n' + datan[3] + '\n' + datan[4] + '\n\n' + sm + ' Вторник\n' + datan[5] + '\n' + datan[6] + '\n' + datan[7] + '\n' + datan[8] + '\n' + datan[9]
    else:
        if (week == 'Monday'):
            message = 'Расписание группы ' + group + '\n' + chz + '\n\n' + sm + ' Завтра вторник\n' + data[5] + '\n' + data[6] + '\n' + data[7] + '\n' + data[8] + '\n' + data[9] + '\n\n' + sm + ' Среда\n' + data[10] + '\n' + data[11] + '\n' + data[12] + '\n' + data[13] + '\n' + data[14]
        if (week == 'Tuesday'):
            message = 'Расписание группы ' + group + '\n' + chz + '\n\n' + sm + ' Завтра среда\n' + data[10] + '\n' + data[11] + '\n' + data[12] + '\n' + data[13] + '\n' + data[14] + '\n\n' + sm + ' Четверг\n' + data[15] + '\n' + data[16] + '\n' + data[17] + '\n' + data[18] + '\n' + data[19]
        if (week == 'Wednesday'):
            message = 'Расписание группы ' + group + '\n' + chz + '\n\n' + sm + ' Завтра четверг\n' + data[15] + '\n' + data[16] + '\n' + data[17] + '\n' + data[18] + '\n' + data[19] + '\n\n' + sm + ' Пятница\n' + data[20] + '\n' + data[21] + '\n' + data[22] + '\n' + data[23] + '\n' + data[24]
        if (week == 'Thursday'):
            message = 'Расписание группы ' + group + '\n' + chz + '\n\n' + sm + ' Завтра пятница\n' + data[20] + '\n' + data[21] + '\n' + data[22] + '\n' + data[23] + '\n' + data[24] + '\n\n' + chzn + '\n' + sm + ' Понедельник\n' + datan[0] + '\n' + datan[1] + '\n' + datan[2] + '\n' + datan[3] + '\n' + datan[4]
        if (week == 'Saturday' or week == 'Sunday' or week == 'Friday'):
            message = 'Расписание группы ' + group + '\n' + chzn + '\n\n' + sm + ' Понедельник\n' + datan[0] + '\n' + datan[1] + '\n' + datan[2] + '\n' + datan[3] + '\n' + datan[4] + '\n\n' + sm + ' Вторник\n' + datan[5] + '\n' + datan[6] + '\n' + datan[7] + '\n' + datan[8] + '\n' + datan[9]

    vk.messages.send(peer_id=peer_id, random_id=random.getrandbits(32), message=message, keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read())
