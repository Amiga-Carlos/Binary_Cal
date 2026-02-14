import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,400))
font = pygame.font.Font(None, 32)
# clock = pygame.time.Clock()

# input_rect = pygame.Rect(200, 150, 140, 32)
input_rect = pygame.Rect(200, 150, 140, 32)
def Calculate(Data):
    Data = Data.strip()
    print(Data)
    Temp = int(Data)
    Binaryinfo = []
    while Temp > 0:
        info = Temp % 2
        Binaryinfo.append(str(info))
        Temp = Temp // 2
    return Binaryinfo
def Bulb_Calcu (d :list):
    a =""
    for i in d:
        a+=i
    return int(a,2)


temp =""
result = ""
Binaryresult = ['0', '0', '0' ,'0','0','0','0', '0']
running = True
image_1 = pygame.image.load("lighton.png").convert_alpha()
image_2 = pygame.image.load("lightoff.png").convert_alpha()
background = pygame.image.load("WinBack.png").convert()
back = pygame.transform.scale(background,(800,400))
img_1 = pygame.transform.scale(image_1,(100,100))
img_2 = pygame.transform.scale(image_2,(100,100))
color_active = pygame.Color('blue')
color_off = pygame.Color('white')
color = color_active
color_active = (255, 255, 255)  # White
color_passive = (100, 100, 100) # Gray
active = False

pygame.display.set_caption("Bi-Calcu")
pygame.display.flip()
# acitve = False
img_width = img_1.get_width()
bulb_rect=[]
for i in range(8):
    b_rect = pygame.Rect(1+i*100,200,60,60)
    bulb_rect.append(b_rect)

while running:   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                acitve = True
                color = color_active
            else:
                acitve= False
                color = color_off
            for i in range(8):
                if bulb_rect[i].collidepoint(event.pos):
                    if Binaryresult[i] == '1':
                        Binaryresult[i] ='0'
                    else:
                        Binaryresult[i] ='1'

        if event.type == pygame.TEXTINPUT:
            result += event.text   
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if  result:
                    Binaryresult =Calculate(result)
                    temp = result
                    result = "" 
                else:
                    temp =Bulb_Calcu(Binaryresult)
                    result = str(temp)
    
                # screen.fill(back)
                
    screen.blit(back,(0,0))                      
    text_surface = font.render(result, True, (255, 255, 255))
# input_rect.w = max(100, text_surface.get_width() + 10)
    screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
    pygame.draw.rect(screen, color, input_rect, 2)
    count = 0
                
    for i in range(8):
        count +=1
        x_p = count*img_width
        y_p = 150
        print(count,x_p)
        print(i)
        if Binaryresult[i]== '1':
            screen.blit(img_1,bulb_rect[i])  
        else:
            screen.blit(img_2,bulb_rect[i]) 
        pygame.display.set_caption (f'{temp}  = {Binaryresult}')
        temp = str(temp)
        event.text = temp

    text_surface = font.render(str(temp), True, (255, 255, 255))
    pygame.display.flip()
# clock.tick(60)
                        
    
pygame.quit()

# CusData = input("Enter Customer Data in here :")

# def Calculate(Data):
#     Temp = int(Data)
#     Binaryinfo = ""
#     while Temp > 0:
#         info = Temp % 2
#         Binaryinfo = str(info)+ Binaryinfo
#         Temp = Temp // 2
#     return Binaryinfo

# print(Calculate(CusData))


