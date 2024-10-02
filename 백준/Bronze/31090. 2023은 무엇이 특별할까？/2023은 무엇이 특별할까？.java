import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int T,N;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t=0; t<T; t++){
            N = Integer.parseInt(input.readLine());
            int mod = N%100;
            N++;
            if (N%mod==0){
                System.out.println("Good");
            }else {
                System.out.println("Bye");
            }
        }
    }
}