package RSS_Work.Projects;
import java.util.*;

public class decBinConvert {
    public static void main(String[] args){
        int choice;
        int inp;
        int i = 0;
        int n = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("Type 1 to convert decimal to binary, or type 2 to convert binary to decimal");
        choice=sc.nextInt();
        if(choice==1){
            //Convert dec to bin
            System.out.println("Enter a number");
            inp=sc.nextInt();
            int[] binaryNum = {inp};
            while(n>0){
            binaryNum[i]=n%2;
            n=n/2;
            i++;           
            }
            for (int j = i-1; j>= 0; j--){
                System.out.print(binaryNum[j]);
            }
        }
        else if(choice==2){
            //Convert bin to dec
            System.out.println("Enter a number");
            inp=sc.nextInt();
            int remainder, decimal = 0, base = 1;
		
            while(choice > 0)
            {
                remainder = choice % 10;
                decimal = decimal + (remainder * base);
                choice = choice / 10;
                base = base * 2;
            }
            System.out.print("You entered " + base + " in binary");
        }
        else{
            System.out.print("Run the code again, this time type in 1 or 2");
        }
        sc.close();
    }
}
