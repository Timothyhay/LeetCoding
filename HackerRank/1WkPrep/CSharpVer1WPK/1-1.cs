// See https://ausing System.CodeDom.Compiler;
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
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<int> arr)
    {
        int posCount = 0;
        int negCount = 0;
        int zeroCount = 0;
        foreach (int e in arr)
        {
            if (e > 0)
                posCount++;
            else if (e < 0)
                negCount++;
            else
                zeroCount++;
        }
        string ansPos = ((float)posCount / arr.Count).ToString("0.000000");
        string negPos = ((float)negCount / arr.Count).ToString("0.000000");
        string zeroPos = ((float)zeroCount / arr.Count).ToString("0.000000");

        Console.Write(ansPos + '\n' + negPos + '\n' + zeroPos);

    }

}

class Solution
{
    public static void Main(string[] args)
    {
        int n = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> arr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(arrTemp => Convert.ToInt32(arrTemp)).ToList();

        Result.plusMinus(arr);
    }
}
