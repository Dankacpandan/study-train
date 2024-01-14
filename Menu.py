def Menu(options):
    while True:
        print('''Choose mode you want to pick:
1. Battle
2. Logistics
0. Exit
    ''')
        try:
            pick = int(input())
        except:
            print("Wrogn input, try again")
            continue
        if pick not in options:
            print("Wrogn input, try again")
            continue
        else:
            return pick