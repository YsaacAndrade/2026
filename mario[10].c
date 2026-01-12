#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int user;

    while (true)
    {
        printf("Height: ");
        scanf("%d", &user);

        if (user <= 0)
        {
            continue;
        }
        else if (user <= 8)
        {
            break;
        }
    }

    for (int i = 0; i < user; i++)
    {
        for (int space = user - 1; space > i; space--)
        {
            printf(" ");
        }

        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }

        printf("  ");

        for (int k = -1; k < i; k++)
        {
            printf("#");
        }

        printf("\n");
    }
}
