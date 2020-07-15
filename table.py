def game_p(c, p):
    if c not in points:
        points[c] = p
    else:
        points[c] = points.get(c) + p

def game_c(c):
    if c not in games:
        games[c] = 1
    else:
        games[c] = games.get(c) + 1

def game_w(c):
    if c not in los:
        los[c] = 0
    else:
        los[c] = los.get(c) + 0
    if c not in win:
        win[c] = 1
    else:
        win[c] = win.get(c) + 1
    game_p(c, 3)
    if c not in eq:
        eq[c] = 0
    else:
        eq[c] = eq.get(c) + 0



def game_l(c):
    if c not in los:
        los[c] = 1
    else:
        los[c] = los.get(c) + 1

    if c not in win:
        win[c] = 0
    else:
        win[c] = win.get(c) + 0
    if c not in eq:
        eq[c] = 0
    else:
        eq[c] = eq.get(c) + 0
    game_p(c, 0)

def game_e(c):
    if c not in eq:
        eq[c] = 1
    else:
        eq[c] = eq.get(c) + 1
    if c not in eq:
        eq[c] = 0
    else:
        eq[c] = eq.get(c) + 0
    game_p(c, 1)
    if c not in win:
        win[c] = 0
    else:
        win[c] = win.get(c) + 0
    if c not in los:
        los[c] = 0
    else:
        los[c] = los.get(c) + 0





games = {}
win = {}
eq = {}
los = {}
points = {}
n = int(input())
for i in range(n):
    h,hp,g,gp = input().split(';')
    game_c(h)
    game_c(g)
    if int(hp) > int(gp):
        game_w(h)
        game_l(g)
    elif int(hp) == int(gp):
        game_e(h)
        game_e(g)

    elif int(hp) < int(gp):
        game_w(g)
        game_l(h)

for elem in games:
    print(elem, end = ':')
    print(games[elem],end = ' ')
    print(win[elem],end = ' ')
    print(eq[elem],end = ' ')
    print(los[elem],end = ' ')
    print(points[elem])
