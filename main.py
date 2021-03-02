import pygame
from button import Button
WINDOW_BACKGROUND = (0, 0, 0)
DRAWING_SPACE_BACKGROUND = (60, 63, 65)

DRAWING_SPACE_MARGIN_VERT = 50
DRAWING_SPACE_MARGIN_HORI = 100


class MainApp:
    def __init__(self,name, width=900, height=600):
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.btn = Button(20, 20, "hello, world")
        self.btn2 = Button(200, 20, "bbbbb")
        # create the drawing space
        self.drawing_space = pygame.Surface(
            (
                self.width - (DRAWING_SPACE_MARGIN_HORI * 2), # width 
                self.height - (DRAWING_SPACE_MARGIN_VERT * 4) # height
            )
        )
      
        
    
    def on_init(self):
        self.is_running = True

    def on_loop(self):
        pass

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

        self.on_init()
        while self.is_running:

            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
        self.on_clean()


if __name__ == "__main__":
    NAME = 'visualization  of selction sort algorithm'
    app = MainApp(NAME)
    app.on_execute()