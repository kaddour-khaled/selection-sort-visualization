import pygame

WINDOW_BACKGROUND = (0, 0, 0)

class MainApp:
    def __init__(self,name, width=900, height=600):
        self.width, self.height = width, height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill((255, 0, 0))
        
    
    def on_init(self):
        self.is_running = True

    def on_loop(self):
        pass

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
    def on_render(self):
        # clean the window
        self.window.fill(WINDOW_BACKGROUND)
        

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