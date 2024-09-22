import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static int[] arr, tree;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        arr = new int[N+1];
        token = new StringTokenizer(input.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        tree = new int[N*4];
        init(1,N,1);
        M = Integer.parseInt(input.readLine());
        for (int i = 1; i <= M; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            int c = Integer.parseInt(token.nextToken());

            if (a==1){
                update(1,N,1,b,c);
            }else{
                sb.append(min(1,N,1,b,c)).append("\n");
            }
        }
        System.out.println(sb);

    }
    public static int init(int start, int end, int node){
        if (start==end) {
            return tree[node] = arr[start];
        }
        int mid = (start+end)/2;
        return tree[node] = Math.min(init(start, mid, node*2), init(mid+1, end, node*2+1));
    }
    public static int min(int start, int end, int node, int left, int right){
        if (left>end || right<start) {
            return Integer.MAX_VALUE;
        }
        if (left<=start && right>=end){
            return tree[node];
        }
        int mid = (start+end)/2;
        return Math.min(min(start, mid, node*2, left, right), min(mid+1, end, node*2+1, left, right));
    }
    public static void update(int start, int end, int node, int idx, int val){
        if (idx<start || idx>end) return;
        if (start==end){
            tree[node] = val;
            return;
        }
        int mid = (start+end)/2;
        update(start, mid, node*2, idx, val);
        update(mid+1, end, node*2+1, idx, val);
        tree[node] = Math.min(tree[node*2], tree[node*2+1]);
    }
}