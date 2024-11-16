import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int max = 0;
        String res = "";
        for (int i=0; i<7; i++){
            token = new StringTokenizer(input.readLine());
            String s = token.nextToken();
            int n = Integer.parseInt(token.nextToken());
            if (n>max){
                max = n;
                res = s;
            }
        }
        System.out.println(res);
    }
}