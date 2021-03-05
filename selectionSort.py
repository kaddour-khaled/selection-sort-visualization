import pygame

pygame.font.init()
RECT_COLOR = (180, 180, 180)
MAX_RECT_COLOR = (200, 100, 50)
CHECK_RECT_COLOR = (70, 140, 160)
SORT_RECT_COlOR = (73, 156, 84)
VEL = 20
ASC = 0
DESC = 1
class SelctionSortVis:

    def __init__(self, rects, drawing_surface, direction=ASC):
        self.font = pygame.font.SysFont('comicsans', 24)
        self.index = 1
        self.max_min_index = 0
        self.swap_index = 0
        self.list_rects = rects
        self.drawing_surface = drawing_surface
        self.distance_between_rects = abs(self.list_rects[0].x - self.list_rects[1].x)
        self.direction = direction 
  
    def find_max_min(self):

        if self.index < len(self.list_rects):
            check_rect_height = self.list_rects[self.index].height
            max_min_rect_height = self.list_rects[self.max_min_index].height
            if self.direction == ASC:
                if max_min_rect_height < check_rect_height:
                    self.max_min_index = self.index
            if self.direction == DESC:
                if max_min_rect_height > check_rect_height:
                    self.max_min_index = self.index
            self.index += 1

    def swap(self):
        if self.swap_index < len(self.list_rects):
            x = self.swap_index * self.distance_between_rects
            if x < self.list_rects[self.max_min_index].x:
                self.list_rects[self.swap_index].x += VEL
                self.list_rects[self.max_min_index].x -= VEL 
            else:
                self.list_rects[self.swap_index],  self.list_rects[self.max_min_index] =  self.list_rects[self.max_min_index], self.list_rects[self.swap_index]
                self.swap_index += 1
                self.max_min_index = self.swap_index
                self.index = self.swap_index

    def render_all_rects(self):
        for rect in self.list_rects:
            pygame.draw.rect(self.drawing_surface, RECT_COLOR, rect)
    
    def render_max_rect(self):
        if self.max_min_index < len(self.list_rects):
            pygame.draw.rect(self.drawing_surface, MAX_RECT_COLOR, self.list_rects[self.max_min_index])
    
    def render_check_rect(self):
        if self.index < len(self.list_rects):
            pygame.draw.rect(self.drawing_surface, CHECK_RECT_COLOR, self.list_rects[self.index])
    
    def render_swap_rect(self):
        if self.swap_index < len(self.list_rects):
            pygame.draw.rect(self.drawing_surface, SORT_RECT_COlOR, self.list_rects[self.swap_index])
    

    def max_is_found(self):
        return self.index ==  len(self.list_rects)
      
    def selection_sort_is_finished(self):
        return self.swap_index == len(self.list_rects)
    
    def render_max_text(self, surface):
        text = self.font.render("max/min rectangle", 1, MAX_RECT_COLOR)
        text_x_pos = surface.get_width()- text.get_width() - 20
        text_y_pos = surface.get_height() - text.get_height() -20
        surface.blit(text, ( text_x_pos , text_y_pos))
    
    def render_sort_text(self, surface):
        text = self.font.render("sort rectangle", 1, SORT_RECT_COlOR)
        text_x_pos = 20
        text_y_pos = surface.get_height() - text.get_height() -20
        surface.blit(text, ( text_x_pos , text_y_pos))
    
    def render_check_text(self, surface):
        text = self.font.render("check rectangle", 1, CHECK_RECT_COLOR)
        text_x_pos = surface.get_width() //  2 - text.get_width() // 2
        text_y_pos = surface.get_height() - text.get_height() -20
        surface.blit(text, ( text_x_pos , text_y_pos))
        