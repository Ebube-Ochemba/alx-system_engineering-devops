# Processes and signals

> This project was on Bash processes and signals.

## Summary

I learnt about PID's, processes, how to find a process’ PID, how to kill a process, what a signalis and the 2 signals that cannot be ignored.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-what-is-my-pid](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/0-what-is-my-pid): A Bash script that displays its own PID.
- [x] [1-list_your_processes](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/1-list_your_processes): A Bash script that displays a list of currently running processes.
	- Shows all processes, for all users, including those which might not have a TTY
	- Displays in a user-oriented format
	- Shows process hierarchy
- [x] [2-show_your_bash_pid](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/2-show_your_bash_pid): A Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process. (using previous command)
	- Cannot use `pgrep`
	- The third line of your script must be `# shellcheck disable=SC2009`
- [x] [3-show_your_bash_pid_made_easy](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/3-show_your_bash_pid_made_easy): A Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`
- [x] [4-to_infinity_and_beyond](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/4-to_infinity_and_beyond): A Bash script that displays `To infinity and beyond` indefinitely.
> (can be stopped with `ctrl+c`)
- [x] [5-dont_stop_me_now](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/5-dont_stop_me_now): A Bash script that stops [`4-to_infinity_and_beyond`](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/4-to_infinity_and_beyond) process.
> (must use `kill`)
- [x] [6-stop_me_if_you_can](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/6-stop_me_if_you_can): A Bash script that stops [`4-to_infinity_and_beyond`](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/4-to_infinity_and_beyond) process.
> (cannot use `kill` or `killall`)
- [x] [7-highlander](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/7-highlander): A Bash script that displays:
	- `To infinity and beyond` indefinitely
	- With a `sleep 2` in between each iteration
	- `I am invincible!!!` when receiving a `SIGTERM` signal
> ([`67-stop_me_if_you_can`](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/67-stop_me_if_you_can) kills [`7-highlander`](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/7-highlander))
- [x] [8-beheaded_process](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/8-beheaded_process): A Bash script that kills the process [`7-highlander`](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/7-highlander).
- [x] [100-process_and_pid_file](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/100-process_and_pid_file): A Bash script that:
	- Creates the file `/var/run/myscript.pid` containing its PID
	- Displays `To infinity and beyond` indefinitely
	- Displays `I hate the kill command` when receiving a `SIGTERM` signal
	- Displays `Y U no love me?!` when receiving a `SIGINT` signal
	- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a `SIGQUIT` or `SIGTERM` signal
- [x] [101-manage_my_process](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/101-manage_my_process): There are two steps:
I. Write a [`manage_my_process`](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/manage_my_process) Bash script that:
	- Indefinitely writes `I am alive!` to the file `/tmp/my_process`
	- In between every `I am alive!` message, the program should pause for 2 seconds
II. Write Bash (init) script `101-manage_my_process` that manages [`manage_my_process`](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/manage_my_process).
> (check task page for requirements)
- [x] [102-zombie.c](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/102-zombie.c): A C program that creates 5 zombie processes.
