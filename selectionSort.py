import pygame

RECT_COLOR = (180, 180, 180)
MAX_RECT_COLOR = (200, 100, 50)
CHECK_RECT_COLOR = (70, 140, 160)
SORT_RECT_COlOR = (73, 156, 84)

class SelctionSortVis:

    def __init__(self, rects, drawing_surface):
        self.max_found = False # check if the index of maximmum is found or not yet found
        self.is_sorted = False # check if the list of rectangles  are sorted or  not yet start
        self.index = 1
        self.index_max = 0
        self.index_swap = 0
        self.list_rects = rects
        self.drawing_surface = drawing_surface
        self.distance_between_rects = abs(self.list_rects[0].x - self.list_rects[1].x)   
  
    def find_max(self):

        if self.index < len(self.list_rects):
            check_rect_height = self.list_rects[self.index].height
            max_rect_height = self.list_rects[self.index_max].height

            if max_rect_height < check_rect_height:
                self.index_max = self.index
            
            
            self.index += 1

    def swap(self):
        pass

    def render_all_rects(self):
        for rect in self.list_rects:
            pygame.draw.rect(self.drawing_surface, RECT_COLOR, rect)
    
    def render_max_rect(self):
        if self.index_max < len(self.list_rects):
            pygame.draw.rect(self.drawing_surface, MAX_RECT_COLOR, self.list_rects[self.index_max])
    
    def render_check_rect(self):
        if self.index < len(self.list_rects):
            pygame.draw.rect(self.drawing_surface, CHECK_RECT_COLOR, self.list_rects[self.index])
    
    def render_swap_rect(self):
        if self.index_swap < len(self.list_rects):
            pygame.draw.rect(self.drawing_surface, SORT_RECT_COlOR, self.list_rects[self.index_swap])
    

    def max_is_found(self):
        return self.index ==  len(self.list_rects)
      
    def selection_sort_is_finished(self):
        return self.index_swap == len(self.list_rects)