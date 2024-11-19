import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            if (a==1){
                sb.append(a).append(" ").append(b).append("\n").append(b).append("\n");
            }else{
                sb.append(a).append(" ").append(b).append("\n").append(b+(b-2)*(a-1)).append("\n");
            }
        }
        System.out.println(sb);
    }
}