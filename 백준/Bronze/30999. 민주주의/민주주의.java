import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    
    static int N,M;
    
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        int res = 0;
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            char[] chars = s.toCharArray();
            int a=0; int b=0;
            for (char c : chars) {
                if (c=='O'){
                    a++;
                }else{
                    b++;
                }
            }
            if (a>b) res++;
        }
        System.out.println(res);
    }
}