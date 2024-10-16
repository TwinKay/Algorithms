import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;
    static long sum;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        sum = 1L;
        for (int i=11; i<=N; i++ ) {
            sum *= i;
        }
        System.out.println(sum*6);
    }
}