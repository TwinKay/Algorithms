import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int N,P,res;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        P = Integer.parseInt(input.readLine());

        if (N<5){
            res = P;
        }else if (N<10){
            res = P-500;
        }else if (N<15){
            res = (int) Math.min(P-500,0.9*P);
        }else if (N<20){
            res = (int) Math.min(P-2000,0.9*P);
        }else{
            res = (int) Math.min(P-2000,0.75*P);
        }
        if (res>0){
            System.out.println(res);
        }else{
            System.out.println(0);
        }
    }
}