#include <bits/stdc++.h>

using namespace std;

string getWord(int num)
{
    if(num == 1) return "one";
    else if(num == 2) return "two";
    else if(num == 3) return "three";
    else if(num == 4) return "four";
    else if(num == 5) return "five";
    else if(num == 6) return "six";
    else if(num == 7) return "seven";
    else if(num == 8) return "eight";
    else if(num == 9) return "nine";
    else return "Greater than 9";
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    string s = getWord(n);
    cout << s << endl;

    return 0;
}
