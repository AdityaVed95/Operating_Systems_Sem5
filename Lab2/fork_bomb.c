#include <unistd.h>
// do not run this on your machine 
// it will completely freeze your machine
// how to recover if you run this ?
// reboot the machine by pressing on the power button

int main()
{
   while(1) 
      fork();    
   return 0;
}