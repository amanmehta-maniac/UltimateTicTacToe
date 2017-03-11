def minmax(self, board, block, ismax, x, y, player, depth, alpha, beta,Parentalpha,Parentbeta, allowed_boards):
    # xnew = (x % 4) * 4
    # ynew = (y % 4) * 4

    # print xnew,ynew
    if player=='x':
        nextplayer='o'
    else:
        nextplayer='x'

    if depth == 4:
        if ismax==1:
            # return 0
            d = self.evaluate_board()
            # print 'd returned is', d
            # d += (self.evaluate(block, 0, 0, player,0)) * 10
        else:
            # return 0

            d = self.evaluate_board()
            # print 'd returned is', d
            # d += (self.evaluate(block, 0, 0, nextplayer,0)) * 10

        return d

    if ismax==1:
        # print 'max payer'
        best = -10 ** 12 - 3
        allowed_cells=self.find_allowed_cells(board,[x,y])
        # print allowed_cells
        # print 'call1'
        if len(allowed_cells) is 0:
            d = self.evaluate_board()
            # print 'd returned is', d
            # d += (self.evaluate(block, 0, 0, player,0)) * 10
            return d

        for i,j in allowed_cells:
            board[i][j]=player
            # print 'update'
            self.update_heuristic(board,i,j,player)
            # board[i][j] = player
            beta = Parentbeta
            if alpha < beta:
                best = self.minmax(board, block, not ismax,i,j, nextplayer, depth + 1, -10**12-3,10**12+3,alpha,
                                       beta, allowed_boards)
                # print best
                if alpha < best:
                    alpha = best
                board[i][j]='-'

            else:
                board[i][j]='-'
                break
        return alpha
    else:
        # print 'min'
        best = 10 ** 12 + 3
        allowed_cells=self.find_allowed_cells(board,[x,y])
        if len(allowed_cells) is 0:
            d = self.evaluate_board()
            # print 'd returned is', d
            # d += (self.evaluate(block, 0, 0, nextplayer,0)) * 10
            return d

        for i,j in allowed_cells:
            board[i][j]=player
            self.update_heuristic(board,i,j,nextplayer)
            # board[i][j] = player
            alpha = Parentalpha
            if alpha < beta:
                best = self.minmax(board, block, not ismax,i,j, nextplayer, depth + 1, -10**12-3,10**12+3,alpha,
                                       beta, allowed_boards)
                # print best
                if beta > best:
                    beta = best
                board[i][j]='-'

            else:
                board[i][j]='-'
                break
        return beta
