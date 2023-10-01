from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('charactersheet.png')
hand = load_image('hand_arrow.png')

frame_up = [
    (11, 3, 41, 53), 
    (78, 3, 42, 60), 
    (11, 3, 41, 53), 
    (218, 3, 42, 60) 
]

frame_right = [
    (23, 287 - 212, 46, 50), 
    (90, 287 - 212, 46, 54), 
    (23, 287 - 212, 46, 50), 
    (223, 287 - 212, 48, 54), 
]

frame_left = [
    (0, 287 - 140, 46, 50), 
    (69, 287 - 140, 48, 54), 
    (0, 287 - 140, 46, 50),  
    (204, 287 - 140, 46, 54), 
]

frame_down = [
    (11, 287 - 68, 46, 50), 
    (75, 287 - 68, 46, 52), 
    (11, 287 - 68, 46, 50),  
    (219, 287 - 68, 46, 52), 
]

def handle_events():
    global running, mouse_x, mouse_y, target_x, target_y, clicked
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            target_x.append(event.x)
            target_y.append(TUK_HEIGHT - 1 - event.y)


running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
mouse_x = 0
mouse_y = 0
target_x = []
target_y = []


while running:
    handle_events()
    
    if target_x:
        frame_index = 0
        x1, y1 = x, y
        x2 = target_x[0]
        y2 = target_y[0]
        dir_y = y2 - y1
        dir_x = x2 - x1
        for i in range(0, 100 + 1, 2):
            t = i / 100
            x = (1 - t) * x1 + t * x2
            y = (1 - t) * y1 + t * y2
            tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            for i in range(len(target_x)):
                handle_events()
                hand.draw(mouse_x, mouse_y)
                hand.draw(target_x[i], target_y[i])
            if dir_y > 0 and abs(dir_y) > abs(dir_x):
                frame = frame_up[frame_index]
                character.clip_draw(frame[0], frame[1], frame[2], frame[3], x, y, frame[2] * 2, frame[3] * 2)
                frame_index = (frame_index + 1) % len(frame_up)
            elif dir_y < 0 and abs(dir_y) > abs(dir_x):
                frame = frame_down[frame_index]
                character.clip_draw(frame[0], frame[1], frame[2], frame[3], x, y, frame[2] * 2, frame[3] * 2)
                frame_index = (frame_index + 1) % len(frame_down)
            elif dir_x > 0 and abs(dir_y) < abs(dir_x):
                frame = frame_right[frame_index]
                character.clip_draw(frame[0], frame[1], frame[2], frame[3], x, y, frame[2] * 2, frame[3] * 2)
                frame_index = (frame_index + 1) % len(frame_right)
            elif dir_x < 0 and abs(dir_y) < abs(dir_x):
                frame = frame_left[frame_index]
                character.clip_draw(frame[0], frame[1], frame[2], frame[3], x, y, frame[2] * 2, frame[3] * 2)
                frame_index = (frame_index + 1) % len(frame_left)
            
            delay(0.01)  
            update_canvas()
        del target_x[0], target_y[0]
    else:
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        character.clip_draw(11, 287 - 68, 46, 50, x, y, 92, 100)
        hand.draw(mouse_x, mouse_y)
        
        update_canvas()
close_canvas()
