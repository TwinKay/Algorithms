import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,A,B;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        token = new StringTokenizer(input.readLine());
        A = Integer.parseInt(token.nextToken());
        B = Integer.parseInt(token.nextToken());

        System.out.println(Math.min(N,A/2+B));
    }
}
