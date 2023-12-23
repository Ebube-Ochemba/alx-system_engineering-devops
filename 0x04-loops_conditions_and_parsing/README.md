# Loops, conditions and parsing

> This project was on shell loops, conditions and parsing.

## Summary

I learnt about how to create SSH keys, the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`, how to use `while`, `until` and `for loops`, how to use `if`, `else`, `elif` and `case` condition statements, how to use the `cut` command and what are files and other comparison operators, and how to use them.

## Files

> Each file contains the solution to a task in the project.

- [0-RSA_public_key.pub](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/0-RSA_public_key.pub): Create a RSA key pair.
- [1-for_best_school](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/1-for_best_school): A Bash script that displays `Best School` 10 times.
> (`for` loop)
- [2-while_best_school](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/2-while_best_school): A Bash script that displays `Best School` 10 times.
> (`while` loop)
- [3-until_best_school](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/3-until_best_school): A Bash script that displays `Best School` 10 times.
> (`until` loop)
- [4-if_9_say_hi](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/4-if_9_say_hi): A Bash script that displays `Best School` 10 times, ut for the 9th iteration, displays `Best School` and then `Hi` on a new line.
> (`while` loop and `if` statement)
- [5-4_bad_luck_8_is_your_chance](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/5-4_bad_luck_8_is_your_chance): A Bash script that loops from 1 to 10 and: 
	- displays `bad luck` for the 4th loop iteration
	- displays `good luck` for the 8th loop iteration
	- displays `Best School` for the other iterations
> (`while` loop and `if`, `elif` and `else` statements)
- [6-superstitious_numbers](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/6-superstitious_numbers): A Bash script that displays numbers from 1 to 20 and:
	- displays `4` and then `bad luck from China` for the 4th loop iteration
	- displays `9` and then `bad luck from Japan` for the 9th loop iteration
	- displays `17` and then `bad luck from Italy` for the 17th loop iteration
> (`while` loop and `case` statement)
- [7-clock](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/7-clock): A Bash script that displays the time for 12 hours and 59 minutes:
	- display hours from 0 to 12
	- display minutes from 1 to 59
> (`while` loop)
- [8-for_ls](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/8-for_ls): A Bash script that displays:
	- The content of the current directory
	- In a list format
	- Where only the part of the name after the first dash is displayed
> (`for` loop)
- [9-to_file_or_not_to_file](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/9-to_file_or_not_to_file): A Bash script that gives you information about the school file.
> (`if` and `else` statements)
- [10-fizzbuzz](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/10-fizzbuzz): A Bash script that displays numbers from 1 to 100.
	- Displays `FizzBuzz` when the number is a multiple of 3 and 5
	- Displays `Fizz` when the number is multiple of 3
	- Displays `Buzz` when the number is a multiple of 5
	- Otherwise, displays the number
	- In a list format
- [100-read_and_cut](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/100-read_and_cut): A Bash script that displays the content of the file `/etc/passwd`. It will only display:
	- username
	- user id
	- Home directory path for the user
> (`while` loop)
- [101-tell_the_story_of_passwd](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/101-tell_the_story_of_passwd): A Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS.
- [102-lets_parse_apache_logs](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/102-lets_parse_apache_logs): A Bash script that displays the visitor IP along with the HTTP status code from the [Apache log file](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/apache-access.log).
	- Format: IP HTTP_CODE
		- in a list format
		- See example
	- You must use awk
	- You are not allowed to use `while`, `for`, `until` and `cut`
- [103-dig_the-data](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x04-loops_conditions_and_parsing/103-dig_the-data): A Bash script that groups visitors by IP and HTTP status code, and displays this data. (from previous task)
	- The exact format must be:
		- OCCURENCE_NUMBER IP HTTP_CODE
		- In list format
	- Ordered from the greatest to the lowest number of occurrences
	- You must use awk
        - You are not allowed to use `while`, `for`, `until` and `cut`
