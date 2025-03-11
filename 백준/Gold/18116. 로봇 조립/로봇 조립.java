import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int MAX = 1000000;
    static int[] parent;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        parent = new int[MAX+1];
        arr = new int[MAX+1];
        for (int i = 1; i <= MAX; i++) {
            parent[i] = i;
            arr[i] = 1;
        }

        for (int t = 0; t < N; t++) {
            token = new StringTokenizer(input.readLine());
            char c = token.nextToken().charAt(0);
            if (c == 'I') {
                int a = Integer.parseInt(token.nextToken());
                int b = Integer.parseInt(token.nextToken());
                union(a, b);
            } else {
                int a = Integer.parseInt(token.nextToken());
                sb.append(arr[find(a)]).append("\n");
            }
        }
        System.out.println(sb);
    }

    public static int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]);
    }

    public static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x != y) {
            if (arr[x] < arr[y]) {
                int temp = x;
                x = y;
                y = temp;
            }
            parent[y] = x;
            arr[x] += arr[y];
        }
    }
}