from jutsu_api import API   # Ссылка на доку https://github.com/gXLg/jutsu-api?ysclid=lukuh4nh9p361454898
from db import *
import time

main_url = "https://jut.su/"

api = API(verbosity=0)

print("[~] Starting Jutsu...")

start = time.time()

list_anime = api.search(maxpage=10)  # На каждой странице по 30 аниме

end = time.time()

print(f"[~] Ready for {end - start:0.2f} seconds")
print(f"[+] Count {len(list_anime)}\n")

print(f"[~] Arrive data in database...")

start = time.time()

update = Update.get_or_create(date=datetime.date.today())

for anime in list_anime:
    Anime.get_or_create(title=anime.name.name, url=main_url + anime.name.id, update=update[0].id)

end = time.time()

print(f"[~] Finished in database for {end - start:0.2f} seconds")
print(f"[~] Count in db {Anime.select().count()}\n")
