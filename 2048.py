
import random
import pygame
from pygame.locals import *
pygame.init()



def midXY(O,I):
    Xy = [O[0]/2-I[0]/2,O[1]/2-I[1]/2]
    return Xy
def locate(p,l):
	num = 0
	for I in l:
		if I == p:
			return num
		num += 1
	return False
def Gather(l):
	L = []
	r = False
	len_l = len(l)
	for i in l:
		if i == 0:
			continue
		elif i == r :
			L[-1] = i*2
			r = False
		else :
			L.append(i)
			r = i
	while len(L) < len_l:
		L.append(0)
	return L

def Position(L,p):
	l = []
	Y = len(L)
	X = len(L[0])

	# up
	if p == 0:
		for x in range(X):
			lx = []
			for y in range(Y):
				lx.append(L[y][x])
			l.append(lx)
		return l
	# left
	if p == 1:
		return L
	# right
	if p == 2:
		for y in range(Y):
			lx = []
			for x in range(X):
				lx.append(L[y][3-x])
			l.append(lx)
		return l
	# down
	if p == 3:
		for x in range(X):
			lx = []
			for y in range(Y):
				lx.append(L[3-y][x])
			l.append(lx)
		return l

def Reposition(L,p):
	l = []
	Y = len(L)
	X = len(L[0])

	# up
	if p == 0:
		for x in range(X):
			lx = []
			for y in range(Y):
				lx.append(L[y][x])
			l.append(lx)
		return l
	# left
	if p == 1:
		return L
	# right
	if p == 2:
		for y in range(Y):
			lx = []
			for x in range(X):
				lx.append(L[y][3-x])
			l.append(lx)
		return l
	# down
	if p == 3:
		for x in range(X):
			lx = []
			for y in range(Y):
				lx.append(L[y][3-x])
			l.append(lx)
		return l

def Rad_place(l):
	L = l
	z_num = 0
	z_cur = 0
	for y in range(len(L)):
		for x in range(len(L[0])):
			if L[y][x] == 0:
				z_num += 1
	if z_num == 0:
		return l
	z_pos = random.randint(0,z_num-1)
	for y in range(len(L)):
		for x in range(len(L[0])):
			if L[y][x] == 0:
				if z_cur == z_pos:
					L[y][x] = 2
					return L
				z_cur +=1
	return L

def Fall(L,p):
	global L_Default
	L_mid = [] 
	L_pre = Position(L,p)
	for i in range(len(L_pre)):
		L_mid.append(Gather(L_pre[i]))
	L_fin = Reposition(L_mid,p)
	# if L_fin == L and L_fin != L_Default:
	# 	return L_fin
	L_r = Rad_place(L_fin)
	return L_r
		
	

Game_stadus = 4

def Event_react(event):
	global L, Game_stadus
	if event.type == QUIT:
		exit()
	if Game_stadus == 0 or Game_stadus == 3 or Game_stadus == 4:
		if event.type == KEYDOWN :
			if event.key == K_s or event.key == K_DOWN:
				d = 3
			elif event.key == K_w or event.key == K_UP:
				d = 0
			elif event.key == K_a or event.key == K_LEFT:
				d = 1
			elif event.key == K_d or event.key == K_RIGHT:
				d = 2
			else :
				d = 4
			if d != 4:	
				L = Fall(L,d)
				if Game_stadus == 4:
					Game_stadus = 0
			if event.key == K_r or event.key == K_RETURN:
				Game_stadus = 2
	if Game_stadus == 1:
		if event.type == KEYDOWN :
			if event.key == K_SPACE:
				Game_stadus = 3

			if event.key == K_RETURN:
				Game_stadus = 0
				L = L_Default
	if Game_stadus == 2:
		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				Game_stadus = 0
				L = L_Default


def Detect_Game_Status():
	global Game_stadus,L_Default
	if Game_stadus == 0 or Game_stadus == 3:
		if Game_stadus == 0:
			for I in L:
				for i in I:
					if i == Winning_num:
						Game_stadus = 1
		if Fall(L,0) == L and Fall(L,1) == L and Fall(L,2) == L and Fall(L,3) == L and L != L_Default :
			Game_stadus = 2

def Refresh_screen():
	global Winning_unit,Losing_unit,L_bef
	if Game_stadus == 0 or Game_stadus == 3:
		if L != L_bef:
			issetnum = True
		else :
			issetnum = False
		for x in range(4):
			for y in range(4):		
				if issetnum == True:				
					Unit_list[x*4+y].Set_num(L[y][x])
					Unit_list[x*4+y].Set_Font(40-len(str(L[y][x]))*2)
					Unit_list[x*4+y].Set_Color(Block_color_set[1][locate(str(L[y][x]),Block_color_set[0])])
				L_bef = L

				Unit_list[x*4+y].Draw()
	if Game_stadus == 1:
		Winning_unit.Set_Font(End_text_size)
		for x in range(4):
			for y in range(4):
				Unit_list[x*4+y].Set_num(L[y][x])		
				Unit_list[x*4+y].Draw()
		Winning_unit.Draw()
	if Game_stadus == 2:
		Losing_unit.Set_Font(End_text_size)
		for x in range(4):
			for y in range(4):	
				Unit_list[x*4+y].Set_num(L[y][x])	
				Unit_list[x*4+y].Draw()
		Losing_unit.Draw()

	if Game_stadus == 4:
		Starting_unit.Set_Font(Start_text_size)		
		for x in range(4):
			for y in range(4):	
				Unit_list[x*4+y].Set_num(L[y][x])	
				Unit_list[x*4+y].Draw()
		Starting_unit.Draw()

		
