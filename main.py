from display import *
import pieces
import time

coord_x,coord_y = 0,0
selected = None

piece_coord = [['rook','knight','bishop','queen','king','bishop','knight','rook'],
               ['pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn'],
               ['','','','','','','',''],
               ['','','','','','','',''],
               ['','','','','','','',''],
               ['','','','','','','',''],
               ['wpawn','wpawn','wpawn','wpawn','wpawn','wpawn','wpawn','wpawn'],
               ['wrook','wknight','wbishop','wqueen','wking','wbishop','wknight','wrook']]

def board():
    lcd.fill(colour(0,150,0))
    for row in range(8):
        for col in range(8):
            if(row+col) % 2 == 0:
                lcd.rect(col*30,row*30,30,30,colour(240,240,200),1)
    lcd.show()

def draw(xpos,ypos,piece,c):
    y=ypos
    pieces_list = getattr(pieces,piece)
    for row in pieces_list:
        y+=1
        x=xpos
        for col in row:
           x+=1
           if col == '1':
               lcd.hline(x,y,1,c)

def update():
    try:
        lcd.fill(board())
    except:
        print("playing...")
        
    for row in range(8):
        for col in range(8):
            piece = piece_coord[row][col]
            if piece and piece[0] == 'w':  # Eğer karede bir taş varsa 
                xpos = col * 30  # x pozisyonunu hesapla
                ypos = row * 30  # y pozisyonunu hesapla
                draw(xpos, ypos, piece,colour(215,215,215))  # Taşı çiz
            if piece and piece[0] != 'w':
                xpos = col * 30  # x pozisyonunu hesapla
                ypos = row * 30  # y pozisyonunu hesapla
                draw(xpos, ypos, piece,colour(0,0,0))  # Taşı çiz
    lcd.show()

#------AÇILIŞ---------------    
chess = ["C","H","E","S","S"]
for i in range(5):
    printstring(chess[i],37+(i*30),94,3,1,0,colour(255,120,0))
    time.sleep(0.2)
time.sleep(1)
#-----------------------------
update()

while True:
    if up.value() == 0 and coord_y>0:
        update()
        coord_y-=1
        lcd.rect(coord_x*30,coord_y*30,30,30,colour(255,0,0))
        lcd.show()
        #print(coord_x,coord_y)
    elif down.value() == 0 and coord_y<7:
        update()
        coord_y+=1
        lcd.rect(coord_x*30,coord_y*30,30,30,colour(255,0,0))
        lcd.show()
        #print(coord_x,coord_y)
    elif left.value() == 0 and coord_x>0:
        update()
        coord_x-=1
        lcd.rect(coord_x*30,coord_y*30,30,30,colour(255,0,0))
        lcd.show()
        #print(coord_x,coord_y)
    elif right.value() == 0 and coord_x<7:
        update()
        coord_x+=1
        lcd.rect(coord_x*30,coord_y*30,30,30,colour(255,0,0))
        lcd.show()
        #print(coord_x,coord_y)
    elif keyA.value() == 0:
        time.sleep(0.2)
        
        if selected is None:
            selected = (coord_y,coord_x)
            
        else:
            if selected != (coord_y, coord_x):
                piece_coord[coord_y][coord_x]=piece_coord[selected[0]][selected[1]]
                piece_coord[selected[0]][selected[1]]=''
                selected=None
                update()
            
        
time.sleep(0.2)
            
            
            