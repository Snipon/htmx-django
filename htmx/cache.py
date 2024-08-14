from pprint import pprint

cache = dict()
from faker import Faker
fake = Faker()

def fake_content(path):
    if path not in cache:
        cache[path] = {
            'title': fake.color_name(),
            'message': fake.text(max_nb_chars=500),
            'image': fake.image_url(width=900, height=450),
            'path': path,
        }

    return cache[path]

def fake_content_list():
    return [fake_content(f'/content/{i}') for i in range(1, 6)]
