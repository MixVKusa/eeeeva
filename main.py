import requests

cities = input('Введите города, разделяя их запятой: ').split(',')
point_min = None
south_city = None
for i in cities:
    rep = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&'
                       f'geocode={i}&format=json')
    j_rep = rep.json()
    pathtonames = j_rep['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    points = pathtonames['Point']['pos'].split()
    y = points[1]
    if point_min is None or y < point_min:
        point_min = y
        south_city = i

print(f'Самый южный город - {south_city}')
