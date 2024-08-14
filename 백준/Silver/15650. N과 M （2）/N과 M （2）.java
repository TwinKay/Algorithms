import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer tokens;
    static int n;
    static int m;
    static int[] arr;

    public static void Perm(int cnt, int[] save) {
        if (cnt == save.length) {
            for (int i=0; i<save.length; i++){
                sb.append(save[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i = 0; i < n; i++) {
            if (cnt !=0){
                if (arr[i] <= save[cnt-1]){
                    continue;
                }
            }
            save[cnt] = arr[i];
            Perm(cnt + 1, save);
        }
    }

    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        n = Integer.parseInt(tokens.nextToken());
        m = Integer.parseInt(tokens.nextToken());

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }

        Perm(0, new int[m]);
        System.out.println(sb);
    }
}