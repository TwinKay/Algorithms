import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,U,L;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        U = Integer.parseInt(token.nextToken());
        L = Integer.parseInt(token.nextToken());

        if (N >= 1000) {
            if (U >= 8000 || L >= 260) {
                System.out.println("Very Good");
            } else {
                System.out.println("Good");
            }
        } else {
            System.out.println("Bad");
        }
    }
}