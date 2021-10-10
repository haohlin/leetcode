def backtrack(line_loc, ball_loc):
    if not ball_loc:
        lineup.append(line_loc.copy())
        return
    for i in range(len(ball_loc)):
        if i >= 1 and ball_loc[i - 1] == ball_loc[i]:
            continue
        b = ball_loc.pop(i)
        line_loc.append(b)
        if isLegal(line_loc):
            backtrack(line_loc, ball_loc)
        ball_loc.insert(i, b)
        line_loc.pop(-1)
    return

def isLegal(line_loc):
    for i in range(1, len(line_loc)):
        if line_loc[i] == line_loc[i - 1]:
            return False
    return True


input_lists = list()
while True:
    try:
        l = input().split()
        l = list(map(int, l))
        l = ['P'] * l[0] + ['Q'] * l[1] + ['R'] * l[2]
        input_lists.append(l)
    except:
        break
for balls in input_lists:
    lineup = list()
    line = list()
    backtrack(line, balls)
    print(len(lineup))