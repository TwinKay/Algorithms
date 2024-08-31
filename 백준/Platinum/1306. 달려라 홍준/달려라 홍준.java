import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int[] arr, tree;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(token.nextToken());
        int m = Integer.parseInt(token.nextToken());

        arr = new int[n+1];
        token = new StringTokenizer(input.readLine());
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }

        tree = new int[n*4];

        init(1,n,1);

        for (int i = m; i <= n-m+1; i++){
            sb.append(max(1,n,1,i-m+1,i+m-1)).append(" ");
        }
        System.out.println(sb);
    }
    public static int init(int start, int end, int node){
        if (start==end){
            return tree[node] = arr[start];
        }
        int mid = (start + end)/2;
        return tree[node] = Math.max(init(start, mid, node*2),init(mid+1, end, node*2+1));
    }
    public static int max(int start, int end, int node, int left, int right){
        if (left <= start && end <= right){
            return tree[node];
        }
        if (left > end || right < start) return 0;
        int mid = (start + end)/2;
        return Math.max(max(start,mid,node*2,left,right), max(mid+1,end,node*2+1,left,right));
    }
}