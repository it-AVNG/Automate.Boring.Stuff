# A valid board will have:
# 1. Exactly one black king and exactly one white king. 
# 2. Each player can only have at most 16 pieces, at most 8 pawns.
# 3. All pieces must be on a valid space from '1a' to '8h'; 
# 4. The piece names begin with either a 'w' or 'b' to represent white or black, 
#    followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or'king'. 
# This function should detect when a bug has resulted in an improper chess board

##Regulation: keys represents places on the board; value represents pieces
## imagine when we move to 
import pprint
#create reference dictionary
wPiece = ['wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking']
bPiece = ['bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking']
#a function to count all the of the dictionary and return a list
def sumValue(dictionary):
    sum = [0,0]
    for k,v in dictionary.items():
        if k in wPiece:
            sum[0] = sum[0] +v
        if k in bPiece:
            sum[1] = sum[1] +v
    return sum

#function to count all the piece
def countPiece(board):
  count ={}
  for piece in board.values():
      count.setdefault(piece,0)
      count[piece] = count[piece] + 1
  return count

#main function
def isValidChessBoard(board):
    check = True
    for v in board.values():
      #checkRule4
      if v[0] == 'w':
        if v not in wPiece:
          check = False
          return check
      else:
        if v not in bPiece:
          check = False
          return check

    #count pieces 
    pieceOnBoard = countPiece(board)

    #checkrule1:
    if pieceOnBoard['bking'] !=1:
      check = False
      return check
    elif pieceOnBoard['wking'] !=1:
      check = False    
         
    #checkrule2
    #count pawns
    if pieceOnBoard['bpawn'] >8:
      check = False
      return check
    elif pieceOnBoard['wpawn'] >8:
      check = False
             
    #check sum of piece
    value = sumValue(pieceOnBoard)
    if (value[0] > 16):
      check =False
      return check
    elif (value[1] > 16):
      check =False  
        
    #checkrule3
    for k in board.keys():
        if int(k[0]) >8 :
          check =False
          return check
        elif k[1] not in list(map(chr, range(97, 105))):
          check = False
  
            
    return check


#create a model valid board
modelboard = {'1a': 'wrook', '1b': 'wknight', '1c': 'wbishop' , '1d': 'wqueen',
              '1e': 'wking', '1f': 'wbishop', '1g': 'wknight' , '1h': 'wrook' ,
              '2a': 'wpawn', '2b': 'wpawn'  , '2c': 'wpawn'   , '2d': 'wpawn' ,
              '2e': 'wpawn', '2f': 'wpawn'  , '2g': 'wpawn'   , '2h': 'wpawn' ,

              '8a': 'brook', '8b': 'bknight', '8c': 'bbishop' , '8d': 'bqueen',
              '8e': 'bking', '8f': 'bbishop', '8g': 'bknight' , '8h': 'brook' ,
              '7a': 'bpawn', '7b': 'bpawn'  , '7c': 'bpawn'   , '7d': 'bpawn' ,
              '7e': 'bpawn', '7f': 'bpawn'  , '7g': 'bpawn'   , '7h': 'bpawn' }

tally = isValidChessBoard(modelboard)

pprint.pprint(tally)