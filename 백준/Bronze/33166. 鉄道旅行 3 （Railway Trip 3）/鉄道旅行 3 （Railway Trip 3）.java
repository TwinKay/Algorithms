import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int P = Integer.parseInt(token.nextToken());
        int Q = Integer.parseInt(token.nextToken());
        token = new StringTokenizer(input.readLine());
        int A = Integer.parseInt(token.nextToken());
        int B = Integer.parseInt(token.nextToken());
        int cost = Math.min(Q,P)*A + Math.max(Q-P,0)*B;
        System.out.println(cost);
    }
}