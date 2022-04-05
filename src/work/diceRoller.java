package work;
import java.util.*;

public class diceRoller{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the sides of the die: ");
        int sides = sc.nextInt();
        System.out.println("Enter the amount of die: ");
        int num = sc.nextInt();
        int sum = 0;
        for (int i=0; i<num+1; i++){
            sum+=Math.random()*(sides)+1;   
        }
        System.out.println("Sum is: " + sum);
        sc.close();
    }
}