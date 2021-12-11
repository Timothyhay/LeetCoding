class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = []

        def backtrack(idx=0, curr=[]):
            if len(curr) == len(s):
                output.append("".join(curr))
                return

            if num[idx].isdigit():
                curr.append(num[idx])
                backtrack(idx + 1, curr)
            else:
                curr.append(num[idx].upper())
                backtrack(idx + 1, curr)
                curr.pop()

                curr.append(num[idx].lower())
                backtrack(idx + 1, curr)
                curr.pop()

        backtrack()
        return output


'''
class Solution {
    /**  
            a1b2   i=0, when it's at a, since it's a letter, we have two branches: a, A
         /        \
       a1b2       A1b2 i=1 when it's at 1, we only have 1 branch which is itself
        |          |   
       a1b2       A1b2 i=2 when it's at b, we have two branches: b, B
       /  \        / \
      a1b2 a1B2  A1b2 A1B2 i=3  when it's at 2, we only have one branch.
       |    |     |     |
      a1b2 a1B2  A1b2  A1B2 i=4 = S.length(). End recursion, add permutation to ans. 
      
      During this process, we are changing the S char array itself
    */
    public List<String> letterCasePermutation(String S) {
        List<String> ans = new ArrayList<>();
        backtrack(ans, 0, S.toCharArray());
        return ans;
    }
    public void backtrack(List<String> ans, int i, char[] S){
        if(i==S.length)
            ans.add(new String(S));
        else{
            if(Character.isLetter(S[i])){ //If it's letter
                S[i] = Character.toUpperCase(S[i]);
                backtrack(ans, i+1, S); //Upper case branch
                S[i] = Character.toLowerCase(S[i]);
                backtrack(ans, i+1, S); //Lower case branch
            }
            else
                backtrack(ans, i+1, S); 
        }
    }
}
'''