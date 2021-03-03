import pygame

RECT_COLOR = (180, 180, 180)
MAX_RECT_COLOR = (200, 100, 50)
CHECK_RECT_COLOR = (70, 140, 160)
SORT_RECT_COlOR = (73, 156, 84)

class SelctionSortVis:

    def __init__(self, rects):
        self.max_found = False # check if the index of maximmum is found or not yet found
        self.swap_ended = False # check if the swapping is start  not yet start
        self.is_sorted = False # # check if the list of rectangles  are sorted or  not yet start
        self.index = 0
        self.index_max = 0
        self.index_swap = 0
        self.list_rects = rects
    

    def find_max(self):
        pass

    def swap(self):
        pass

    def render_all_rects(self, surface):
        for rect in self.list_rects:
            pygame.draw.rect(surface, RECT_COLOR, rect)