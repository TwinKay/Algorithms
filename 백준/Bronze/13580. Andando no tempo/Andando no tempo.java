import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int[] arr = new int[3];
        for (int i = 0; i < 3; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        int a = arr[0];
        int b = arr[1];
        int c = arr[2];
        if (a-b==0 || b-c==0 || c-a==0 ||a+b-c==0||b+c-a==0||c+a-b==0||
        a-b-c==0||b-a-c==0||c-a-b==0){
            System.out.println("S");
        }else{
            System.out.println("N");
        }

    }
}