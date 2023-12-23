#include <stdio.h> /* printf() */
#include <unistd.h> /* fork() */
#include <stdlib.h> /* exit() */
#include <sys/types.h> /* pid_t */

int infinite_while(void);

/**
 * main - Creates 5 zombie processes.
 * Return: 0 (Success)
 */
int main(void)
{
	pid_t pid;
	int idx;

	for (idx = 0; idx < 5; idx++)
	{
		pid = fork();
		if (pid == 0) /* child process */
		{
			exit(0);
		}
		else if (pid > 0) /* parent process */
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - infinite loop
 *
 * Return: nothing
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
