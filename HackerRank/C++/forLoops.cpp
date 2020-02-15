#include <iostream>
#include <cstdio>
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
    else
    {
        if(num%2 == 0) return "even";
        else return "odd";
    }
}

int main() {
    // Complete the code.
    int start, end;
    cin >> start;
    cin >> end;
    for(int i = start; i <= end; i++)
    {
        string s = getWord(i);
        cout << s << endl;
    }

    return 0;
}
