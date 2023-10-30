# Shell, init files, variables and expansions

> This project was an introduction to init files, variables and expansions.

## Introduction

I learnt about initialization files, local, global, and reserved variables, and special parameters in the Shell.
	- How to create, update and delete shell variables.
	- The roles of the some reserved variables.
I practiced using expansions, performing arithmetic operations, and utilizing aliases.

## Files

> Each file contains the solution to a task in the project.

- [0-alias](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/0-alias): Bash script that creates an alias named `ls` with value `rm *`.
- [1-hello_you](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/1-hello_you): Bash script that prints `hello user`, where user is the current Linux user.
- [2-path](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/2-path): Bash script that adds `/action` to the `PATH`.
- [3-paths](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/3-paths): Bash script that counts the number of directories in the `PATH`.
- [4-global_variables](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/4-global_variables): Bash script that lists environment variables.
- [5-local_variables](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/5-local_variables): Bash script that lists all local variables, environment variables and functions.
- [6-create_local_variable](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/6-create_local_variable): Bash script that creates a new local variable named `BEST` with value `School`.
- [7-create_global_variable](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/7-create_global_variable): Bash script that creates a new global variable named `BEST` with value `School`.
- [8-true_knowledge](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/8-true_knowledge): Bash script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.
- [9-divide_and_rule](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/9-divide_and_rule): Bash script that prints the result of `POWER` divided by `DIVIDE`. `POWER` and `DIVIDE` are environment variables.
- [10-love_exponent_breath](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/10-love_exponent_breath): Bash script that displays the result of `BREATH` to the power of `LOVE`. `BREATH` and `LOVE` are environment variables.
- [11-binary_to_decimal](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/11-binary_to_decimal): Bash script that converts a number in base 2 stored in the environment variable `BINARY` to base 10.
- [12-combinations](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/12-combinations): Bash script that prints all possible combinations of two letters, except `oo`, as follows:
	- Letters are lower cases, from `a` to `z`.
	- One combination per line.
	- The output should be alpha ordered, starting with `aa`.
	- Does not print `oo`.
- [13-print_float](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/13-print_float): Bash script that prints a number stored in the environment variable `NUM` with two decimal places.
- [100-decimal_to_hexadecimal](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/100-decimal_to_hexadecimal): Bash script that converts a number in base 10 stored in the environment variable `DECIMAL` to base 16.
- [101-rot13](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/101-rot13): Bash script that encodes and decodes text using the rot13 encryption.
- [102-odd](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/102-odd): Bash script that prints every other line from the input, starting with the first line.

- [103-water_and_stir](https://github.com/Ebube-Ochemba/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/103-water_and_stir): Bash script that adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result.
	- `WATER` is in base `water`, `STIR` is in base `stir`, and the result is in base `bestchol`.
