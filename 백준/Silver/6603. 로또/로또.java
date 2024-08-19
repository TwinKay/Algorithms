import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int[] arr;

    public static void main(String[] args) throws IOException {
        while (true){
            token = new StringTokenizer(input.readLine());
            int r = Integer.parseInt(token.nextToken());
            if (r==0) break;
            arr = new int[r];
            for (int i=0; i<r; i++){
                arr[i] = Integer.parseInt(token.nextToken());
            }
            Comb(0, 0, new int[6]);
            sb.append("\n");
        }
        System.out.println(sb);
    }

    public static void Comb(int cnt, int n, int[] save){
        if(cnt==6){
            for (int i=0; i<6; i++){
                sb.append(save[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i=n; i<arr.length; i++){
            save[cnt] = arr[i];
            Comb(cnt+1, i+1, save);
        }
    }
}