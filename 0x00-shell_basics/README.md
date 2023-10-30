# Shell, Basics

> This project was an introduction to the Shell.

## Introduction

I learnt about built-in commands like `cd`, `pwd`, `ls`... I learnt about the filesystem and how to navigate it.
I also learnt how to 'look around' using commands like `ls`, `less`, `file`... also, the `ln` command and its usage.
I also learnt about commands like `type`, `which`, `help`, `man`... implementing wildcards, reading man pages, creating links, setting file permissions and using keyboard shortcuts in Bash.

## Files

> Each file contains the solution to a task in the project.

- [0-current_working_directory](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory): Bash script that prints the absolute pathname of the current working directory.
- [1-listit](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/1-listit): Bash script that displays the contents list of current directory.
- [2-bring_me_home](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home): Bash script that changes the working directory to the user's home directory.
- [3-listfiles](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles): Bash script that displays current directory contents in long format.
- [4-listmorefiles](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles): Bash script that displays current directory contents, including hidden files, using long format.
- [5-listfilesdigitonly](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly): Bash script that displays current directory contents, including hidden files, as follows:
	- Long format.
	- User and group ID's displayed numerically.
- [6-firstdirectory](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/6-firstdirectory): Bash script that creates a directory named holberton in the /tmp/ directory.
- [7-movethatfile](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/7-movethatfile): Bash script that moves the file `betty` from `/tmp/` to `/tmp/my_first_directory`.
- [8-firstdelete](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/8-firstdelete): Bash script that deletes the file `betty` in `/tmp/my_first_directory`.
- [9-firstdirdeletion](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/9-firstdirdeletion): Bash script that deletes the directory `my_first_directory` in the `/tmp` directory.
- [10-back](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/10-back): Bash script that changes the working directory to the previous one.
- [11-lists](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/11-lists): Bash script that lists all files, including hidden files, in the current directory, parent of the working directory, and `/boot` directory, using long format.
- [12-file_type](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/12-file_type): Bash script that prints the type of the file named `iamafile` located in the `/tmp` directory.
- [13-symbolic_link](13-symbolic_link): Bash script that creates a symbolic link to `/bin/ls`, named `__ls__`.
- [14-copy_html](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/14-copy_html): Bash script that copies all HTML files from the current working directory to the parent of the working directory, but only those that did not exist in the parent directory or were newer than the versions in the parent working directory.
- [100-lets_move](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/100-lets_move): Bash script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.
- [101-clean_emacs](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/101-clean_emacs): Bash script that deletes all files in the current working directory that end with the character `~`.
- [102-tree](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/102-tree): Bash script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.
- [103-commas](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/103-commas): Bash script that lists all files and directories of the current directory, including hidden ones, as follows:
	- Separated by commas (`,`).
	- Directory names end with a slash (`/`).
	- Alpha-ordered, except for the directories `.` and `..` which are listed at the beginning.
	- Only digits and letters are used to sort - digits come first.
- [school.mgc](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x00-shell_basics/school): A magic file that can be used with the command `file` to detect `School` data files.
