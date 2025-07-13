import pygame
from os.path import join
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

COLORS = {
    'black': '#000000',
    'red': '#ee1a0f',
    'gray': "#646464",
    'white': '#ffffff',
}

CHARACTERS_DATA = {
    'Espadachim': {'poder': 'espada', 'vida': 200},
    'Arqueiro': {'poder': 'arco', 'vida': 140},
    'Mago': {'poder': 'magia', 'vida': 100},
    'Lacaio': {'poder': 'garras', 'vida': 100},
    'O Desertor': {'poder': 'magia', 'vida': 1000},
}

ABILITIES_DATA = {
    'golpe de espada': {'dano': 50, 'poder': 'espada', 'animation': 'golpe_de_espada'},
    'golpe com as mãos': {'dano': 20, 'poder': 'espada', 'animation': 'golpe_com_maos'},
    'atirar flecha': {'dano': 40, 'poder': 'arco', 'animation': 'arco_e_flecha'},
    'lançar magia': {'dano': 45, 'poder': 'espada', 'animation': 'golpe_com_maos'},
    'arranhar': {'dano': 25, 'poder': 'garras', 'animation': 'arranhar'},
    'meteoro': {'dano': 70, 'poder': 'magia', 'animation': 'meteoro'},
    'lançar raio': {'dano': 100, 'poder': 'magia', 'animation': 'raio'},
}

ELEMENT_DATA = {
    'espada': {'magia': 1, 'garras': 2},
    'arco': {'magia': 2, 'garras': 0.5},
    'magia': {'espada': 2, 'arco': 1},
    'garras': {'espada': 0.5, 'arco': 2},
}