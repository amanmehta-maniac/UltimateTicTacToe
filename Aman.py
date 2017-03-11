import random
class ticTacToe:
	def __init__(self):
		self.INF = 10000000000
		self.bl_ut = [0,1,8,27,10000000000]
		self.bo_ut = [0,1,8,27,10000000]

	def find_empty_cells(self,board):
		
		validCells = []
		for i in range(16):
			for j in range(16):
				if board[i][j] == '-': validCells.append([i,j])
		return validCells


	def generate_random_cells(self,board):
		
		allowedMoves = []
		for i in range(16):
			for j in range(16):
				if board.board_status[i][j] == '-' and board.block_status[i/4][j/4] == '-':
					allowedMoves.append([i,j])
				
		return allowedMoves
        
	def find_valid_cells(self,board,old_move):
		
		x, y, emptyCells = (old_move[0]%4)*4, (old_move[1]%4)*4,[]
		for i in range(4):
			for j in range(4):
				if board[x+i][y+j] == '-':emptyCells.append([x+i,y+j])
		return emptyCells

	def block_occupied(self,board,old_move,player):
		
		x, y, flag = (old_move[0]%4)*4, (old_move[1]%4)*4, 0
		
		# print 'please', x, y
		for i in range(4):
			if board[x+i][y] == board[x+i][y+1] == board[x+i][y+2] == board[x+i][y+3]:
				if board[x+i][y] != '-': 
					return 1
			if board[x][y+i] == board[x+1][y+i] == board[x+2][y+i] == board[x+3][y+i]:
				if board[x][y+i] != '-': 
					return 1


		if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3]:
			if board[x][y] != '-': 
				return 1

		if board[x+3][y] == board[x+2][y+1] == board[x+1][y+2] == board[x][y+3]:
			if board[x+3][y] != '-': 
				return 1


		for i in range(4):
			for j in range(4):
				if board[x+i][y+j] == '-': flag = 1

		if flag == 0: return 1

		return 0

	def calculate_utility_board(self,board,old_move,player,block,flag):
		bo_ut = self.bo_ut
		bo_sc = 0

		temp = [[] for i in range(4)]

		for i in range(4):
			for j in range(4):
				for k in range(i,i+4):
					cx,co,bo_sc = 0,0, 0
					for l in range(j,j+4):
						cx,co = cx + board[k][l].count('x'), co + board[k][l].count('o')

					if co == 0:
						bo_sc += bo_ut[cx]
					else :
						bo_sc += 0
					if cx == 0:
						bo_sc -= bo_ut[co]
					else:
						bo_sc -= 0
					final = max(final, bo_sc)		

				for k in range(j,j+4):
					cx,co,bo_sc = 0,0, 0
					for l in range(i,i+4):
						cx,co = cx + board[l][k].count('x'), co + board[l][k].count('o')

					if co == 0:
						bo_sc += bo_ut[cx]
					else :
						bo_sc += 0
					if cx == 0:
						bo_sc -= bo_ut[co]
					else:
						bo_sc -= 0

					final = max(final, bo_sc)		

				cx = board[i][j].count('x') + board[i+1][j+1].count('x') + board[i+2][j+2].count('x') + board[i+3][j+3].count('x')		
				co = board[i][j].count('o') + board[i+1][j+1].count('o') + board[i+2][j+2].count('o') + board[i+3][j+3].count('o')		

				if co == 0:
					bo_sc += bo_ut[cx]
				else :
					bo_sc += 0
				if cx == 0:
					bo_sc -= bo_ut[co]
				else:
					bo_sc -= 0

				final = max(final, bo_sc)		
				bo_sc = 0

				cx = board[i][j+3].count('x') + board[i+1][j+2].count('x') + board[i+2][j+1].count('x') + board[i+3][j].count('x')		
				co = board[i][j+3].count('o') + board[i+1][j+2].count('o') + board[i+2][j+1].count('o') + board[i+3][j].count('o')		

				if co == 0:
					bo_sc += bo_ut[cx]
				else :
					bo_sc += 0
				if cx == 0:
					bo_sc -= bo_ut[co]
				else:
					bo_sc -= 0

				final = max(final, bo_sc)		
	

				temp[i].append(final)		

		rt = -10**12

		for i in range(4):
			ans = 0
			for j in range(4):
				ans += temp[i][j]

			x = temp[i].count(0)
			ans *= (4-x)
			rt = max(rt, ans)

		newTemp = zip(*temp)

		for i in range(4):
			ans = 0
			for j in range(4):
				ans += newTemp[i][j]

			x = newTemp[i].count(0)
			ans *= (4-x)
			rt = max(rt, ans)


		ans = (temp[0][0] + temp[1][1] + temp[2][2] + temp[3][3])
		ans *= (4 - (1 if temp[0][0] == 0 else 0) - (1 if temp[1][1] == 0 else 0) - (1 if temp[2][2] == 0 else 0) - (1 if temp[3][3] == 0 else 0))

		rt = max(rt,ans)

		ans = (temp[0][3] + temp[1][2] + temp[2][1] + temp[3][0])
		ans *= (4 - (1 if temp[0][3] == 0 else 0) - (1 if temp[2][1] == 0 else 0) - (1 if temp[1][2] == 0 else 0) - (1 if temp[3][0] == 0 else 0))

		rt = max(rt,ans)

		return rt


	def calculate_utility_block(self,board,old_move,player,block, flag):

		bl_ut = self.bl_ut
		bl_sc = 0
		#for utility of board status:
		#for rows:
		for i in range(4):
			countx = block[i].count('x');
			counto = block[i].count('o');
			if counto == 0: 
				bl_sc += bl_ut[countx];
			else:
				bl_sc += 0;
			if countx == 0: 
				bl_sc -= bl_ut[counto];
			else:
				bl_sc -= 0
		#for clm
		trArr = zip(*block)
		for i in range(4):
			countx = trArr[i].count('x');
			counto = trArr[i].count('o');
			if counto == 0: 
				bl_sc += bl_ut[countx];
			else:
				bl_sc += 0;
			if countx == 0: 
				bl_sc -= bl_ut[counto];
			else:
				bl_sc -= 0
		#for diagonal
		countx = block[0][0].count('x') + block[1][1].count('x') + block[3][3].count('x') + block[2][2].count('x')
		counto = block[0][0].count('o') + block[1][1].count('o') + block[3][3].count('o') + block[2][2].count('o')
		if counto == 0: 
			bl_sc += bl_ut[countx];
		else:
			bl_sc += 0;
		if countx == 0: 
			bl_sc -= bl_ut[counto];
		else:
			bl_sc -= 0

		countx = block[0][3].count('x') + block[1][2].count('x') + block[3][0].count('x') + block[2][1].count('x')
		counto = block[0][3].count('o') + block[1][2].count('o') + block[3][0].count('o') + block[2][1].count('o')
		if counto == 0: 
			bl_sc += bl_ut[countx];
		else:
			bl_sc += 0;
		if countx == 0: 
			bl_sc -= bl_ut[counto];
		else:
			bl_sc -= 0

		d = self.calculate_utility_board(board,old_move,player,block, flag)
		return ((bl_sc)**5) + (d**5)




		# when block is conquered



	def callMinMax(self,board,old_move,isMax,current_depth,player,Palpha,Pbeta,block,objBoard):

		validMoves = []
		if isMax: 
			best = -103
		else: 
			best = 103

		alpha = -103
		beta = 103

		x, y, flag1=(old_move[0]%4)*4,(old_move[1]%4)*4,0
	
		# if temp_status == 150 : print 'Hi',temp_status
		# if temp_status != 0: 
		# 	return temp_status

		if current_depth == 4: 
			temp_status = self.calculate_utility_block(board,old_move,player,block,0)
			return temp_status

		for i in range(4):
			for j in range(4):
				if board[x+i][y+j] == '-' and block[(x+i)/4][(y+j)/4] == '-':
					validMoves.append([x+i,y+j])

		
		if isMax:

			if len(validMoves) == 0:
				return self.calculate_utility_block(board,old_move,player,block,0)

			for i,j in validMoves:
				board[i][j] = player
				beta = Pbeta
				if alpha < beta:
					best = self.callMinMax(board,[i,j],not isMax, current_depth + 1, player, alpha, beta,block,objBoard)
					if alpha < best:
						alpha = best
					board[i][j] = '-'
				else:
					board[i][j] = '-'
					break
			return alpha

		else:

			if len(validMoves) == 0:
				return self.calculate_utility_block(board,old_move,player,block,0)

			
			for i,j in validMoves:
				if player == 'x': board[i][j] = 'o'
				else: board[i][j] = 'x'
				beta = Pbeta
				if alpha < beta:
					best = self.callMinMax(board,[i,j],not isMax, current_depth + 1, player, alpha, beta,block,objBoard)
					if beta > best:
						beta = best
					board[i][j] = '-'
				else:
					board[i][j] = '-'
					break
			return beta


		# flag1 = 0
		# gal = 10**30
		# for i in range(4):
		# 	for j in range(4):
		# 		if board[x+i][y+j] == '-' and block[(x+i)/4][(j+y)/4] == '-':
					
		# 			flag1 = 1
		# 			c1 = [x+i,y+j]

		# 			if isMax == 1:
		# 				beta = Pbeta
		# 				board[x+i][y+j] = player
		# 				if alpha < beta:
		# 					best = self.callMinMax(board,c1,not isMax, current_depth + 1, player, alpha, beta,block,objBoard)
		# 					if alpha < best:
		# 						alpha = best					
		# 				# alpha = max(best, alpha)
		# 					board[x+i][y+j] = '-'
		# 				else:
		# 					board[x+i][y+j] = '-'
		# 					gal=alpha
						


		# 			else:
		# 				if player == 'x': board[x+i][y+j] = 'o'
		# 				else: board[x+i][y+j] = 'x'
		# 				alpha = Palpha
		# 				if alpha < beta:
		# 					best = self.callMinMax(board,c1,not isMax, current_depth + 1, player, alpha, beta,block,objBoard)
		# 					if beta > best: 
		# 						beta = best
		# 					board[x+i][y+j] = '-'
		# 				else:
		# 					board[x+i][y+j] = '-'
		# 					gal=beta
						
		# if flag1 == 0:


		# 	moves=[]
		# 	moves = self.generate_random_cells(objBoard)
		# 	x=[]
		# 	for i,j in moves:
		# 			c1=[i,j]
		# 			# print check_status(board,c1,player,block)
		# 			x.append(self.check_status(board,c1,player,block,1))

		# 	if isMax: return max(x)
		# 	else: return min(x)

		# else:
		# 	return gal


	def find_valid_move_cells(self,board,old_move,player):
				

		# First move when old_move is initialised to [-1,-1]

		if old_move[0] == old_move[1] == -1:
			return 1,1
			moves = self.generate_random_cells(board)

		# Condition if the whole board is filled or the block in which the player is to move is occupied
		elif self.block_occupied(board.board_status,old_move,player) == 0:
			moves = self.find_valid_cells(board.board_status,old_move)

		# Condition when the cell is full or captured
		else:
			moves = self.generate_random_cells(board)

		# print 'hello = ', self.block_occupied(board.board_status,old_move,player)
		
		# print 'MOves = ', moves

		heuristic = -105
		MIN = -101
		MAX = 101
		isMax = 0
		for i in range(len(moves)):
			x,y = moves[i][0],moves[i][1]
			board.board_status[x][y] = player
			cell = [x,y]
			temp = self.callMinMax(board.board_status,cell,isMax,0,player,MIN,MAX,board.block_status,board)
			if temp >= heuristic:
				heuristic = temp
				f,g = x,y
			board.board_status[x][y] = '-'

		print 'Returning = ', f, g
		
		return f,g