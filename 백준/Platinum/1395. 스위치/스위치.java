import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static long[] tree, lazy;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        tree = new long[N*4];
        lazy = new long[N*4];

        for (int m = 1; m <= M; m++) {
            token = new StringTokenizer(input.readLine());
            int q = Integer.parseInt(token.nextToken());
            int left = Integer.parseInt(token.nextToken());
            int right = Integer.parseInt(token.nextToken());

            if (q == 0) {
                update(1, N, 1, left, right);
            } else {
                sb.append(sum(1, N, 1, left, right)).append("\n");
            }
        }
        System.out.println(sb);
    }

    public static void propagate(int start, int end, int node) {
        if (lazy[node] != 0) {
            tree[node] = (end-start+1) - tree[node];

            if (start != end) {
                lazy[node*2] ^= 1;
                lazy[node*2+1] ^= 1;
            }
            lazy[node] = 0;
        }
    }

    public static long sum(int start, int end, int node, int left, int right) {
        propagate(start, end, node);

        if (right < start || left > end) {
            return 0;
        }
        if (left <= start && end <= right) {
            return tree[node];
        }

        int mid = (start + end) / 2;
        return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right);
    }

    public static void update(int start, int end, int node, int left, int right) {
        propagate(start, end, node);

        if (right < start || left > end) {
            return;
        }
        if (left <= start && end <= right) {
            lazy[node] ^= 1;
            propagate(start, end, node);
            return;
        }

        int mid = (start + end) / 2;
        update(start, mid, node*2, left, right);
        update(mid+1, end, node*2+1, left, right);
        tree[node] = tree[node*2] + tree[node*2+1];
    }
}