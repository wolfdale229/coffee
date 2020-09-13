#! /usr/bin/env python3
"""Coffee is a program that prints out the contents of a file on
the terminal line-by-line when taking a break"""

import sys
import os
import time
import random


def create_short_stories() -> str:
    """This function searches for a directory called
    'short stories' in the users home directory. If no
    directory with that name it creates it, else it skips
    the function"""
    filename = 'short stories'
    home = os.getenv('HOME')  # gets the home directory name
    os.chdir(home)
    try:
        os.mkdir(filename)  # if folder is not present, create the folder
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
    #  check if the folder is not empty
    if len(path) is not None:
        story = random.choice(path)  # select a file randomly
        print(story)  # name of the story
        try:
            with open(story) as f_obj:
                file = f_obj.readlines()
                for line in file:
                    line = line.strip()
                    print(line)
                    time.sleep(4)
        # exit script if keyboardinterrupt key is entered
        except KeyboardInterrupt:
            print('Coffee exiting, Bye')
        sys.exit(0)
    else:
        print('Folder is empty, add a story')


def main() -> None:
    """Main function"""
    path = create_short_stories()
    read_story(path)


if __name__ == '__main__':
    os.system('clear')  # clears the screen
    main()
