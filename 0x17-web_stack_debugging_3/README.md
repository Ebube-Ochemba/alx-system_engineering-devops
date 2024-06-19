# Web stack debugging #3

> This project about more Web stack debugging cases.

## Summary

I learnt about `tmux` and `strace` and how to use them to debug web applications.
These are the steps i took for the project.
- Start the `tmux` session: `tmux`
- List Apache Processes (parent/child): `ps aux | grep apache`
- Attach strace to "the" Apache Process: `sudo strace -p <PID>`
- Trigger the 500 Error:
  - split `tmux` into two panes: `C-b %`
  - on the new pane, use `curl` to Trigger the Error: `curl -sI 127.0.0.1`
- Analyze the `strace` Output:
  - look for error messages or failed system calls
  - in this case, `error: No such file or directory` related to a `.phpp` file, a typo
- Search for the files containing the typo error: `grep -ro "phpp" <PATH>`
```sh
root@07778635a2a2:/# grep -ro "phpp" /var/www/html            
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-settings.php:phpp
root@07778635a2a2:/#
```
- Inspect "the" file and fix the typo occurences:
  - search for the line number(s) containing the typo: `grep -n "phpp" <PATH>`
  - open the file and make the necessary correction. (from `.phpp` to `.php`)
- write puppet manifest to fix the typo error: [`0-strace_is_your_friend.pp`](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/tree/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp)

## Files

> Each file contains the solution to a task in the project.

- [x] [0-strace_is_your_friend.pp](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/tree/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp): Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
