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
        for (int i=1; i<=N; i++) {
            if (i%7==0 && i%11==0){
                sb.append("Wiwat!\n");
            }else if (i%7==0){
                sb.append("Hurra!\n");
            }else if (i%11==0){
                sb.append("Super!\n");
            }else{
                sb.append(i+"\n");
            }
        }
        System.out.println(sb);
    }
}