// Parent process and child process are running the 
// same program, but it does not mean they are identical.
// OS allocates different data and states for these two
// processes, and the control flow of these processes
// can be different


#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
	
int main()
{
	int x = 1;
    printf("The address of x in parent process before fork is : %d\n",&x);

    pid_t retval = fork();

	if (retval == 0)
    {
        // this block will execute for the child process only
        printf("The address of x in child process after fork is : %d\n",&x);
        printf("Child has x = %d\n",x);
        x = 500;
        printf("Child has x updated = %d\n",x);
    }
		
	else
    {
        // this block will execute for the proces parent 
        // process only
        printf("The address of x in parent process after fork is : %d\n",&x);
        printf("Parent has x = %d\n",x);
        x = 100;
        printf("Parent has x updated = %d\n",x);
    }
		
    
    return 0;
}









