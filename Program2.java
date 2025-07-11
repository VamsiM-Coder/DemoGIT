import java.util.*;
public class Program2 {
    public static void main(String args[]) {

       Scanner sc = new Scanner(System.in);
       
       int n = sc.nextInt();

       List<Map<String,Integer>> scores= new ArrayList<>();

       int A_Score = 0;
       int B_Score = 0;
       int C_Score = 0;
       int D_Score = 0;

       for(int i = 1; i <= n; i++) {
           System.out.println("Enter Subject Name: ");
           String sub = sc.next();

           System.out.println("Enter the number of students");
           int nStud = sc.nextInt();

           Map<String,Integer> map = new HashMap<>();

           for(int j = 1; j <= nStud; j++) {
              String studName = sc.next();
              int marks = sc.nextInt();
              
              if(studName.equals("A")) A_Score += marks;
              if(studName.equals("B")) B_Score += marks;
              if(studName.equals("C")) C_Score += marks;
              if(studName.equals("D")) D_Score += marks;

              map.put(studName,marks);
           }
           scores.add(map);

       }
       System.out.println("A Student Score is: " + A_Score);
       System.out.println("B Student Score is: " + B_Score);
       System.out.println("C Student Score is: " + C_Score);
       System.out.println("D Student Score is: " + D_Score);


    }
}
