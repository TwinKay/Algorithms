import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        if (n%5 == 1){
            if (n==1){
                System.out.println(-1);
            }else{
                System.out.println(n/5+1);
            }
        } else if(n%5 == 2){
            if (n==2 || n==7){
                System.out.println(-1);
            }else{
                System.out.println(n/5+2);
            }
        } else if (n%5 == 3) {
            System.out.println(n/5+1);
        } else if (n%5 == 4){
            if (n==4){
                System.out.println(-1);
            }else{
                System.out.println(n/5+2);
            }
        } else{
            System.out.println(n/5);
        }

    }
}