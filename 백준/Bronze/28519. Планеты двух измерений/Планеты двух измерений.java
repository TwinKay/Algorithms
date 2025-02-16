import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int a = Integer.parseInt(token.nextToken());
        int b = Integer.parseInt(token.nextToken());
        if (a==b) {
            System.out.println(a+b);
        } else if (a+1>b) {
            System.out.println(b*2+1);
        } else if (a<b+1) {
            System.out.println(a*2+1);
        } else{
            System.out.println(a+b);
        }
    }
}