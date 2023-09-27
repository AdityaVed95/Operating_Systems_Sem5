#include <stdio.h> 
#include <sys/types.h> 
#include <unistd.h> 

int main() 
{ 
    char ch; 
    int val =fork(); 
    if(val <0) 
    { 
        printf("\nCreation of a child process was unsuccessful.\n"); 
    }

    // child process because return value zero 
    else if (val == 0) 
    { 
        printf("\nHello from Child!\n"); 
        printf("Process ID: %d\n",getpid()); 
        printf("Parent Process ID: %d\n",getppid()); 
        FILE *fp; fp = fopen("my_file", "r");

        if (fp == NULL) 
        { 
            perror("\nError while opening the file.\n"); 
        } 
        printf("\nThe contents of my_file are:\n"); 
        
        while((ch = fgetc(fp)) != EOF) 
            printf("%c", ch); 
        
        fclose(fp); 
            
    }

// parent process because return value non-zero. 

    else 
    { 
        
        printf("\nHello from Parent!\n"); 
        printf("Process ID: %d\n",getpid()); 
        printf("Parent Process ID: %d\n",getppid()); 
        printf("Process ID of child process %d\n",val); 
    } 
        
    return 0; 
}