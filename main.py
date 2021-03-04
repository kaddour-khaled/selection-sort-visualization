import pygame
from button import Button
from selectionSort import SelctionSortVis


WINDOW_BACKGROUND = (0, 0, 0)
DRAWING_SPACE_BACKGROUND = (60, 63, 65)

DRAWING_SPACE_MARGIN_VERT = 50
DRAWING_SPACE_MARGIN_HORI = 100


class MainApp:
    def __init__(self,name, width=900, height=600):
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.btn = Button(20, 20, "Asc selection sort")
        self.btn2 = Button(200, 20, "Desc selection sort")
        # create the drawing space
        self.drawing_space = pygame.Surface(
            (
                self.width - (DRAWING_SPACE_MARGIN_HORI * 2), # width 
                self.height - (DRAWING_SPACE_MARGIN_VERT * 4) # height
            )
        )
      
        
    
    def on_init(self):
        self.is_running = True
        random_rects = generate_rectangles_with_random_height(self.drawing_space.get_height())
        self.selection_sort = SelctionSortVis(random_rects, self.drawing_space)

    def on_loop(self):
        if not self.selection_sort.selection_sort_is_finished():

            if not self.selection_sort.max_is_found():
                # find max
                self.selection_sort.find_max()
            else:
                # swap rects
                self.selection_sort.swap()
        else:
            print("sorting is finished")

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
        if self.btn.get_click_event() == event.type:
            print(self.btn.get_text())
        if self.btn2.get_click_event() == event.type:
            print(self.btn2.get_text())
        
        self.btn.on_Action(event)
        self.btn2.on_Action(event)

    def on_render(self):
        # clean the window
        self.window.fill(WINDOW_BACKGROUND)

        # draw drawing space on window
        self.drawing_space.fill(DRAWING_SPACE_BACKGROUND)

        # render all rects
        self.selection_sort.render_all_rects()
        # render check rect
        self.selection_sort.render_check_rect()
        # render max_rect
        self.selection_sort.render_max_rect()
        # render swap rect
        self.selection_sort.render_swap_rect()

        self.window.blit(
            self.drawing_space,
             (DRAWING_SPACE_MARGIN_HORI, DRAWING_SPACE_MARGIN_VERT * 3)
            )
        
        self.btn.render_button(self.window)
        self.btn2.render_button(self.window)
        # update window
        pygame.display.update()

    def on_clean(self):
        pygame.quit()

    def on_execute(self):
        clock = pygame.time.Clock()
        self.on_init()
        while self.is_running:
            clock.tick(10)
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
        self.on_clean()


def generate_rectangles_with_random_height( max_height, nbr_rects = 35, w = 20):
    import random
    rects = []
    for i in range(nbr_rects):
        h = random.randrange(10, max_height, 10)
        rect = pygame.rect.Rect(i * 20, max_height - h, 20 - 1, h)
        rects.append(rect)
    rects[-1].height = max_height
    rects[-1].y = 0
    return rects

if __name__ == "__main__":
    NAME = 'visualization  of selction sort algorithm'
    app = MainApp(NAME)
    app.on_execute()