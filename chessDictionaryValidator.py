chessBoard = {'1h': 'bking', '6c': 'wqueen',
'2g': 'bbishop', '5h': 'bqueen', '9e': 'wking'}

chessPieces = ['wpawn', 'bpawn', 'wknight', 'bknight', 'wbishop', 'bbishop', 'wrook', 'brook', 'wqueen', 'bqueen', 'wking', 'bking']
whitePieces = ['wpawn', 'wknight','wbishop', 'wrook', 'wqueen', 'wking']
blackPieces = ['bpawn', 'bknight','bbishop', 'brook', 'bqueen', 'bking']
validSpaces = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h',
               '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
               '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
               '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
               '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h',
               '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
               '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',
               '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h',]

def isValidChessBoard(chessBoard):
    if 'bking' not in chessBoard.values():
        return False
    if 'wking' not in chessBoard.values():
        return False
    numWhite = 0
    numBlack = 0
    numWhitePawns = 0
    numBlackPawns = 0
    for v in chessBoard.values():
        if v not in chessPieces:
            return False
    for v in chessBoard.values():
        if v in whitePieces:
            numWhite += 1
        if v in blackPieces:
            numBlack += 1
    if numWhite > 16 or numBlack > 16:
        return False
    for v in chessBoard.values():
        if v == 'wpawn':
            numWhitePawns += 1
        if v == 'bpawn':
            numBlackPawns += 1
    if numWhitePawns > 8 or numBlackPawns > 8:
        return False
    for k in chessBoard.keys():
        if k not in validSpaces:
            return False
    
        



    

print(isValidChessBoard(chessBoard))