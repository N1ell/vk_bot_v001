import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
import pypyodbc

mySQLServer = 'DESKTOP-TKFJREF\SQLEXPRESS'
myDatabase = 'vk_bot'

try:
    connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+mySQLServer+';'
                            'Database='+myDatabase+';')
except Exeption:
    print("Возникла ошибка при подключении дб")

cursor = connection.cursor()

def find_me(id: int):
    cursor.execute("""
                SELECT user_id,user_name
                FROM dbo.bot_users
                """)
    results = cursor.fetchall()
    for row in results:
        if row[0] == id:
                return row[1]

def AddToDB(id: int):
    #cursor.execute(mySQLQueryExistId,id)
    cursor.execute("""SELECT COUNT(*) FROM dbo.bot_users WHERE user_id = ?""",(id,))
    res = cursor.fetchall()
    if res[0][0] == 1:
        return 1
    if res[0][0] == 0:
        cursor.execute("""INSERT INTO dbo.bot_users (user_id) VALUES (?)""",(id,))
        connection.commit()
        return 0

vk_session = vk_api.VkApi(token='9c7c696912713e79b7db547db5a10ea32f7c5bf2b65dfb09933eae0f034ffd73d9c9891720fcb9fb37a05')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "192575276")

def getHello(hello):
    q = 0
    if hello == "Привет":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Привет!'
        )
        q = q + 1
    if hello == "привет":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Привет!'
        )
        q = q + 1
    if hello == "Прив":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Привет!'
        )
        q = q + 1
    if hello == "прив":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Привет!'
        )
        q = q + 1
    if hello == "Хай":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хай)'
        )
        q = q + 1
    if hello == "хай":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хай)'
        )
        q = q + 1
    if hello == "Ку":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Ку'
        )
        q = q + 1
    if hello == "ку":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Ку'
        )
        q = q + 1
    if hello == "Здравствуйте":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Здравствуй'
        )
        q = q + 1
    if hello == "здравствуйте":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Здравствуй'
        )
        q = q + 1
    print(hello)
    return q

def getQuestion(question):
    w = 0
    if question == 'Начать':
        if AddToDB(event.message.from_id) == 0:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message='Ты здесь в первый раз? Добро пожаловать)'
            ) 
        if AddToDB(event.message.from_id) == 1:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message='Я тебя уже знаю))'
            ) 
        w = w + 1 #старт
    if question == 'начать': 
        if AddToDB(event.message.from_id) == 0:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message='Ты здесь в первый раз? Добро пожаловать)'
            ) 
        if AddToDB(event.message.from_id) == 1:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message='Я тебя уже знаю))'
            ) 
        w = w + 1 #старт
    if question == "Как тебя зовут?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1  #имя бота
    if question == "как тебя зовут?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "Как тебя зовут":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "как тебя зовут":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "Какое у тебя имя?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "какое у тебя имя?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "Какое у тебя имя":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        ) 
        w = w + 1 #имя бота
    if question == "какое у тебя имя":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "А как тебя зовут?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1  #имя бота
    if question == "а как тебя зовут?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота 
    if question == "А как тебя зовут":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "а как тебя зовут":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "А какое у тебя имя?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "а какое у тебя имя?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "А какое у тебя имя":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        ) 
        w = w + 1 #имя бота
    if question == "акакое у тебя имя":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "Как тебя называть?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "как тебя называть?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1#имя бота
    if question == "Как тебя называть":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "как тебя называть":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "Как тебя звать?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "как тебя звать?":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        ) 
        w = w + 1 #имя бота
    if question == "Как тебя звать":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == "как тебя звать":
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='У меня нет имени. Т_Т'
        )
        w = w + 1 #имя бота
    if question == 'Что ты умеешь?': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды 
    if question == 'что ты умеешь?': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == 'Что ты умеешь': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == 'что ты умеешь': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == 'Что ты можешь?': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == 'что ты можешь?':
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == 'Что ты можешь': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == 'что ты можешь': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == 'Команды': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == 'команды': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == '!Команды': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == '!команды': 
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Список команд: \n1.Как тебя зовут \n2.Как меня зовут \n...\nP.s. Я все еще учусь!)'
        )
        w = w + 1 #команды
    if question == 'Как меня зовут?':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'Как меня зовут':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'как меня зовут?':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'как меня зовут':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'Как меня звать?':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'Как меня звать':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'как меня звать?':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'как меня звать':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'Кто я?':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'Кто я':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'кто я?':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    if question == 'кто я':
        name = find_me(event.message.from_id)
        if name == None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Ты еще не сказал мне свое имя. \nЧтобы сказать как тебя зовут ты можешь написать 'Меня зовут...' или 'Мое имя...'"
            )
        if name != None:
            vk.messages.send(
            user_id=event.message.from_id,
            random_id=get_random_id(),
            message="Тебя зовут: "+name
            )
        w = w + 1  #имя пользователя
    return w

def PutCommand(command):
    e = 0
    if "Забудь как меня зовут" in command and e == 0:
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(None,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Как скажешь.'
        )
        e = e + 1  #Удаляет имя
    if "Забудь мое имя" in command and e == 0:
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(None,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Как скажешь.'
        )
        e = e + 1  #Удаляет имя
    if "Нет меня зовут" in command and e == 0 :
        command = command[14:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    if "нет меня зовут" in command and e == 0 : #UPDATE bot_users SET user_name = 'Котик' WHERE user_id = 440796331 
        command = command[14:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    if "Меня зовут" in command and e == 0 :
        command = command[10:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    if "меня зовут" in command and e == 0 : #UPDATE bot_users SET user_name = 'Котик' WHERE user_id = 440796331 
        command = command[10:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    if "Мое имя" in command and e == 0 : #UPDATE bot_users SET user_name = 'Котик' WHERE user_id = 440796331 
        command = command[7:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    if "мое имя" in command and e == 0 : #UPDATE bot_users SET user_name = 'Котик' WHERE user_id = 440796331 
        command = command[7:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    if "Называй меня" in command and e == 0 : #UPDATE bot_users SET user_name = 'Котик' WHERE user_id = 440796331 
        command = command[12:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    if "называй меня" in command and e == 0 : #UPDATE bot_users SET user_name = 'Котик' WHERE user_id = 440796331 
        command = command[12:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    if "Зови меня" in command and e == 0 : #UPDATE bot_users SET user_name = 'Котик' WHERE user_id = 440796331 
        command = command[9:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    if "Зови меня" in command and e == 0 : #UPDATE bot_users SET user_name = 'Котик' WHERE user_id = 440796331 
        command = command[9:]
        cursor.execute("""UPDATE bot_users SET user_name = ? WHERE user_id = ? """,(command,event.message.from_id))
        connection.commit()
        vk.messages.send(
        user_id=event.message.from_id,
        random_id=get_random_id(),
        message='Хорошо. Я запомню!'
        )
        e = e + 1  #Сам задает имя
    return e

for event in longpoll.listen(): #Проверка действий
    q , w = 0 , 0
    if event.type == VkBotEventType.MESSAGE_NEW:
        #проверяем не пустое ли сообщение нам пришло
        if event.obj.text != '': 
            #проверяем пришло сообщение от пользователя или нет
            if event.from_user:
                q = getHello(event.message.text)
                if q == 0: 
                   w = getQuestion(event.message.text)
                   if w == 0:
                      e = PutCommand(event.message.text)
                      if (q + w + e) == 0:
                        vk.messages.send(
                        user_id=event.message.from_id,
                        random_id=get_random_id(),
                        message='Я не понимаю что ты написал/a, попробуй еще раз.'
                        )   

connection.close()