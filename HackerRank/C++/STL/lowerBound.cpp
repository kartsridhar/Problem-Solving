#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    vector<int> arr;
    for(int i = 0; i < n; i++)
    {
        int val;
        cin >> val;
        arr.push_back(val);
    }
    int q;
    cin >> q;
    for(int i = 0; i < q; i++)
    {
        int index;
        cin >> index;
        vector<int>::iterator low = lower_bound(arr.begin(), arr.end(), index);
        if (arr[low - arr.begin()] == index)
           cout << "Yes " << (low - arr.begin()+1) << endl;
        else
           cout << "No " << (low - arr.begin()+1) << endl;
    }
    return 0;
}
