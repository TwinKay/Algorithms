import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int a,b,c,d,N;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        a = Integer.parseInt(token.nextToken());
        b = Integer.parseInt(token.nextToken());
        c = Integer.parseInt(token.nextToken());
        d = Integer.parseInt(token.nextToken());
        N = Integer.parseInt(token.nextToken());
        int res = N*4-(a+b+c+d);
        if (res<0){
            System.out.println(0);
        }else {
            System.out.println(res);
        }
    }
}
