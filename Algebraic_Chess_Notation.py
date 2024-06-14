import time

print("Warning: this doesn't support disambiguation")
time.sleep(2)

while True:
    move = str(input("\nEnter your chess move (in algebraic notation)\n(Please put a space at the start if it's a pawn non-capture (ex. e4)):\n"))
    symbols = len(move)
    if symbols <= 2:
        print("Invalid move. Please enter a move with more than two symbols.")
        continue

    chesspiece = ""
    movement = ""
    promotion = ""
    promote_piece = ""
    king_attack = ""

    if move[0] == "K":
        chesspiece = "King"
    elif move[0] == "Q":
        chesspiece = "Queen"
    elif move[0] == "R":
        chesspiece = "Rook"
    elif move[0] == "B":
        chesspiece = "Bishop"
    elif move[0] == "N":
        chesspiece = "Knight"
    elif move[0] in "12345678 ":
        chesspiece = "Pawn"
    else:
        print("Invalid move. Please enter a valid chess move.\n(Did you forget to put a space before a non-capture pawn move?)")
        continue

    if move[1] == "x":
        movement = "takes"
        file = move[2]
        row = move[3]
    else:
        movement = "moves to"
        file = move[1]
        row = move[2]

    if "=" in move:
        if chesspiece == "Pawn":
            promotion = " and promotes to"
            if "Q" in move:
                promote_piece = " a queen"
            elif "R" in move:
                promote_piece = " a rook"
            elif "B" in move:
                promote_piece = " a bishop"
            elif "N" in move:
                promote_piece = " a knight"
            else:
                print("Invalid promotion piece.")
                continue
        else:
            print(f"{chesspiece} can't promote!")
            continue

    if "+" in move:
        king_attack = " and does a check"
    if "#" in move:
        if "+" in move:
            print("Don't put + together with #")
            continue
        king_attack = " and checkmates!"

    print(f"{chesspiece} {movement} {file}{row}{promotion}{promote_piece}{king_attack}")
    time.sleep(2)