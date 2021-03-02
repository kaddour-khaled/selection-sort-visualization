import pygame

# init font module of pygame
pygame.font.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# margins
PADDING_VERT = 10
PADDING_HORI = 10

# create a font
FONT = pygame.font.SysFont('comicsans', 24)

class Button:
    INDEX = 0
    def __init__(self, x, y, text): 
        self.background_color = WHITE
        self.text_color = BLACK
        self.text = text
        self.x = x 
        self.y = y

        # create the text of button
        self.text_surface = FONT.render(self.text, 1, self.text_color)

        # create the surface of button
        self.button = pygame.Surface((self.text_surface.get_width() + PADDING_HORI, self.text_surface.get_height() + PADDING_VERT))
        
        self.index = Button.INDEX

        # create the user event of button
        self.click_event = pygame.USEREVENT + self.index

        Button.INDEX += 1

    def get_index(self):
        return self.index
    
    def render_button(self, surface):
        # draw button
        self.button.fill(self.background_color)
        self.button.blit(self.text_surface, (PADDING_HORI // 2, PADDING_VERT // 2))
        surface.blit(self.button, (self.x, self.y))
       
    def set_background(self, new_color):
        # change the background of butoon
        self.background_color = new_color
    
    def set_color(self, new_color):
        # change the color text of the button
        self.text_color = new_color
        self.text_surface = FONT.render(self.text, 1, self.text_color)

    def set_text(self, new_text):
        # change the text of the button
        self.text = new_text
        self.text_surface = FONT.render(self.text, 1, self.text_color)

    def get_click_event(self):
        return self.click_event

    def on_Action(self, event):
        # handle the mouse event on the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # grasp value of mouse event
            btn_index, mous_pos_x, mous_pos_y = event.button, event.pos[0], event.pos[1]

            # check the value of mouse event
            left_mouse_btn_is_clicked = btn_index == 1
            mouse_in_hori_range = self.x < mous_pos_x < self.x + self.button.get_width()
            mouse_in_vert_range = self.y < mous_pos_y < self.y + self.button.get_height()

            if  left_mouse_btn_is_clicked and mouse_in_hori_range and mouse_in_vert_range:
                pygame.event.post(pygame.event.Event(self.click_event))
            
    def get_text(self):
        return self.text