Start_text_size = 30
End_text_size = 20
Unit_list = [] 
screensize = (425,425)
Title = "2048 Game"
Winning_T = ["conguations, you won, nicely done","Press enter to clear the screen, space to continue"]
Losing_T = "Game Over Press enter to restart"
Starting_T = ["2048 Game",'press wasd to start']
Text_Data = (40,(255,255,255))
Text_Font = 'Avenir.ttc'
Table_data = ((420,420),(189,173,158),5)
Unit_size = (Table_data[0][0]//4,Table_data[0][1]//4)
screen = pygame.display.set_mode((screensize[0],screensize[1]))
pygame.display.set_caption(Title)
Winning_num = 2048
Block_color_set = [['0','2','4','8','16','32','64','128','256','512','1024','2048','4096','8192','16384','32768'],
[(207,193,179),(222,207,194),(238,222,209),(232,195,184),(172,158,144),(217,193,149),(247,163,149),(227,153,0),(207,193,19),(235,215,31),(157,193,129),(207,103,179),(207,73,179),(107,103,159),(137,163,189),(157,193,89)]]

def init2048():
	global Winning_unit,Losing_unit,Starting_unit
	for x in range(4):
		for y in range(4):
			Unit_list.append(Unit((Unit_size[0]*x+Table_data[2],Unit_size[1]*y+Table_data[2]),(100,100),'0',(207,193,179)))
			Unit_list[x*4+y].Set_Font(40-len(str(L_Default[y][x]))*2)
	Winning_unit = Unit((0,0),screensize,Winning_T,False)
	Losing_unit = Unit((0,0),screensize,Losing_T,False)
	Starting_unit = Unit((0,0),screensize,Starting_T,False)

L_Default = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]
]

L = L_Default
L_bef = L

class Unit:
	def __init__(self,XY,size,num,color):
		self.__XY = XY
		if num != 0:
			self.__Num = num
		else:
			self.__Num = ''
		self.__BGColor = color
		self.__size = size
		self.__font = [40,(255,255,255),'Avenir.ttc']
		self.__shake = [1,0.8,0.85,0.9,0.95,1,1.05,1.1,1.15,1]
		self.__isshake = False
		self.__timer = len(self.__shake)-1
	def Draw(self,shake = False):
		if self.__BGColor != False:
			if self.__isshake == True :
				if self.__timer != 0:
					self.__timer -= 1
				else: 
					self.__timer = len(self.__shake)-1
					self.__isshake = False
			MidXY = midXY(self.__size,(self.__size[0]*self.__shake[self.__timer],self.__size[1]*self.__shake[self.__timer]))
			SpaceXY = (self.__XY[0]+MidXY[0],self.__XY[1]+MidXY[1])
			pygame.draw.rect(screen,self.__BGColor,(SpaceXY,(self.__size[0]*self.__shake[self.__timer],self.__size[1]*self.__shake[self.__timer])))



		if type(self.__Num) == str:
			Font = pygame.font.Font(self.__font[2],self.__font[0])
			Text = Font.render(self.__Num,True,self.__font[1])
			TextPos = midXY(self.__size,(Text.get_width(),Text.get_height()))
			screen.blit(Text,(TextPos[0]+self.__XY[0],TextPos[1]+self.__XY[1]))
		elif type(self.__Num) == list:
			t = 0
			for i in self.__Num:
				Font = pygame.font.Font(self.__font[2],self.__font[0])
				Text = Font.render(i,True,self.__font[1])
				TextPos = midXY(self.__size,(Text.get_width(),Text.get_height()*len(self.__Num)))
				TextPos[1] = TextPos[1]+Text.get_height()*t
				screen.blit(Text,(TextPos[0]+self.__XY[0],TextPos[1]+self.__XY[1]))
				t += 1
		
	def Set_num(self,N):
		if N == 0:
			self.__Num = ''
		else:			
			if str(N) != self.__Num:
				self.__isshake = True
			self.__Num = str(N)
	def Set_Font(self,F):
		self.__font[0] = F
	def Set_Color(self,F):
		self.__BGColor = F



init2048()
while True:
		for event in pygame.event.get():
			Event_react(event)
		Detect_Game_Status()
		screen.fill((189,173,158))
		Refresh_screen()
		pygame.display.update()
# Just a easter egg XD





























