#include <cs50.h> // Because this code was made on VScode of CS50x Course
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// 1st verify how many args, 2nt verify what's in every one arg
int main(int argc, string argv[])
{
    if (argc == 2) // need to be exactly two args (./caser + key)
    {
        // loop to iterate char-by-char and verify if is numeric
        for (int i = 0, n = strlen(argv[1]); i <= n; i++)
        {
            if (isalpha(argv[1][i]))
            {
                printf("Usage: ./caser key\n"); // if is alpha, return an error exit
                return 1;
            }
        }
        printf("TODO\n"); // for 1/28

    }
    else
    {
        printf("Usage: ./caser key\n");
        return 1; // error and exit in case that's there anything but 2 args
    }

    return 0;
}

