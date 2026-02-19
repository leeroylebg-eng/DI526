# Tic Tac Toe

def create_board():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def display_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print("\n")

def player_input(board, player):
    while True:
        try:
            row = int(input(f"Joueur {player}, entrez le numéro de ligne (0, 1, 2) : "))
            col = int(input(f"Joueur {player}, entrez le numéro de colonne (0, 1, 2) : "))
            if row not in range(3) or col not in range(3):
                print("Position invalide, réessayez.")
            elif board[row][col] != " ":
                print("Cette case est déjà prise, réessayez.")
            else:
                return row, col
        except ValueError:
            print("Entrée invalide, entrez un chiffre.")

def check_win(board, player):
    # Vérifier les lignes
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Vérifier les colonnes
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Vérifier les diagonales
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def play():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)
        row, col = player_input(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Le joueur {current_player} a gagné !")
            break

        if check_tie(board):
            display_board(board)
            print("Match nul ! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"

play()