#include <stdio.h>
#include <math.h>
int main()
{
    int limit;
    printf("Enter your limit:");
    scanf("%d",&limit);
    SieveofEratosthenes(limit);
}

int isPrime(int x)
{
    if (x==1)
    {
        return 0;
    }
    else if (x==2)
    {
        return 1;
    }
    
    else
    {
        int lim = sqrt(x);
        for (int i = 2; i <= lim; i++)
        {
            if (x%i==0)
            {
                return 0;
            }   
        }
        return 1;   
    }   
}

int SieveofEratosthenes(int y)
{
    int arr[y+1];
    for (int j = 2; j <=y ; j++)
    {
        arr[j] = j;
    }

    int sievelim = sqrt(y);
    for (int k = 2; k <= sievelim; k++)
    {
        if (isPrime(k))
        {
            int mul = y/k;
            for (int n = 2; n <= mul; n++)
            {
                arr[n*k] = -1;
            }           
        }    
    }
    for (int m = 2; m <= y; m++)
    {
        if (arr[m]!=-1)
        {
            printf("%d, ",arr[m]);
        }
    }    
}
