#include <stdio.h> 
#include <sys/types.h> 
#include <unistd.h> 

int main() 
{
    pid_t retval;

    printf("In the parent process before the fork took place\n\n");

    retval= fork();

    // In the above code, a child process is created. fork() 
    // returns 0 in the child process and positive integer in 
    // the parent process. Here, two outputs are possible because the 
    // parent process and child process are running concurrently. 
    // So we don’t know whether the OS will first give control to 
    // the parent process or the child process.

    if (retval == 0)
    {
        // if the retval = 0 then this process is the child process
        printf("This is the child process. My pid is %d and my parent's id is %d.\n", getpid(),getppid());
        printf("Enter your number : \n");
        int x;
        scanf("%d",&x);
        printf("you inputted this number : %d\n",x);
    }
    else if (retval > 0)
    {
        printf("This is the parent process. My pid is %d and my parent's id is %d.\n", getpid(), getppid() );
        // the return value of retval = process id of the child process if the child process creation was successful
        // this return value is obtained in the parent process only.
        printf("My child process pid is : %d\n",retval);

        // for(int i=0;i<1000000;i++)
        // {
            
        // }

        printf("Enter your age : \n");
        // now use pstree command and observe the process tree
        
        int x;
        scanf("%d",&x);
        printf("Your age is : %d\n",x);
    }

    else
    {
        printf("This is parent process\n");
        printf("The creation of the child process was unsuccessful\n");
    }
    

    printf("Hello world!\n"); return 0; 
}