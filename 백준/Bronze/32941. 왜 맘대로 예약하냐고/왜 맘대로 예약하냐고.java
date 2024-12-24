import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int T = Integer.parseInt(token.nextToken());
        int X = Integer.parseInt(token.nextToken());
        int N = Integer.parseInt(input.readLine());
        int cnt = 0;
        flag:
        for (int i = 0; i < N; i++) {
            int M = Integer.parseInt(input.readLine());
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < M; j++) {
                int a = Integer.parseInt(token.nextToken());
                if (a==X){
                    cnt++;
                    break;
                }else if (a>X){
                    break flag;
                }
            }
        }
        if (cnt==N){
            System.out.println("YES");
        }else {
            System.out.println("NO");
        }
    }
}