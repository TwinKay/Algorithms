import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb= new StringBuilder();

    static int N,M;

    static int[] arr, minTree;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        arr = new int[N+1];
        minTree = new int[N*4];
        for (int i=1; i<=N; i++) {
            arr[i] = Integer.parseInt(input.readLine());
        }
        initMin(1,N,1);
        for (int i=0; i<M; i++){
            token = new StringTokenizer(input.readLine());
            int left = Integer.parseInt(token.nextToken());
            int right = Integer.parseInt(token.nextToken());
            int a = min(1,N,1,left,right);
            sb.append(a).append("\n");
        }
        System.out.println(sb);

    }
    public static int initMin(int start, int end, int node){
        if(start==end){
            return minTree[node] = arr[start];
        }
        int mid = (start+end)/2;
        return minTree[node] = Math.min(initMin(start, mid, node*2), initMin(mid+1, end, node*2+1));
    }
    public static int min(int start, int end, int node, int left, int right){
        if (left<=start && right>=end){
            return minTree[node];
        }
        if (left>end || right<start) return Integer.MAX_VALUE;
        int mid = (start+end)/2;
        return Math.min(min(start,mid,node*2,left,right), min(mid+1,end,node*2+1,left,right));
    }

}