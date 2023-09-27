#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
    printf("PID of exec_call.c before exec is called is  = %d\n", getpid());
    char *args[] = {"Hello", "C", "Programming", NULL};
    execv("./hello_world", args);
    printf("This line is never gonna be executed unless there is an error in execution of hello executable file");
    return 0;
}