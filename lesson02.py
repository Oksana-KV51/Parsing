import requests
import pprint
# URL API
url = 'https://jsonplaceholder.typicode.com/posts'
#создаем словарь
data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post(url, data=data)
print(response.status_code)
print(f'ответ - {response.json()}')

# URL API
#url = 'https://jsonplaceholder.typicode.com/posts'
# Параметры для GET-запроса
#params = {
   # 'userId': 1
#}
# Отправляем GET-запрос с параметрами
#response = requests.get(url, params=params)

#response_json = response.json()
#pprint.pprint(response_json)


#params = {
   # 'q' : 'html'
#}
#response = requests.get('https://api.github.com/search/repositories', params=params)
#print(response.status_code)
#if response.ok:
    #print('запрос успешно выполнен')
#else:
    #print('произошла ошибка')

#print(response.text)
#response_json = response.json()
#pprint.pprint(response_json)
#print(f"количество репозиториев с использованием html: {response_json['total_count']}")

#img = 'https://netology.ru/_next/static/media/phone.42ed97e9.png'
#response = requests.get(img)
#with open('test.jpg', 'wb') as file:
    #file.write(response.content)