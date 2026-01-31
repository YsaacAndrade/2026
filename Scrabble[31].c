#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

string playerOne;
string playerTwo;

struct Pair {
    char key;
    int value;
};
struct Pair one[] = {
    {'a', 1}, {'e', 1},
    {'i', 1}, {'o', 1},
    {'u', 1}, {'d', 2},
    {'g', 2}, {'b', 3},
    {'c', 3}, {'m', 3},
    {'p', 3}, {'f', 4},
    {'h', 4}, {'v', 4},
    {'w', 4}, {'y', 4},
    {'k', 5}, {'j', 8},
    {'x', 8}, {'q', 10},
        {'z', 10}
};

int punctuationOne = 0;
int punctuationTwo = 0;


int main(void)
{
    playerOne = get_string("Player one: ");

    for (int i = 0, x = strlen(playerOne); i <= x; i++) {
        // punctuationOne += one[i].value;

        printf("%i\n", one[i].value);
    }
    printf("%i\n", punctuationOne);
    /*
        playerTwo = get_string("Player two: ");

        for (int j = 0, z = strlen(playerTwo); j <= z; j++) {
            punctuationTwo += one[j].value;
        }
        printf("%i\n", punctuationTwo);
    */
}
