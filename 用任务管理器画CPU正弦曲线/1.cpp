#include <iostream>
#include <windows.h>
#include <cmath>

#define PI 3.14
using namespace std;

int main()
{
    int starttime;
    int busytime;
    int sinval = 0;
    while(1)
    {
        //���شӲ���ϵͳ������������elapsed���ĺ�����
        starttime = GetTickCount();
        float T = 30/float(sinval %= 30);
        busytime = (int)(500 * sin(2 * PI / T)) + 500;
        sinval++;
        while(GetTickCount() - starttime < busytime)
            ;
        Sleep(1000 - busytime);
    }
    return 0;
}
