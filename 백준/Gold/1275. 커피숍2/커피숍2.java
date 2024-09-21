import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,Q;

    static long[] arr,tree;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        Q = Integer.parseInt(token.nextToken());

        arr = new long[N+1];
        token = new StringTokenizer(input.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Long.parseLong(token.nextToken());
        }
        tree = new long[N*4];

        init(1,N,1);
        for (int i=0; i<Q; i++){
            token = new StringTokenizer(input.readLine());
            int x = Integer.parseInt(token.nextToken());
            int y = Integer.parseInt(token.nextToken());
            int a = Integer.parseInt(token.nextToken());
            long b = Long.parseLong(token.nextToken());
            if (x>y){
                int temp = x;
                x = y;
                y = temp;
            }
            sb.append(sum(1,N,1,x,y)).append("\n");
            long val = b-arr[a];
            arr[a] = b;
            update(1,N,1,a,val);
        }
        System.out.println(sb);

    }
    public static long init(int start, int end, int node){
        if (start==end){
            return tree[node] = arr[start];
        }
        int mid = (start+end)/2;
        return tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1);
    }
    public static long sum(int start, int end, int node, int left, int right){
        if (left<=start && right>=end){
            return tree[node];
        }
        if (left>end || right<start) return 0;
        int mid = (start+end)/2;
        return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2+1, left, right);
    }
    public static void update (int start, int end, int node, int idx, long val){
        if (idx<start || idx>end) return;
        tree[node] += val;
        if (start==end) return;
        int mid = (start+end)/2;
        update(start,mid,node*2,idx,val);
        update(mid+1, end, node*2+1, idx,val);
    }
}