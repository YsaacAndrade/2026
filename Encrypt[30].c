#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

char number = 0;
char cipher[1000000];
int letter;
int all = 0;
int leftover = -1;
int calc = 0;

// 1st verify how many args, 2st verify what's in every one arg
int main(int argc, string argv[])
{
    if (argc == 2) // need to be exactly two args (./caser + key)
    {
        // loop to iterate char-by-char and verify if which one is numeric
        for (int i = 0, n = strlen(argv[1]); i <= n; i++)
        {
            if (isalpha(argv[1][i]))
            {
                printf("Usage: ./caser key\n"); // if is alpha, return an error exit
                return 1;
            }
            else
            {
                if (argv[1][i] != '\0')
                {
                    number = atoi(argv[1]);
                    all = atoi(argv[1]);
                }
            }
        }
        string plaintext = get_string("plaintext:  "); // Receive the text to be encrypted

        for (int j = 0, x = strlen(plaintext); j <= x; j++) // verify if some char != letters
        {
            if (isdigit(plaintext[j]))
            {
                printf("ciphertext: %s\n", plaintext); // if was, so, just don't encrypt this
                return 1;
            }
        }

        for (int k = 0, z = strlen(plaintext); k <= z; k++)
        {
            if (isalpha(plaintext[k]))
            {
                for (int a = 0; a <= number; a++)
                {
                    if (plaintext[k] >= 122)
                    {
                        plaintext[k] = 97;
                        calc = all - leftover;
                        letter = plaintext[k] + calc;
                        leftover++;
                    }
                    else
                    {
                        letter = plaintext[k]++;
                        leftover++;
                    }
                }
                cipher[k] += letter;
            }
            else
            {
                cipher[k] += plaintext[k];
            }

        }
        printf("ciphertext: %s\n", cipher);
    }
    else
    {
        printf("Usage: ./caser key\n");
        return 1; // error and exit in case that's there anything but 2 args
    }

    return 0;
}
