import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static long[] arr, tree;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(token.nextToken());
        int m = Integer.parseInt(token.nextToken());
        int k = Integer.parseInt(token.nextToken());

        arr = new long[n+1];
        for (int i = 1; i <= n; i++) {
            arr[i] = Long.parseLong(input.readLine());
        }

        tree = new long[n*4];

        init(1,n,1);

        for (int i=0; i<m+k; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());

            if (a==1){
                long c = Long.parseLong(token.nextToken());
                update(1,n,1,b,c);
            }else{
                int c = Integer.parseInt(token.nextToken());
                sb.append(mul(1,n,1,b,c)).append("\n");
            }
        }
        System.out.println(sb);
    }

    public static long init(int start, int end, int node){
        if (start==end){
            return tree[node] = arr[start];
        }
        int mid = (start + end)/2;
        return tree[node] = (init(start, mid, node*2) * init(mid+1, end, node*2+1))%1000000007;
    }


    public static long mul(int start, int end, int node, int left, int right){
        if (left <= start && end <= right){
            return tree[node];
        }
        if (left > end || right < start) return 1;
        int mid = (start + end)/2;
        return (mul(start,mid,node*2,left,right) * mul(mid+1,end,node*2+1,left,right))%1000000007;
    }

    public static void update(int start, int end, int node, int idx, long val){
        if (idx<start || idx>end) return;

        if (start==end) {
            tree[node] = val;
            return;
        }
        int mid = (start+end)/2;
        update(start,mid,node*2,idx,val);
        update(mid+1,end,node*2+1,idx,val);
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007;
    }

}