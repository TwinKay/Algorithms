import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        int res = 0;
        for (int i = 0; i < N; i++) {
            int d = Integer.parseInt(input.readLine());
            if (d%2==1){
                res++;
            }
        }
        System.out.println(res);
    }
}