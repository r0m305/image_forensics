'''
Author: Romeos CyberGypsy
Date: 24/03/2020
Name: exif.py
License: (c) romeos
'''

###############################
#Extract exif data from image files
#This is essential especially when carrying out an image forensics investigation
###############################



from PIL import Image
from PIL.ExifTags import TAGS
from colorama import *
import time
from termcolor import colored
import sys

class Engine:
    def __init__(self):
        banner = '''
        ░▀█▀░█▄█░█▀█░█▀▀░█▀▀░░░█▀▀░█▀█░█▀▄░█▀▀░█▀█░█▀▀░▀█▀░█▀▀░█▀▀
        ░░█░░█░█░█▀█░█░█░█▀▀░░░█▀▀░█░█░█▀▄░█▀▀░█░█░▀▀█░░█░░█░░░▀▀█
        ░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░░░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀'''
        print(colored(banner,"yellow"))
        print(colored("       Ⓦⓡⓘⓣⓣⓔⓝ  Ⓑⓨ  Ⓡⓞⓜⓔⓞⓢ  ⒸⓨⓑⓔⓡⒼⓨⓟⓢⓨ","green"))
        print("\n")
        print("<--Extract image exif data-->")
        try:
            self.read_exif()

        except KeyboardInterrupt:
            print(f"{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.YELLOW}Exiting safely!!")
            sys.exit()


    def read_exif(self):
        choice = input(f"{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.GREEN}Would you like to save the output to a text file?(Y/n){Fore.BLUE}")
        if choice == "N" or choice == "n":
            pass

        elif choice == "Y" or choice == "y":
            file = input(f"{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.GREEN}Enter the name of the text file to save data:{Fore.YELLOW}")
            file2 = open(file+".txt","w")

        else:
            print(colored("[-] Invalid choice!!Exiting...","red"))
            time.sleep(1)
            sys.exit()

        imagename = input(f"{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.BLUE}Enter path to image to examine:{Fore.YELLOW}")
        try:
            image = Image.open(imagename)

        except Exception as e:
            print(e)

        #extract our target data
        print(f"{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.BLUE}Reading exif data ...")
        time.sleep(2)
        exif_DATA = image.getexif()
        for tag_id in exif_DATA:
            tag = TAGS.get(tag_id, tag_id)
            data = exif_DATA.get(tag_id)

            if isinstance(data, bytes):
                data = data.decode()

            print(f"{Fore.GREEN}{tag:25}:{Fore.YELLOW}{data}")
            if choice == "Y" or choice == "y":
                file2.write(f"{tag:25}:{data}\n")

        try:
            file2.close()

        except:
            pass


if __name__ == '__main__':
    obj = Engine()
