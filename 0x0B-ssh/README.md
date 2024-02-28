# SSH

> This project was on SSH

## Summary

I learnt about servers and where they usually live, SSH and how to create an SSH RSA key pair, how to connect to a remote host using an SSH RSA key pair and the advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-use_a_private_key](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x0B-ssh/0-use_a_private_key): A Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.
- [x] [1-create_ssh_key_pair](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x0B-ssh/1-create_ssh_key_pair): A Bash script that creates an RSA key pair.
- [x] [2-ssh_config](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x0B-ssh/2-ssh_config): SSH client configuration to:
	- Use the private key `~/.ssh/holberton`
	- Refuse to authenticate using a password
- [x] [100-puppet_ssh_config.pp](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x0B-ssh/100-puppet_ssh_config.pp): A Puppet manifest that makes changes to my servers configuration file.
