import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
//    static int[] arr;
    static int[][] arr, tree;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        arr = new int[N+1][2];
        token = new StringTokenizer(input.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i][0] = Integer.parseInt(token.nextToken());
            arr[i][1] = i;
        }
        tree = new int[N*4][2];

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
                int[] temp = min(1,N,1,b,c);
                sb.append(temp[1]).append("\n");
            }
        }
        System.out.println(sb);

    }
    public static int[] minIdx(int[] m1, int[] m2){
        if (m1[0]==m2[0]){
            if (m1[1]<m2[1]){
                return m1;
            }else{
                return m2;
            }
        }
        if (m1[0]<m2[0]){
            return m1;
        }else{
            return m2;
        }
    }

    public static int[] init(int start, int end, int node){
        if (start==end) {
            tree[node][0] = arr[start][0];
            tree[node][1] = arr[start][1];

            return tree[node];
        }
        int mid = (start+end)/2;
        return tree[node] = minIdx(init(start, mid, node*2), init(mid+1, end, node*2+1));
    }
    public static int[] min(int start, int end, int node, int left, int right){
        if (left>end || right<start) {
            return new int[] {Integer.MAX_VALUE,-1};
        }
        if (left<=start && right>=end){
            return tree[node];
        }
        int mid = (start+end)/2;
        return minIdx(min(start, mid, node*2, left, right), min(mid+1, end, node*2+1, left, right));
    }
    public static void update(int start, int end, int node, int idx, int val){
        if (idx<start || idx>end) return;
        if (start==end){
            tree[node][0] = val;
            return;
        }
        int mid = (start+end)/2;
        update(start, mid, node*2, idx, val);
        update(mid+1, end, node*2+1, idx, val);
        tree[node] = minIdx(tree[node*2], tree[node*2+1]);
    }
}