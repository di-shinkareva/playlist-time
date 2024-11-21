# IvanovaShinkarevaplaylist-time
#Ranepa case 2 for playlist task
#импорт модулей 
import random
import datetime
from typing import Iterable
#плейлисты 
playlist_c = (
 "Happy Nation; 3.32",
 "It's My Life; 3.59",
 "Lady(Hear Me Tonight); 5.07",
 "Fields Of Gold; 3.38",
 "The Winner Takes It All; 4.54",
 "Self Control; 4.06",
 "I Shot The Sheriff; 4.57",
 "Don't Give Up; 6.34",
 "Relax, Take It Easy; 4.30",
 "Dancing Queen; 3.36",
)

playlist_b = {
 'Портофино': 3.32,
 'Снег': 4.35,
 'Попытка №5': 3.23,
 'Тополиный Пух': 3.53,
 'Если хочешь остаться': 4.48,
 'Зеленоглазое такси': 5.52,
 'Ты не верь слезам': 3.1,
 'Nowhere to Run': 2.58,
 'Салют, Вера': 4.44,
 'Улетаю': 3.24,
 'Опять метель': 3.37,
 }
 #определение функции для обработки плейлистов
def get_duration(playlist: Iterable, n: int) -> datetime.timedelta:
    total_duration = datetime.timedelta(seconds=0)
#преобразование словаря в список ключей (названия песен)
    if isinstance(playlist, dict):
        playlist = list(playlist.keys())

    selected_songs = random.sample(playlist, n)

    if isinstance(playlist, tuple):
        for song in selected_songs:
            duration = datetime.timedelta(minutes=int(song.split(';')[1].strip().split('.')[0]),
                                       seconds=int(song.split(';')[1].strip().split('.')[1]))
            total_duration += duration
#проверка,является ли playlist списком
    elif isinstance(playlist, list):
      for song in selected_songs:
            duration = playlist_b[song]
#преобразование время из float в строку перед разделением
            duration_str = str(duration)
            total_duration += datetime.timedelta(minutes=int(duration_str.split('.')[0]),
                                       seconds=int(duration_str.split('.')[1]))

    return total_duration
#пример использования функции с плейлистом playlist_c, выбраны 5 песен
duration_c = get_duration(playlist_c, 5)
print(f"Общее время звучания 5 случайных песен из playlist_c: {duration_c}")
#пример использования функции с плейлистом playlist_b, выбраны 3 песни 
duration_b = get_duration(playlist_b, 3)
print(f"Общее время звучания 3 случайных песен из playlist_b: {duration_b}")

