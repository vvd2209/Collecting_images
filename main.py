from pathlib import Path
from PIL import Image
import os


# Ввод названия папки пользователем
dicts = input("Введите название папки с изображениями: ")

# Папка с изображениями
folder_path = Path.cwd()/'data/'/dicts

# Список файлов в папке
images_list = os.listdir(folder_path)

# Открываем первое изображение для получения параметров
first_image = Image.open(os.path.join(folder_path, images_list[0]))

# Создаем новый файл tiff
tiff_path = Path.cwd()/'data/'
tiff = Image.new('RGB', (first_image.width, first_image.height * len(images_list)))
tiff.save('result.tiff')
# Собираем все изображения в один tiff файл
for i, image_name in enumerate(images_list):
    img = Image.open(os.path.join(folder_path, image_name))
    tiff.paste(img, (0, i * first_image.height))

# Сохраняем tiff файл
tiff.save('result.tiff')

print(f"Собрано {len(images_list)} изображений в файл {tiff_path}")
