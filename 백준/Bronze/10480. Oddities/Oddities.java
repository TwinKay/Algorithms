import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        for (int i = 0; i < N; i++) {
            int a = Integer.parseInt(input.readLine());
            sb.append(a).append(" is ");
            if (Math.abs(a)%2==0){
                sb.append("even\n");
            }else{
                sb.append("odd\n");
            }
        }
        System.out.println(sb);
    }
}