def minimax(self,old_move, depth, max_depth, alpha, beta, isMax, p_board, p_block, flag1, flag2, best_node):
		if datetime.datetime.utcnow() - self.begin > self.timeLimit:
			return (-111,(-1,-1))
		terminal_state = p_board.find_terminal_state()
		if terminal_state[1] == 'WON' :
			if terminal_state[0] == 'x' :
				return (self.WIN_UTILITY,old_move)
			if terminal_state[0] == 'o' :
				return (-self.WIN_UTILITY,old_move)

		if depth==max_depth:
			utility = self.check_utility(p_block,p_board)
			if flag1 == 'o':
				return (-utility,old_move)
			return (utility,old_move)
		else:
			children_list = p_board.find_valid_move_cells(old_move)
			random.shuffle(children_list)
			if len(children_list) == 0:
				utility = self.check_utility(p_block,p_board)
				if flag1 == 'o':
					return (-utility,old_move)
				return (utility,old_move)
			for child in children_list:
				if isMax:
					p_board.update(old_move,child,flag1)
				else:
					p_board.update(old_move,child,flag2)
				if isMax:
					score = self.minimax (child,depth+1,max_depth,alpha,beta,False,p_board,p_block,flag1,flag2,best_node)
					if datetime.datetime.utcnow() - self.begin > self.timeLimit:
						p_board.board_status[child[0]][child[1]] = '-'
						p_board.block_status[child[0]/4][child[1]/4] = '-'
						return (-111,(-1,-1))
					if (score[0] > alpha):
						alpha = score[0]
						best_node = child
				else:
					score = self.minimax (child,depth+1,max_depth,alpha,beta,True,p_board,p_block,flag1,flag2,best_node)
					if datetime.datetime.utcnow() - self.begin > self.timeLimit:
						p_board.board_status[child[0]][child[1]] = '-'
						p_board.block_status[child[0]/4][child[1]/4] = '-'
						return (-111,(-1,-1))
					if (score[0] < beta):
						beta = score[0]
						best_node = child
				p_board.board_status[child[0]][child[1]] = '-'
				p_board.block_status[child[0]/4][child[1]/4] = '-'
				if (alpha >= beta):
					break
			if isMax:
				return (alpha, best_node)
			else:
				return(beta, best_node)