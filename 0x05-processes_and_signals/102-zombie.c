/*
 * File_Name: 102-zombie.c
 * Created: 28th June, 2023
 * Author: David James Taiye (Official0mega)
 * Size_Of_File: Undefined
 * Project_Title: sorting_algorithms
 * Status: Submitted.!
 */

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - Initializes an infinite while loop.
 *
 * Return: Always returns 0.
 *
 * Description:
 * This function creates an infinite loop using a while statement.It repeatedly
 * calls the sleep() function to pause the execution for 1 second, allowing the
 * program to continue running indefinitely until interrupted by a signal. The
 * function returns 0 to indicate successful execution.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * create_process - Creates a new process and prints the PID of the new process
 *
 * Description:
 * This function creates a new child process using the fork() system call. The
 * fork() system call creates a new process by duplicating the calling process.
 * The child process starts execution from the point where fork() was called.
 * The parent process continues execution after creating the child process. In
 * the child process, the function prints its own process ID (PID) to the
 * standard output using the getpid() function. The parent process does not
 * print anything and continues its execution.
 */
void create_process(void)
{
	int rc = fork();

	if (rc == 0)
	{
		/* Child process */
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * main - Creates 5 zombie processes.
 *
 * Return: Always returns 0.
 *
 * Description:
 * This is the main entry point of the program.It creates 5 zombie processes by
 * calling the create_process() function five times. Each process is created as
 * a child of the main process using the fork() system call. The fork() system
 * call creates a new child process by duplicating the main process. The child
 * processes created by calling create_process() print their own process IDs
 * (PIDs) to the standard output. The main process, which is the parent, does
 * not print anything. After creating the child processes, the main process
 * enters an infinite while loop by calling the infinite_while() function. The
 * infinite_while() function keep the program running indefinitely by executing
 * an infinite loop that repeatedly calls the sleep() function to pause the
 * execution for 1 second.
 */
int main(void)
{
	create_process();
	create_process();
	create_process();
	create_process();
	create_process();
	return (infinite_while());
}
