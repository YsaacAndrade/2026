#include <stdbool.h>
#include <stdio.h>

int main(void)
{

    int quarter = 25;
    int dime = 10;
    int nickel = 5;
    int penny = 1;

    int coins = 0;
    int user;

    while (true)
    {
        printf("Change owed: ");
        scanf("%d", &user);


        if (user < 0)
        {
            continue;
        }
        else
        {
            break;
        }
    }

    while (user > 0)
    {
        while (user >= 25)
        {
            user = user - quarter;
            coins += 1;
            if (user < 25)
            {
                while (user >= 10)
                {
                    user = user - dime;
                    coins += 1;

                    if (user < 10)
                    {
                        while (user >= 5)
                        {
                            user = user - nickel;
                            coins += 1;

                            if (user < 5)
                            {
                                while (user >= 1)
                                {
                                    user = user - penny;
                                    coins += 1;
                                }
                            }
                        }
                    }
                }
            }
        }

        while (user >= 10)
        {
            user = user - dime;
            coins += 1;
            if (user < 10)
            {
                while (user >= 5)
                {
                    user = user - dime;
                    coins += 1;

                    if (user < 5)
                    {
                        while (user >= 1)
                        {
                            user = user - nickel;
                            coins += 1;
                        }
                    }
                }
            }
        }

        while (user >= 5)
        {
            user = user - nickel;
            coins += 1;

            if (user < 5)
            {
                while (user >= 1)
                {
                    user = user - penny;
                    coins += 1;
                }
            }
        }
        while (user >= 1)
        {
            user = user - penny;
            coins += 1;
        }

        printf("%d\n", coins);
    }

    return 0;
}
