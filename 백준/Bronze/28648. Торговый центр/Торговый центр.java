import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            min = Math.min(min, Integer.parseInt(token.nextToken())+Integer.parseInt(token.nextToken()));
        }
        System.out.println(min);
    }
}