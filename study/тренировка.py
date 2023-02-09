from datetime import date
import turtle as t
import django
import sys

# today = date.today()
# print(today)

my_birthday = date(2001, 10, 3)
print(my_birthday)
print(my_birthday.toordinal())
print(my_birthday.fromordinal(my_birthday.toordinal()))
print(my_birthday.ctime())
my_list = my_birthday.ctime().split()
print(my_list)
# timedelta - количество дней до/после какой-то даты


# t.circle(90)

# t.Screen().mainloop()

# print(*sys.path, sep='\n')


# url = URL.format(TOKEN=TOKEN, method=updates)  - для чат-бота
# url = URL.format(TOKEN=TOKEN, method=send)
#
#
# data = {
#     'chat_id': '1563279921',
#     'text': 'Sure, I want to talk with you!'
# }
#
#
# response = r.post(url, data)
# print(response)
# print(response.text)
# response = r.get(url)

# print(response)

# print(response.text)
# print(type(response.text))


# json.loads - из пайтон-файла в словарь
# json.dumps - из словаря в пайтон-файл

# json_content = json.loads(response.text)
# print(json_content)
# print(type(json_content))
