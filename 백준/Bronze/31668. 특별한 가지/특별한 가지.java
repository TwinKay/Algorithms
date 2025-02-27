import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        int M = Integer.parseInt(input.readLine());
        int K = Integer.parseInt(input.readLine());

        System.out.println(K*(M/N));


    }
}