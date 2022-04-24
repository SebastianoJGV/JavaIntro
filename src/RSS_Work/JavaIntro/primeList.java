package RSS_Work.JavaIntro;
import java.util.*;
public class primeList {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        boolean flag = false;
        for(int n=2; n<=num; n++){
            for (int i = 2; i <= n/2; ++i) {
                if (n % i == 0) {
                    flag = true;
            }
        }
            if (!flag){
                System.out.println(n);}
            
        }
        sc.close();
    }
}
