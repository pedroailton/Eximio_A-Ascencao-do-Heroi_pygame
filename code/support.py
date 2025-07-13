from settings import *

# Transformar depois em classe
# Para o código ser completamente orientado a objeto

def folder_importer(*path): # o que é esse asterisco?
    surfs = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            full_path = join(folder_path, file_name)
            surfs[file_names.split('.')[0]] =  pygame.image.load(full_path).convert_alpha()
    return surfs

def audio_importer(*path):
    audio_dict = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            audio_dict[file_name.split('.')[0]] =  pygame.mixer.Sound(join(folder_path, file_name))
    return audio_dict