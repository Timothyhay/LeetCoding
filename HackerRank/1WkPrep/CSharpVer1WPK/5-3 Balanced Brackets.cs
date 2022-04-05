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
     * Complete the 'isBalanced' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static string isBalanced(string s)
    {
            Stack<char> stack = new Stack<char>();

            for (int i = 0; i < s.Length; ++i)
            {
                char crt = s[i];
                if (crt == '(')
                {
                    stack.Push(crt);
                }
                else if (crt == '[')
                {
                    stack.Push(crt);
                }
                else if (crt == '{')
                {
                    stack.Push(crt);
                }
                else if (crt == ')')
                {
                    if (stack.Count == 0)
                    {
                       return("NO");
                    }
                    if (stack.Peek() == '(')
                    {
                        stack.Pop();
                    }
                    else
                        return("NO");
                }
                else if (crt == ']')
                {
                    if (stack.Count == 0)
                    {
                        return("NO");
                    }
                    if (stack.Peek() == '[')
                    {
                        stack.Pop();
                    }else{
                        return("NO");
                    }
                }
                else if (crt == '}')
                {
                    if (stack.Count == 0)
                    {
                       return("NO");
                    }
                    if (stack.Peek() == '{')
                    {
                        stack.Pop();
                    }
                    else
                        return("NO");
                }
                // Console.WriteLine("{"+curly+"["+square+"("+round);
            }
            if (stack.Count != 0)
                return("NO");
            else
                return("YES");
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int t = Convert.ToInt32(Console.ReadLine().Trim());

        for (int tItr = 0; tItr < t; tItr++)
        {
            string s = Console.ReadLine();

            string result = Result.isBalanced(s);

            textWriter.WriteLine(result);
        }

        textWriter.Flush();
        textWriter.Close();
    }
}
