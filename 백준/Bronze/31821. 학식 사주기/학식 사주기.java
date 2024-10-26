import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int N,M;
    static int[] menu;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        menu = new int[N+1];
        for (int i = 1; i <= N; i++) {
            menu[i] = Integer.parseInt(input.readLine());
        }
        int res = 0;
        M = Integer.parseInt(input.readLine());
        for (int i = 0; i < M; i++) {
            res += menu[Integer.parseInt(input.readLine())];
        }
        System.out.println(res);
    }
}