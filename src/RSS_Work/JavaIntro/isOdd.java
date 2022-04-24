package RSS_Work.JavaIntro;
import java.util.*;
public class isOdd{
    public static void main(String[] args){
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Pick a number:");
            int n = sc.nextInt();
            if (n%2==0){
                System.out.println("Is even");
            }
            else{
                System.out.print("Is odd");
            }
        }
    }
}