import sys

sys.path.append('army/')
sys.path.append('commands/')
sys.path.append('army/soldier/')
sys.path.append('weapon/')
sys.path.append('money/')
sys.path.append('data_structure/')
sys.path.append('weapon/cold_weapon/')
sys.path.append('weapon/gunshot_weapon/')

from menu_init_command import MenuInitCommand

MenuInitCommand().execute()


