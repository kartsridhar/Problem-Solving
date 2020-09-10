using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

/*
John has a fascination with numbers. He likes numbers that have their digits in increasing order like 149, 468, 789, etc. He does not like numbers that don't follow this rule like 543, 664, 299, etc.
Given a number N as input, find the largest number less than or equal to N which will appeal to John's liking.

Input
An integer N which is less than 1,000,000.

Output
An integer less than or equal to N, which appeals to John's peculiar rules.


For example:

If the input number is 1234 then this number already has its digits in increasing order, and hence, the output would be the same number i.e. 1234.
If the input number is 998 then this number doesn’t have its digits in increasing order and we will decrement this number by 1 in each iteration till we reach the number 789 which follows the desired order.

Input:
1234
Expected Output:
1234

Input:
998
Expected Output:
789

Input:
574
Expected Output:
569
*/

class Solution
{
    static bool IsSorted(int input)
    {
        var digits = input.ToString().ToList();
        var unique = new HashSet<char>(digits);
        if (!digits.SequenceEqual(unique))
            return false;
        else
        {
            var sortedDigits = digits.OrderBy(i => i);
            return digits.SequenceEqual(sortedDigits);
        }
    }

    static int FindLargestNumber(int input)
    {
        if (input < 10) return input;
        while (input > 9)
        {
            if (!IsSorted(input)) input -= 1;
            else return input;
        }
        return 0;
    }

    static void Main(string[] args)
    {
        int input = int.Parse(Console.ReadLine());
        int result = FindLargestNumber(input);
        Console.WriteLine(result);
    }
}
