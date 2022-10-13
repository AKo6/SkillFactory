class Client:
    def __init__(self,name,surname,city,balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб'

    def get_quests (self):
        return f'{self.name} {self.surname}. {self.city}'

client_1 = Client("Иван","Петров","Москва",50)
client_2 = Client("Пётр I","Романов","Санкт-Петербург",10000)
client_3 = Client("Антон","Чехов","Таганрог",100)
print(client_1)

quest_list = [client_1,client_2,client_3]
for quest in quest_list:
    print(quest.get_quests())
