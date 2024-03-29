# Shell, Permissions

> This project was an introduction to the Shell Permissions.

## Summary

I learnt about commands like `chmod`, `sudo`, `su`, `choan`, `chgrp` and thier usage.
Things like;
-  linux permissions and how to represent each of the three sets of permissions (_owner, group, and other_) as a single digit.
- How to create a _user_, _group_ ... and also print these informations.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-iam_betty](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/0-iam_betty): Bash script that changes the user ID to `betty`.
- [x] [1-who_am_i](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/1-who_am_i): Bash script that prints the effective userid of the current user.
- [x] [2-groups](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/2-groups): Bash script that prints all the groups the current user is a part of.
- [x] [3-new_owner](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/3-new_owner): Bash script that changes the owner of the file `hello` to the user `betty`.
- [x] [4-empty](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/4-empty): Bash script that creates an empty file called `hello`.
- [x] [5-execute](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/5-execute): Bash script that adds execute permissions to the owner of the file `hello`.
- [x] [6-multiple_permissions](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/6-multiple_permissions): Bash script that adds execute permission to the owner and the group owner, and read permission to other users, for the file `hello`.
- [x] [7-everybody](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/7-everybody): Bash script that adds execution permission to the owner, the group owner and the other users, for the file `hello`.
- [x] [8-James_Bond](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/8-James_Bond): Bash script that sets the permission for the file `hello` as follows:
	- Owner - no permission at all.
	- Group - no permission at all.
	- Other users - all permissoins.
- [x] [9-John_Doe](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/9-John_Doe): Bash script that sets the mode of the file `hello` to `-rwxr-x-wx`.
- [x] [10-mirror_permissions](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/10-mirror_permissions): Bash script that sets the mode of the file `hello` the same as the file `olleh`.
- [x] [11-directories_permissions](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/11-directories_permissions): Bash script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files are not changed.
- [x] [12-directory_permissions](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/12-directory_permissions): Bash script that creates a directory `my_dir` with permissions 751 in the working directory.
- [x] [13-change_group](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/13-change_group): Bash script that changes the group owner to `school` for the file `hello`.
- [x] [100-change_owner_and_group](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/100-change_owner_and_group): Bash script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.
- [x] [101-symbolic_link_permissions](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/101-symbolic_link_permissions):  Bash script that changes the owner and the group owner of the file `_hello` to `vincent` and `staff`, respectively.
- [x] [102-if_only](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/102-if_only):  Bash script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.
- [x] [103-Star_Wars](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x01-shell_permissions/103-Star_Wars): Bash script that plays Star Wars Episode IV in the terminal.
