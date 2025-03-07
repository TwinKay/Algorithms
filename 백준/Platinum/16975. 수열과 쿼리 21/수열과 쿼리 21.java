import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static long[] arr,tree,lazy;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        arr = new long[N+1];
        token = new StringTokenizer(input.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Long.parseLong(token.nextToken());
        }
        
        tree = new long[N*4];
        lazy = new long[N*4];
        init(1,N,1);
        
        M = Integer.parseInt(input.readLine());
        for (int m = 1; m <= M; m++) {
            token = new StringTokenizer(input.readLine());

            int q = Integer.parseInt(token.nextToken());
            if (q==1) {
                int left = Integer.parseInt(token.nextToken());
                int right = Integer.parseInt(token.nextToken());
                long val = Long.parseLong(token.nextToken());
                update(1,N,1,left,right,val);

            }else {
                int idx = Integer.parseInt(token.nextToken());
                sb.append(sum(1,N,1,idx,idx)).append("\n");
            }
        }
        System.out.println(sb);
    }

    public static long init(int start, int end, int node) {
        if (start == end) {
            return tree[node] = arr[start];
        }
        int mid = (start + end) / 2;
        return tree[node] = init(start,mid,node*2) + init(mid+1,end,node*2+1);
    }

    public static long sum(int start, int end, int node, int left, int right) {
        propa(start,end,node);

        if (right<start || left>end) {
            return 0;
        }
        if (left<=start && right>=end) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        return sum(start,mid,node*2,left,right) + sum(mid+1,end,node*2+1,left,right);
    }

    public static void update(int start, int end, int node, int left, int right, long val) {
        propa(start,end,node);

        if (right<start || left>end) {
            return;
        }
        if (left<=start && right>=end) {
            lazy[node] += val;
            propa(start,end,node);
            return;
        }
        int mid = (start + end) / 2;
        update(start,mid,node*2,left,right,val);
        update(mid+1,end,node*2+1,left,right,val);
        tree[node] = tree[node*2] + tree[node*2+1];
    }

    public static void propa(int start, int end, int node) {
        if (lazy[node] != 0) {
            tree[node] += lazy[node] * (end-start+1);
            if (start != end) {
                lazy[node*2] += lazy[node];
                lazy[node*2+1] += lazy[node];
            }
        }
        lazy[node] = 0;
    }
}