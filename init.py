import sys

sys.path.append('army/')
sys.path.append('army/soldier/')
sys.path.append('weapon/')
sys.path.append('money/')
sys.path.append('data_structure/')
sys.path.append('weapon/cold_weapon/')
sys.path.append('weapon/gunshot_weapon/')


from print_army import *
from currency import *
from interface_commands import interface_commands


interface_commands()
