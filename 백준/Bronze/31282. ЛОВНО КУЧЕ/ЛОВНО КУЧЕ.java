import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int N = Integer.parseInt(token.nextToken());
        int K = Integer.parseInt(token.nextToken());
        int M = Integer.parseInt(token.nextToken());
        if (N%(M-K)==0){
            System.out.println(N/(M-K));
        }else{
            System.out.println(N/(M-K)+1);
        }
    }
}
