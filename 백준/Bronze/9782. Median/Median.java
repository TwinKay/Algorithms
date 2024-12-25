import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int cnt = 1;
        while (true){
            token = new StringTokenizer(input.readLine());
            int n = Integer.parseInt(token.nextToken());
            int[] arr = new int[n+1];
            for (int i = 1; i <= n; i++){
                arr[i] = Integer.parseInt(token.nextToken());
            }
            double res;
            if (n==0) break;
            else if (n%2==1) {
                res = (double)arr[(n+1)/2];
            }else{
                int left = (n+1)/2;
                res = ((double)arr[left]+(double)arr[left+1])/2;
            }
            sb.append("Case ").append(cnt).append(": ").append(String.format("%.1f", res)).append("\n");
            cnt ++;
        }
        System.out.println(sb);
    }
}