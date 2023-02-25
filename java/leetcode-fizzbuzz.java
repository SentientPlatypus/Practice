import java.util.ArrayList;

class Solution {
    public List<String> fizzBuzz(int n) {
        ArrayList<String> r = new ArrayList();
        if (n == 1) {
            r.add("1");
            return r;
        }
        List<String> prev = fizzBuzz(n - 1);
        if (n % 3 == 0 && n % 5 == 0) {
            prev.add("FizzBuzz");
        }
        else if (n % 3 == 0) {
            prev.add("Fizz");
        }
        else if (n % 5 == 0) {
            prev.add("Buzz");
        }
        else {
            prev.add("" + n);
        }
        return prev;
    }
}