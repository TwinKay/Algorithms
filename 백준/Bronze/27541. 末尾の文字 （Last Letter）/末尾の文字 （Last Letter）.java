import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        String S = input.readLine();
        if (S.charAt(N-1)=='G') {
            System.out.println(S.substring(0,N-1));
        }else{
            sb.append(S).append('G');
            System.out.println(sb);
        }
    }
}