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



class Result
{

    /*
     * Complete the 'playlist' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts INTEGER_ARRAY songs as parameter.

     https://www.tutorialspoint.com/pairs-of-songs-with-total-durations-divisible-by-60-in-python
     */

    public static long playlist(List<int> songs)
    {
        long count = 0;
        var playLists = new Dictionary<long, long>();
        foreach(var i in songs)
        {
            if(i % 60 == 0 && playLists.ContainsKey(0))
                count += playLists[int.Parse(0.ToString())];
            else if(playLists.ContainsKey(60 - (i % 60)))
                count += playLists[int.Parse((60 - (i % 60)).ToString())];
                
            if(playLists.ContainsKey(i % 60))
                playLists[i % 60] += 1;
            else
                playLists.Add(i % 60, 1);
        }
        return count;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int songsCount = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> songs = new List<int>();

        for (int i = 0; i < songsCount; i++)
        {
            int songsItem = Convert.ToInt32(Console.ReadLine().Trim());
            songs.Add(songsItem);
        }

        long result = Result.playlist(songs);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
