import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static long[] arr,tree;
    static long MOD = 1000000007L;

    static String s;

    public static void main(String[] args) throws IOException {
        while ((s = input.readLine()) != null){
            token = new StringTokenizer(s);
            N = Integer.parseInt(token.nextToken());
            M = Integer.parseInt(token.nextToken());

            arr = new long[N+1];
            tree = new long[N*4];
            token = new StringTokenizer(input.readLine());
            for (int i=1; i<=N; i++){
                arr[i] = Integer.parseInt(token.nextToken());
            }
            init(1,N,1);
            for (int i=0; i<M; i++){
                token = new StringTokenizer(input.readLine());
                String a = token.nextToken();
                if (a.equals("C")){
                    int b = Integer.parseInt(token.nextToken());
                    Long c = Long.parseLong(token.nextToken());
                    update(1,N,1,b,c);
                }else{
                    int b = Integer.parseInt(token.nextToken());
                    int c = Integer.parseInt(token.nextToken());
                    long temp = mul(1,N,1,b,c);
                    if (temp==0){
                        sb.append(0);
                    }else if (temp>0){
                        sb.append("+");
                    }else{
                        sb.append("-");
                    }
                }
            }
            System.out.println(sb);
            sb.setLength(0);
        }

    }
    public static long init(int start, int end, int node){
        if (start==end){
            return tree[node] = arr[start];
        }
        int mid = (start+end)/2;
        return tree[node] = (init(start,mid,node*2) * init(mid+1,end,node*2+1))%MOD;
    }
    public static long mul(int start, int end, int node, int left, int right){
        if (left>end || right<start){
            return 1;
        }
        if (left<=start && right>=end){
            return tree[node];
        }
        int mid = (start+end)/2;
        return (mul(start,mid,node*2,left,right)*mul(mid+1,end,node*2+1,left,right))%MOD;
    }
    public static void update(int start, int end, int node, int idx, long val){
        if (idx<start || idx>end){
            return;
        }
        if (start==end){
            tree[node] = val;
            return;
        }
        int mid = (start+end)/2;
        update(start,mid,node*2,idx,val);
        update(mid+1,end,node*2+1,idx,val);
        tree[node] = (tree[node*2]*tree[node*2+1])%MOD;
    }

}