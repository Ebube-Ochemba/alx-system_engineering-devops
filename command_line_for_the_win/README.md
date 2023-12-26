# Command line for the win

> This project was on practicing Bash skills with a command line challenge game.

## Summary

I learnt about SFTP and SFTP File Transfer. 
After completing the levels and taking screenshots, I used the following steps to use the `SFTP command-line tool` to upload the `*.png` files correctly;
1. Connect to your Remote Server (_sandbox environment_).
```sh
$ sftp <username>@<remote_server__hostname>
```
2. Navigate to the directory on your **remote server** that you want to upload the `*.png` files **to**.
```sh
$ cd </path/to/directory>
```
3. Navigate to the directory on your **local machine** that you want to upload the `*.png` files **from**.
```sh
$ lcd </path/to/directory>
```
4. Use the `put` command to upload the `*.png` files to your **remote server**. (_to verify step 3 & 4, use:_ `pwd` & `lpwd` _respectively_)
```sh
$ put </path/to/file>
```
5. Now that the files are on your **remote server**, `push` the files to GitHub and you are done.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-first_9_tasks.png](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/command_line_for_the_win/0-first_9_tasks.png): A screenshot after Completing the first 9 tasks.
- [x] [1-next_9_tasks.png](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/command_line_for_the_win/1-next_9_tasks.png): A screenshot after Completing the 9 next tasks, getting to 18 total.
- [x] [2-next_9_tasks.png](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/command_line_for_the_win/2-next_9_tasks.png): A screenshot after Completing the 9 next tasks, getting to 27 total.
