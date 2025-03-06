import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static int[] arr, tree;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        arr = new int[N+1];
        token = new StringTokenizer(input.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }

        tree = new int[N*4];
        init(1, N, 1);

        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < M; i++) {
            int num = Integer.parseInt(token.nextToken());

            int prefix = 0;
            if (num > 1) {
                prefix = find(1, N, 1, 1, num - 1);
            }

            int res = prefix + 1;
            sb.append(res).append(" ");
            update(1, N, 1, num, -arr[num]);
        }
        System.out.println(sb);
    }

    public static int init(int start, int end, int node) {
        if (start == end) {
            return tree[node] = arr[start];
        }
        int mid = (start + end) / 2;
        return tree[node] = init(start, mid, node * 2)
                + init(mid + 1, end, node * 2 + 1);
    }

    public static int find(int start, int end, int node, int left, int right) {
        if (right < start || end < left) {
            return 0;
        }
        if (left <= start && end <= right) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        return find(start, mid, node * 2, left, right) + find(mid + 1, end, node * 2 + 1, left, right);
    }

    public static void update(int start, int end, int node, int idx, int val) {
        if (idx < start || idx > end) return;
        tree[node] += val;
        if (start == end) {
            return;
        }
        int mid = (start + end) / 2;
        update(start, mid, node * 2, idx, val);
        update(mid + 1, end, node * 2 + 1, idx, val);
    }
}
