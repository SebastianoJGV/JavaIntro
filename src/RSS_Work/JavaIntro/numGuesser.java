package RSS_Work.JavaIntro;
import java.util.*;
public class numGuesser {
    public static void main(String[] args){
        int target=0; target+=Math.random()*(101);
        Scanner sc = new Scanner(System.in);
        boolean hasGuessed=false;
        int guess=0;
        do{
            System.out.println("Make a guess");
            guess = sc.nextInt();
            if (guess<target){
                System.out.println("The target is greater than " + guess);
            }
            if (guess>target){
                System.out.println("The target is smaller than " + guess);
            }
            if (guess==target){
                System.out.println("Congratulations! You guessed " + target + " which is what the computer randomized!");
                hasGuessed=true;
            }
        }while(hasGuessed==false);
        sc.close();
    }
}
