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
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static string timeConversion(string s)
    {
        string rawtime = s.Substring(0, 8);
        string flag = s.Substring(8, 1);
        string[] time = rawtime.Split(':');
        int hr = int.Parse(time[0]);
        if (flag == "A")
        {
            if (hr == 12)
            {
                time[0] = "00";
                return string.Join(":", time).ToString();
            }
            Console.WriteLine(rawtime);
            return rawtime;
        }
        else
        {
            if (hr == 12)
            {
                return string.Join(":", time).ToString();
            }
            
            hr += 12;
            time[0] = hr.ToString();
            Console.WriteLine(string.Join(":", time).ToString());
            return string.Join(":", time).ToString();
        }

    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        string result = Result.timeConversion(s);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
