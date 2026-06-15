class myObject{
    int leftPar;
    int rightPar;
    String pattern;

    myObject(String p, int numLeft, int numRight){
        this.pattern = p;
        this.leftPar = numLeft;
        this.rightPar = numRight;
    }

    public boolean shouldPrune(myObject o, int n){
        return o.leftPar > n || o.rightPar > n || o.rightPar > o.leftPar;
    }
}

public class Solution {
    public List<String> generateParenthesis(int n) {
        /*
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
         */

        List<String> res = new ArrayList<>();
        Stack<myObject> possibilities = new Stack<>();
        possibilities.push(new myObject("", 0,0));
        while(!possibilities.isEmpty()){
            myObject curr = possibilities.pop();
            if(curr.shouldPrune(curr, n)) continue;
            if(curr.pattern.length() == 2*n){
                res.add(curr.pattern);
                continue;
            }
            possibilities.add(new myObject(curr.pattern + "(",curr.leftPar+1, curr.rightPar));
            possibilities.add(new myObject(curr.pattern + ")",curr.leftPar, curr.rightPar+1));
        }
        return res;
    }
}


