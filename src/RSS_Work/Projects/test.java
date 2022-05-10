package RSS_Work.Projects;
import java.util.ArrayList;

public class test {
    public static void main(String[] args){
        System.out.println();
    }
    
    public static int[] arrayListToArray(ArrayList<Integer> list){
        int[] array = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            array[i] = list.get(i);
        }
        return array;
    }
}
