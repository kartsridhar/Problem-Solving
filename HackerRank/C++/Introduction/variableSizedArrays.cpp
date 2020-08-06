#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n, q;
    cin >> n >> q;
    vector<vector<int>> a;
    for(int i = 0; i < n; i++)
    {
        int size;
        cin >> size;
        vector<int> k;
        for(int j = 0; j < size; j++)
        {
            int val;
            cin >> val;
            k.push_back(val);
        }
        a.push_back(k);
    }
    for(int i = 0; i < q; i++)
    {
        int index, value;
        cin >> index >> value;
        cout << (a.at(index)).at(value) << endl;
    }
    return 0;
}
