#! /usr/bin/env python3
"""Coffee is a program that prints out the contents of a file on 
the terminal line-by-line when taking a break"""

import sys
import os
import time
import random

def create_shortStories() -> str:
    """This function searches for a directory called
    'short stories' in the users home directory. If no
    directory with that name it creates it, else it skips
    the function"""
    filename = 'short stories'
    home = os.getenv('HOME')
    os.chdir(home)
    try :
        os.mkdir(filename)
    except FileExistsError:
        pass
    path = os.path.join(home, filename)
    return path

def read_story(path) -> None:
    """Randomly selects a story from the 'short stories'
    directory and display's it's content pausing for 3 seconds.
    If no story available it exits the program"""
    path = os.chdir(path)
    path = os.listdir(path)
    if len(path) is not 0:
        story = random.choice(path)
        print(story)
        try:
            with open(story) as f_obj:
                file = f_obj.readlines()
                for line in file:
                    line = line.strip()
                    print(line)
                    time.sleep(4)
        except KeyboardInterrupt:
            print('Coffee exiting, Bye')
        sys.exit(0)
    else:
        print('Folder is empty, add a story')

def main() -> None:
    """Main function"""
    path = create_shortStories()
    read_story(path)

if __name__ == '__main__':
    os.system('clear') # clears the screen
    main()
