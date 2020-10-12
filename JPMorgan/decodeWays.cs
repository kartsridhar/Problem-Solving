using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System;

public class Solution {
    static int NumberOfWays(string number) {
        // if there are no digits, no possible way to decode
        if(number.Length == 0) return 0;

        // Initialise dp. The dp will store the number of ways for digits 
        // up until that length.
        var dp = Enumerable.Repeat(0, number.Length + 1).ToList();
        
        // there is 1 way to decode. (base case)
        dp[0] = 1;

        // if the 0th char is not 0, then there is at least 1 way to decode
        // for length = 1
        if(number[0] != '0') dp[1] = 1;

        // Loop from the third val till the end and compute ASCII vals and update dp
        for(var i = 2; i < dp.Count; i++) {
            // if the char at i-1th pos is NOT 0, then the dp for i will be the 
            // same as i. This is essentially avoiding recomputation
            if(number[i-1] != '0') dp[i] = dp[i-1];

            // Compute ASCII val (this is essentially the cipher) for i-1 and 
            // i-2 digits. Ensure you multiply i-2 by 10 coz its a 2 digit number
            var asciiVal = (number[i-2] - '0') * 10 + (number[i-1] - '0');
            
            // Check if the value is in range, increment dp[i] by the values
            // in dp[i-2] to reuse computation
            if(asciiVal >= 10 && asciiVal <= 26) 
                dp[i] += dp[i-2];
        }
        return dp[number.Length];
    }
}