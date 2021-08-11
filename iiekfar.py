import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
#import json
#import os
#import datetime
vk_session = vk_api.VkApi(token='')
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)
spam = 'spam'
def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})
def girl(spam,str,id):
    what_work = ['что делаешь','чем занята']
    words = ['давай','дальше','?']
    what = ['ну как','нравиться','что думаешь','оцени','ну что','как тебе']
    citi = ['я из','ты откуда','откуда ты','где живешь','живешь где','давай погуляем','город']
    hi = ['привет','здравствуй','hi','hello','прив','qq','доброе утро','хае','добрый вечер','добрый день']
    bad = ['пизда','шлюха','сука','шмара','пошла нахуй','писька','лохушка','дура','шалава','иди нахуй']
    love = ['я тебя люблю','го секс','го встречаться','давай встречаться','я люблю тебя','может секс','хочу тебя']
    nobad = ['Давай общаться без мата, пожалуйста','Сам такой','Не говори так в мой адрес','=(','Перестань']
    si = ['скинь','отправь','интимку','сиськи','жопу']
    about = ['ты робот','кто ты','как звать','расскажи о себе']

    
    she_bl = ['ахахах','у меня есть парень','Нет','интимки покидаешь?']
    she_h = ['привет','hi','hello','хай','здравствуй','мур мур']
    she_l = ['у меня есть парень','давай останемся друзьями','ахахах','ты мне нравишься','я слишком далеко от тебя']
    she_b = ['ублюдок','пидор','лошок','скотина','сам такой','=(','Не говори так в мой адрес']
    she_how = ['нормально','хорошо','все в порядке','топ','отлично','все ок']
    she_si = ['нет','не буду','ты первый','фуу не','отстань от моего тела']
    she_what = ['?','Что?','Не понимаю тебя','Перефразируй','...','-_-']
    she_spam = ['Перестань','Я с первого раза поняла','Хватит','Хватит спамить','БЕЗ СПАМА']
    she_words = ['хрень','фуу','не нравиться','такое себе','улёт','класс','класс..','зачёт']
    she_forest = ['В лесу заблудился?','ау ау ау как ребенок','как ребенок','тебе медведь на ногу наступил','хватит мычать']
    she_citi = ['я из России','круто я из Москвы','я не пойду с тобой гулять','зачем тебе знать это?','улица пушкина дом колотушкина']
    she_work = ['смотрю телик','мемы листаю','мою посуду','ем','отдыхаю','дремлю']
    she_ask = ['как дела','что делаешь','почему ты мне не пишешь','я скучаю по тебе']
    she_about = ['я аня','я робот','я твой ночной кошмар']
    
    _hi = False
    _bad = False
    _love = False
    _how = False
    _si = False
    _what = False
    _forest = False
    _citi = False
    _work = False
    _words = False
    _about = False
    

    if 'как дела' in str:
        _how = True
    if 'ау' in str:
        _forest = True
    
    for i in range(0,len(hi)):
        if hi[i] in str:
            _hi = True
            break

    for i in range(0,len(what_work)):
        if what_work[i] in str:
            _work = True
            break


    for i in range(0,len(words)):
        if words[i] in str:
            _words = True
            break

    for i in range(0,len(about)):
        if about[i] in str:
            _about = True
            break


    for i in range(0,len(what)):
        if what[i] in str:
            _what = True
            break

    for i in range(0,len(citi)):
        if citi[i] in str:
            _citi = True
            break
        
    for i in range(0,len(love)):
        if love[i] in str:
            _love = True
            break
    
    for i in range(0,len(bad)):
        if bad[i] in str:
            _bad = True
            break

    for i in range(0,len(si)):
        if si[i] in str:
            _si = True
            break
    
    if spam == str:
        super_text = f'{she_spam[randint(0,len(she_spam)-1)]}'
        #if spam level big -> blacklist
    elif _forest:
        super_text = f'{she_forest[randint(0,len(she_forest)-1)]}'
    else:
        if _hi and _bad and _love and _si:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_si[randint(0,len(she_si)-1)]}'
        elif _hi and _love and _si:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_si[randint(0,len(she_si)-1)]}'         
        elif _hi and _bad and _love:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_bl[randint(0,len(she_bl)-1)]}'
        elif _hi and _bad and _how:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_how[randint(0,len(she_how)-1)]} {she_b[randint(0,len(she_b)-1)]}'
        elif _hi and _bad and _what:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_words[randint(0,len(she_words)-1)]}'
        elif _hi and _how and _what:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_how[randint(0,len(she_how)-1)]}'
        elif _hi and _bad:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_b[randint(0,len(she_b)-1)]}'
        elif _hi and _love:
            #super_text = f'{she_h[randint(0,len(she_h)-1)]} {name}, {she_l[randint(0,len(she_l)-1)]}'
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_l[randint(0,len(she_l)-1)]}'
        elif _hi and _how:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_how[randint(0,len(she_how)-1)]}'
        elif _hi and _si:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_si[randint(0,len(she_si)-1)]}'
        elif _hi and _what:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_words[randint(0,len(she_words)-1)]}'
        elif _hi and _citi:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_citi[randint(0,len(she_citi)-1)]}'
        elif _hi and _work:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_work[randint(0,len(she_work)-1)]}'
        elif _hi and _words:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_words[randint(0,len(she_ask)-1)]}'
        elif _hi and _about:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}, {she_about[randint(0,len(she_about)-1)]}'
        elif _hi:
            super_text = f'{she_h[randint(0,len(she_h)-1)]}'
        elif _words:
            super_text = f'{she_ask[randint(0,len(she_ask)-1)]}'
        elif _about:
            super_text = f'{she_about[randint(0,len(she_about)-1)]}'
        elif _what:
            super_text = f'{she_words[randint(0,len(she_words)-1)]}'
        elif _bad:
            super_text = f'{nobad[randint(0,len(nobad)-1)]}'
        elif _love:
            #super_text = f'{name}, {she_l[randint(0,len(she_l)-1)]}'
            super_text = f'{she_l[randint(0,len(she_l)-1)]}'
        elif _how:
            super_text = f'{she_how[randint(0,len(she_how)-1)]}'
        elif _si:
            super_text = f'{she_si[randint(0,len(she_si)-1)]}'
        elif _citi:
            super_text = f'{she_citi[randint(0,len(she_citi)-1)]}'
        elif _work:
            super_text = f'{she_work[randint(0,len(she_work)-1)]}'
        else:
            super_text = f'{she_what[randint(0,len(she_what)-1)]}'
    print(super_text)
    spam = str
    
for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            str = msg
            girl(spam,str,id)

