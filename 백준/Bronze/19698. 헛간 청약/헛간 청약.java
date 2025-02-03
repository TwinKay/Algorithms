import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,W,H,L;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        W = Integer.parseInt(token.nextToken());
        H = Integer.parseInt(token.nextToken());
        L = Integer.parseInt(token.nextToken());
        int a = W/L;
        int b = H/L;
        int c = Math.min(N,a*b);
        System.out.println(c);
    }
}