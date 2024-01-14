import Battle
import Menu
M_options=[1,2,0]
pick = Menu.Menu(M_options)
if pick == 0:
    SystemExit(0)
elif pick == 1:
    Battle.Battle()