import pyautogui 
from PIL import Image, ImageGrab 
import time

def hit(key):
   pyautogui.press(key)
   return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 340):
        for j in range(300, 470):
            if data[i, j] < 100:
                hit('up')
                return
    for i in range(305, 340):
        for j in range(300, 388):
            if data[i, j] < 100:
                hit('down')
                return           
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
        
        # Draw the rectangle for cactus
        # for i in range(260, 300):
        #     for j in range(393, 470):
        #         data[i, j] = 0
        
        # # Draw the rectangle for birds
        # for i in range(250, 300):
        #     for j in range(300, 388):
        #         data[i, j] = 171
        # for i in range(200, 220):
        #     for j in range(393, 470):
        #         data[i, j] = 0        

        # image.show()
        # break
      

