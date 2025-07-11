import java.util.*;
public class Int_Roman {
    public static void main(String args[]) {
        Scanner cs = new Scanner(System.in);

        int num = cs.nextInt();

        String res = "";

        //M :  1000 
        int q1 = num / 1000;
        num = num - q1 * 1000;
        for(int i = 1; i <= q1 ; i++) res += "M";


        //D :  500 
        int q2 = num / 500;
        num = num - q2 * 500;
        for(int i = 1; i <= q2; i++) res += "D";


        //C :  100
        int q3 = num / 100;
        num = num - q3 * 100;
        for(int i = 1; i <= q3; i++) res += "C";


        //L : 50
        int q4 = num/50;
        num = num - q4 * 50;
        for(int i = 1; i <= q4; i++) res += "L";


        //X : 10 
        int q5 = num / 10;
        num = num - q5 * 10;
        for(int i = 1; i <= q5; i++) res += "X";



        //X : 0 t0 9
        String arr[] = {"","I","II","III","IV","V","VI","VII","VIII","IX"};
        if(num > 0 && num <= 9) {
            res += arr[num];
        }

        //Result
        System.out.println(res);
 
    }
}
