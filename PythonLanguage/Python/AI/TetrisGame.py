import pygame, random
pygame.init()

WIDTH, HEIGHT = 300, 700
BLOCK = 30
COLS, ROWS = WIDTH // BLOCK, 600 // BLOCK

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mobile Tetris")

BLACK=(0,0,0); GRAY=(50,50,50); WHITE=(255,255,255)
COLORS=[(0,255,255),(255,165,0),(0,0,255),(255,255,0),(0,255,0),(160,32,240),(255,0,0)]
SHAPES=[[[1,1,1,1]],[[1,0,0],[1,1,1]],[[0,0,1],[1,1,1]],[[1,1],[1,1]],
        [[0,1,1],[1,1,0]],[[0,1,0],[1,1,1]],[[1,1,0],[0,1,1]]]

grid=[[BLACK for _ in range(COLS)] for _ in range(ROWS)]
font=pygame.font.SysFont("Arial",24)

score=0; game_over=False

def new_piece():
    return {"shape":random.choice(SHAPES),"color":random.choice(COLORS),"x":COLS//2-2,"y":0}

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(screen,grid[y][x],(x*BLOCK,y*BLOCK,BLOCK,BLOCK))
            pygame.draw.rect(screen,GRAY,(x*BLOCK,y*BLOCK,BLOCK,BLOCK),1)

def valid(p,dx=0,dy=0):
    for y,row in enumerate(p["shape"]):
        for x,c in enumerate(row):
            if c:
                nx,ny=p["x"]+x+dx,p["y"]+y+dy
                if nx<0 or nx>=COLS or ny>=ROWS: return False
                if ny>=0 and grid[ny][nx]!=BLACK: return False
    return True

def lock_piece(p):
    for y,row in enumerate(p["shape"]):
        for x,c in enumerate(row):
            if c: grid[p["y"]+y][p["x"]+x]=p["color"]

def clear_lines():
    global grid,score
    new=[]; lines=0
    for r in grid:
        if BLACK not in r: lines+=1
        else: new.append(r)
    while len(new)<ROWS: new.insert(0,[BLACK]*COLS)
    grid=new; score+=lines*100

def rotate(shape): return [list(r) for r in zip(*shape[::-1])]

clock=pygame.time.Clock()
piece=new_piece(); fall=0; speed=500

# BUTTON AREAS
left_btn=pygame.Rect(10,620,60,60)
right_btn=pygame.Rect(80,620,60,60)
down_btn=pygame.Rect(150,620,60,60)
rot_btn=pygame.Rect(220,620,60,60)

running=True
while running:
    dt=clock.tick(60); fall+=dt

    if not game_over and fall>speed:
        if valid(piece,dy=1): piece["y"]+=1
        else:
            lock_piece(piece); clear_lines()
            piece=new_piece()
            if not valid(piece): game_over=True
        fall=0

    for e in pygame.event.get():
        if e.type==pygame.QUIT: running=False

        if e.type==pygame.MOUSEBUTTONDOWN and not game_over:
            if left_btn.collidepoint(e.pos) and valid(piece,dx=-1): piece["x"]-=1
            if right_btn.collidepoint(e.pos) and valid(piece,dx=1): piece["x"]+=1
            if down_btn.collidepoint(e.pos) and valid(piece,dy=1): piece["y"]+=1
            if rot_btn.collidepoint(e.pos):
                ns=rotate(piece["shape"]); old=piece["shape"]
                piece["shape"]=ns
                if not valid(piece): piece["shape"]=old

    screen.fill(BLACK)
    draw_grid()

    for y,row in enumerate(piece["shape"]):
        for x,c in enumerate(row):
            if c:
                pygame.draw.rect(screen,piece["color"],
                    ((piece["x"]+x)*BLOCK,(piece["y"]+y)*BLOCK,BLOCK,BLOCK))

    # SCORE
    screen.blit(font.render(f"Score: {score}",True,WHITE),(10,10))

    if game_over:
        screen.blit(font.render("GAME OVER",True,(255,0,0)),(70,280))

    # DRAW BUTTONS
    pygame.draw.rect(screen,(80,80,80),left_btn); screen.blit(font.render("◀",True,WHITE),(25,630))
    pygame.draw.rect(screen,(80,80,80),right_btn); screen.blit(font.render("▶",True,WHITE),(95,630))
    pygame.draw.rect(screen,(80,80,80),down_btn); screen.blit(font.render("▼",True,WHITE),(165,630))
    pygame.draw.rect(screen,(80,80,80),rot_btn); screen.blit(font.render("⟳",True,WHITE),(235,630))

    pygame.display.update()

pygame.quit()