import org.w3c.dom.ls.LSOutput;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        int min = Integer.MAX_VALUE;
        int[] res = new int[2];
        for (int t = 1; t <= T; t++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            if (b<min){
                min = b;
                res[0] = a;
                res[1] = b;
            }
        }
        sb.append(res[0]).append(" ").append(res[1]);
        System.out.println(sb);
    }
}