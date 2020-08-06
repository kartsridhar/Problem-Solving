#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int len;
    cin >> len;

    int arr[len];
    for(int i = 0; i < len; i++)
    {
        int num;
        cin >> num;
        arr[i] = num;
    }

    for(int i = len-1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }
    return 0;
}