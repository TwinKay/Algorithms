import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        int res = 0;
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            if (a==136){
                res += 1000;
            }else if (a==142){
                res += 5000;
            }else if (a==148){
                res += 10000;
            }else if (a==154){
                res += 50000;
            }
        }
        System.out.println(res);
    }
}