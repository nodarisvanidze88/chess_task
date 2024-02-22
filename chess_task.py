test_data = '''RbBQKBNR
pppppppp
wbwbwbwb
bwbwbwbw
wbwbwbwb
bwbwbwbw
pppppppp
RNBQKBNR'''

# wNBQKBNR
# pppppppp
# wbwbwbwb
# bwbwbwbw
# wbwbwbwb
# bwbwbwbw
# pppppppp
# RNBQKBNR


# RNwQKBNR
# pppppppp
# wbwbwbwb
# bwbwbwbw
# wbwbwbwb
# bwbwbwbw
# pppppppp
# RNBQKBNR

# RNBbKBNR
# pppppppp
# wbwbwbwb
# bwbwbwbw
# wbwbwbwb
# bwbwbwbw
# pppppppp
# RNBQKBNR

# "w" - ცარიელი თეთრი უჯრა,
# "b" - ცარიელი შავი უჯრა,
# "K" - King,
# "Q" - Queen,
# "R" - Rook,
# "B" - Bishop,
# "N" - Knight,
# "p" - Pawn.

figures = [
    {"name": "King", "symbol": "K", "qty": 2},
    {"name": "Queen", "symbol": "Q", "qty": 2},
    {"name": "Rook", "symbol": "R", "qty": 4},
    {"name": "Bishop", "symbol": "B", "qty": 4},
    {"name": "Knight", "symbol": "N", "qty": 4},
    {"name": "Pawn", "symbol": "p", "qty": 16},
]
def main():
    # board = [list(input()) for _ in range(8)]
    board = [list(i) for i in test_data.split("\n")]
    print(count_figures(board))
    print(get_data_structure(figures))
    print(compare_data(count_figures(board), get_data_structure(figures)))

def count_figures(user):
    current_figures = {}
    for i in user:
        for k in i:
            if k =="w" or k=="b":
                continue
            else:
                current_figures[k] = current_figures.get(k,0)+1
    return dict(sorted(current_figures.items(), key = lambda x: x[0]))


def get_data_structure(data):
    data_figures = {}
    for i in data:
        data_figures[i['symbol']] = i["qty"]
    return dict(sorted(data_figures.items(), key = lambda x: x[0]))

def compare_data(current, database):
    for i in database:
        for m in current:
            if i == m and database[i] != current[i]:
                for L in figures:
                    if L["symbol"] == m:
                        return L["name"]

main()
