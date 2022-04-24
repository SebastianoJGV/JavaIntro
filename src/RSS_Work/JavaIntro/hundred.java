package RSS_Work.JavaIntro;
public class hundred{
    public static void main(String[] args){
        for(int i=1; i<=100; i=i+10){
            System.out.println();
            System.out.println("------------------------------");
            for(int n=0; n<10; n++ ){
			    System.out.print(n+i);
                if(n+i<10){
                    System.out.print(" ");
                }
                System.out.print("|");
            }
        }
    }
}