from csv import reader
import pygame
from settings import *


#Importing maps from Tiled (exported as csv file)
def import_csv_layout(path):
    terrain_map = []
    with open(path, mode='r') as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


#DON'T USE UNLESS ABSOLUTELY NECESSARY (terrible for performance)
#Will add a better alternative soon...
def import_cut_graphic(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_width() / TILE_SIZE)
    tile_num_y = int(surface.get_height() / TILE_SIZE)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            new_surface = pygame.Surface((TILE_SIZE,TILE_SIZE))
            new_surface.blit(surface,(0,0), pygame.Rect(x,y,TILE_SIZE,TILE_SIZE))
            cut_tiles.append(new_surface)

    return cut_tiles


