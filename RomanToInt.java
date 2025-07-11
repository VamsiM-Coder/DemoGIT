import java.util.*;
public class RomanToInt {
    public static void main(String args[]) {
        Scanner cs = new Scanner(System.in);

        String s = cs.next();
        int res = 0;

        Map<Character,Integer> map = new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);


        int n = s.length();

        int st = map.get(s.charAt(n-1));

        res += st;

        for(int i = n - 2; i >= 0; i--) {
            int curr = map.get(s.charAt(i));

            if(curr >= st) {
                res += curr;
            }
            else {
                res -= curr;
            }
        }
        System.out.println(res);


    }
}
