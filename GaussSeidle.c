#include <stdio.h>
#include <math.h>
int main()
    {
    int a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3;
    float prevx=0,prevy=0,prevz=0,cx=1,cy=1,cz=1,out;
    int counter=0;
    printf("a1:");
    scanf("%i",&a1);
    printf("a2:");
    scanf("%i",&a2);
    printf("a3:");
    scanf("%i",&a3);
    printf("b1:");
    scanf("%i",&b1);
    printf("b2:");
    scanf("%i",&b2);
    printf("b3:");
    scanf("%i",&b3);
    printf("c1:");
    scanf("%i",&c1);
    printf("c2:");
    scanf("%i",&c2);
    printf("c3:");
    scanf("%i",&c3);
    printf("d1:");
    scanf("%i",&d1);
    printf("d2:");
    scanf("%i",&d2);
    printf("d3:");
    scanf("%i",&d3);

    while (1<2)
    {
        cx = (d1-b1*prevy-c1*prevz)/a1;
        cy = (d2-a2*cx-c2*prevz)/b2;
        cz = (d3-a3*cx-b3*cy)/c3;
        out = round(cx*100)/100;
        counter++;
        
        
        if (round(cx*100)/100==round(prevx*100)/100){
            break;
        }
        else
        {
            prevx = cx;
            prevy=cy;
            prevz = cz;
            printf("%f %f %f %i\n",cx,cy,cz,counter);
        }
        
    }
    printf("%f %f %f %i\n",cx,cy,cz,counter);
    int i;
    printf("0.Exit 1.Redo:");
    scanf("%i",&i);
    if (i==0)
    {
        printf("closing");
    }
    if (i==1)
    {
        main();
    }
    }
