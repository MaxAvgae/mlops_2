import os
import tensorflow as tf

dataset_folder = "cats_and_dogs/"

for folder_name in ("Cat", "Dog"):
    img_for_d = 0
    for file_name in os.listdir(f"{dataset_folder}PetImages/{folder_name}"):
        file_path = f"{dataset_folder}PetImages/{folder_name}/{file_name}"

        with open(file_path, "rb") as file:
            # Ищем в первых 4 байтах файла байты "JFIF" (в ASCII / UTF-8 кодах).
            has_jfif = tf.compat.as_bytes("JFIF") in file.peek(4)
            if not has_jfif:
                file.close()
                os.remove(file_path)
                img_for_d += 1
    print(f"Удалено {img_for_d} изображений из директории {folder_name}")
