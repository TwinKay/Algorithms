import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer tokens;

    public static void Permu(int cnt, int[] arr, boolean[] visited, int[] save) {
        if (cnt == save.length) {
            for (int i=0; i<save.length; i++){
                sb.append(save[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i = 0; i < visited.length; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            save[cnt] = arr[i];
            Permu(cnt + 1, arr, visited, save);
            visited[i] = false;
        }
    }

    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(tokens.nextToken());
        int m = Integer.parseInt(tokens.nextToken());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }
        Permu(0, arr, new boolean[n], new int[m]);
        System.out.println(sb);
    }
}