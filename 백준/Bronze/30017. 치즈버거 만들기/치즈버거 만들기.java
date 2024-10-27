import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(input.readLine());

        int A = Integer.parseInt(token.nextToken());
        int B = Integer.parseInt(token.nextToken());

        if (A == B + 1) {
            System.out.println(A + B);
        } else if (A > B + 1) {
            System.out.println(B * 2 + 1);
        } else {
            System.out.println(A * 2 - 1);
        }
    }
}