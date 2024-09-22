import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static long[] tree;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(token.nextToken());
        int m = Integer.parseInt(token.nextToken());

        tree = new long[n*4];

        for (int i=0; i<m; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());

            if (a==1){
                long c = Long.parseLong(token.nextToken());
                update(1,n,1,b,c);
            }else{
                int c = Integer.parseInt(token.nextToken());
                if (b>c){
                    int temp = b;
                    b = c;
                    c = temp;
                }
                sb.append(sum(1,n,1,b,c)).append("\n");
            }
        }
        System.out.println(sb);
    }

    public static long sum(int start, int end, int node, int left, int right){
        if (left > end || right < start) return 0;
        if (left <= start && end <= right){
            return tree[node];
        }
        int mid = (start + end)/2;
        return sum(start,mid,node*2,left,right) + sum(mid+1,end,node*2+1,left,right);
    }

    public static void update(int start, int end, int node, int idx, long val){
        if (idx<start || idx>end) return;
        if (start==end){
            tree[node] = val;
            return;
        }
        int mid = (start+end)/2;
        update(start,mid,node*2,idx,val);
        update(mid+1,end,node*2+1,idx,val);
        tree[node] = tree[node*2] + tree[node*2+1];
    }
}