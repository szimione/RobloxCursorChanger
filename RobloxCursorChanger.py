import os
import colorama
import time
import sys
from colorama import Back,Fore,Style
colorama.init(autoreset=True)

def main():
    if os.name != 'nt':
        print(f'{Fore.YELLOW}Warning! This is a windows os only scipt. \nYou are NOT running windows!\nThis script will exit in 10 seconds.')
        time.sleep(10)
        return
    print(fr'{Fore.LIGHTCYAN_EX} ________  ________  ___  _____ ______   ___  ________  ________   _______      ')
    time.sleep(0.1)
    print(fr'{Fore.LIGHTCYAN_EX}|\   ____\|\_____  \|\  \|\   _ \  _   \|\  \|\   __  \|\   ___  \|\  ___ \     ')
    time.sleep(0.1)
    print(fr'{Fore.CYAN}\ \  \___|_\|___/  /\ \  \ \  \\\__\ \  \ \  \ \  \|\  \ \  \\ \  \ \   __/|    ')
    time.sleep(0.1)
    print(fr'{Fore.CYAN} \ \_____  \   /  / /\ \  \ \  \\|__| \  \ \  \ \  \\\  \ \  \\ \  \ \  \_|/__  ')
    time.sleep(0.1)
    print(fr'{Fore.LIGHTBLUE_EX}  \|____|\  \ /  /_/__\ \  \ \  \    \ \  \ \  \ \  \\\  \ \  \\ \  \ \  \_|\ \ ')
    time.sleep(0.1)
    print(fr'{Fore.LIGHTBLUE_EX}    ____\_\  \\________\ \__\ \__\    \ \__\ \__\ \_______\ \__\\ \__\ \_______\ ')
    time.sleep(0.1)
    print(fr'{Fore.BLUE}   |\_________\|_______|\|__|\|__|     \|__|\|__|\|_______|\|__| \|__|\|_______|')
    time.sleep(0.1)
    print(fr'{Fore.BLUE}   \|_________|                                                                 ')
    time.sleep(0.1)
    print(fr'{Fore.LIGHTRED_EX} ___     _    _                                        _                           ')
    time.sleep(0.1)
    print(fr'{Fore.LIGHTRED_EX} | _ \___| |__| |_____ __  __ _  _ _ _ ___ ___ _ _   __| |_  __ _ _ _  __ _ ___ _ _ ')
    time.sleep(0.1)
    print(fr"{Fore.LIGHTRED_EX} |   / _ \ '_ \ / _ \ \ / / _| || | '_(_-</ _ \ '_| / _| ' \/ _` | ' \/ _` / -_) '_|")
    time.sleep(0.1)
    print(fr'{Fore.RED} |_|_\___/_.__/_\___/_\_\ \__|\_,_|_| /__/\___/_|   \__|_||_\__,_|_||_\__, \___|_|  ')
    time.sleep(0.1)
    print(fr'{Fore.RED}                                                                      |___/         ')
    with open("version.txt", "r") as f:
        print(f'{Fore.LIGHTYELLOW_EX}{'    '*15}{f.read()}')


    do_remove_files = input('Remove empty version folders? (Y/N): ').lower()
    os.chdir(os.path.expandvars(r'%localappdata%\Roblox\Versions'))
    folders = [name for name in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), name))]
    print(f'{Fore.CYAN}Found {len(folders)} folders')
    for folder in folders:
        print(f'{Fore.CYAN}Checking for roblox files in {folder}')
        os.chdir(os.path.expandvars(folder))
        things_in_path = os.listdir()
        if 'content' in things_in_path:
            if 'StudioFonts' in os.listdir():
                os.chdir(os.path.expandvars(r'..'))
                print(f'{Fore.RED}  Ignoring Roblox Studio in {folder}...')
            else:
                print(f'{Fore.GREEN}Found roblox files in {os.getcwd()}')
                os.chdir(os.path.expandvars(r'content\textures'))
                os.system(r"xcopy ArrowCursor.png Cursors\KeyboardMouse\\ /Y >nul")
                os.system(r"xcopy ArrowFarCursor.png Cursors\KeyboardMouse\\ /Y >nul")
                print(f'{Fore.GREEN}    Successfully replaced cursor texture!')
                os.system('pause')
                sys.exit()
        else:
            os.chdir(os.path.expandvars(r'..'))
            print(f'{Fore.RED}  No roblox files found in {folder}')
            if do_remove_files == 'y':
                print(f'{Fore.BLUE}     Removing empty version folder {folder}')
                os.system('rmdir /s/q ' + folder)
        time.sleep(0.5)
            

if __name__ == '__main__':
    main()
    os.system('pause')