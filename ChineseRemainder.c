#include <stdio.h>
#include <math.h>
int main()
{
    int numeq,M=1,finb=0,flcm=1;
    printf("Number of eqns:");
    scanf("%d",&numeq);
    int arr[numeq+1];
    int arr2[numeq+1];
    int arrM[numeq+1];
    int arrXn[numeq+1];
    for (int i = 1; i <= numeq; i++)
    {
        printf("b%d:",i);
        scanf("%d",&arr[i]);
        printf("m%d:",i);
        scanf("%d",&arr2[i]);
        M = M*arr2[i];
    }
    for (int i = 1; i <= numeq; i++)
    {
        arrM[i] = M/arr2[i];
        //flcm = lcm(arrM[i],flcm);
        for (int j = 1; j <= arr2[i]; j++)
        {
            if ((arrM[i]*j)%arr2[i]==1)
            {
                finb += arr[i]*arrM[i]*j;
                printf("M%d is %d\nM%d-1 is %d\n",i,arrM[i],i,j);
                break;
            }
            
        }
        
        
    }
    //MiXi = 1 mod mi
    printf("M is %d\n",M);
    printf("finb is %d\n",finb);
    int LeastInt = finb%M;
    printf("Least +ve integer is:%d\n",LeastInt);//LCM Actually... Coming soon
}

int gcd(int x,int y)
{
    if (y%x==0)
    {
        return x;
    }
    else
    {
        int mind = 0;
        for (int k = 2; k <= fmin(x,y)/2; k++)
        {
            if (x%k==0 && y%k==0)
            {
                mind = k;
            }
        }
        return mind;
    }   
}
int lcm(int x,int y)
{
    int lcmm = x*y/gcd(x,y);
    return lcmm;
}