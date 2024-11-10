import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static int A,B,C;
    public static void main(String[] args) throws IOException {
        A = Integer.parseInt(input.readLine());
        B = Integer.parseInt(input.readLine());
        C = Integer.parseInt(input.readLine());
        boolean flag = false;
        if (A+B==C){
            flag = true;
        }
        if (B+C==A){
            flag = true;
        }
        if (A+C==B){
            flag = true;
        }
        if (flag){
            System.out.println(1);
        }else{
            System.out.println(0);
        }

    }
}