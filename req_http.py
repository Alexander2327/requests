import requests
from pprint import pprint

TOKEN = '2619421814940190'
super_heroes = ['Hulk', 'Captain America', 'Thanos']


def most_intelligence(token, heroes_list):
    """Получение самого умного супергероя из списка супергероев"""
    intelligence = {}
    for name in heroes_list:
        url = f'https://superheroapi.com/api/{token}/search/{name}'
        response = requests.get(url)
        intelligence[f'{name}'] = int(response.json()['results'][0]['powerstats']['intelligence'])
    for key, value in intelligence.items():
        if value == max(intelligence.values()):
            hero = key
    return f'Most intelligence hero - {hero}'


def get_question():
    """Получение списка id вопросов за 2 дня с тэгом Python"""
    url = 'https://api.stackexchange.com//2.3/questions?fromdate=1644105600&order=desc&sort=activity&tagged=Python' \
          '&site=stackoverflow'
    response = requests.get(url)
    id = []
    for i in response.json()['items']:
        id.append(i['question_id'])
    print(id)


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_href(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": disk_file_path, "overwrite": "true"}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get('href', '')
        return href

    def upload(self, file_path):
        response = requests.put(self.get_href(disk_file_path=f'Netology/{file_path[:-4]}.txt'),
                                data=open(file_path, 'rb'))
        response.raise_for_status()


# if __name__ == '__main__':
    # print(most_intelligence(TOKEN, super_heroes)) # For first task
    # path_to_file = 'file_to_disk.txt'
    # token = ''
    # uploader = YaUploader(token) # For second task
    # result = uploader.upload(path_to_file)
    # get_question()  # For third task
