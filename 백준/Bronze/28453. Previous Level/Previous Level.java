import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            int a = Integer.parseInt(token.nextToken());
            if (a==300){
                sb.append(1).append(" ");
            }else if (a>=275){
                sb.append(2).append(" ");
            }else if (a>=250){
                sb.append(3).append(" ");
            }else{
                sb.append(4).append(" ");
            }
        }
        System.out.println(sb);
    }
}