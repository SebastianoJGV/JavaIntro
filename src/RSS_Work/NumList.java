package RSS_Work;
import java.util.*; // Import scanner
public class NumList {
    public static void main(String[] args){
        try (Scanner sc = new Scanner(System.in)) {
			System.out.print("What shall we count to?"); 
			int n = sc.nextInt(); //Read input
			for (int i = 1; i<n+1; i++){ // For loop through to number inputted
			    if (i%2==0){ // If even
			        System.out.print(i + " ");// Print with a space
			    }
			}
		}
    }
}
