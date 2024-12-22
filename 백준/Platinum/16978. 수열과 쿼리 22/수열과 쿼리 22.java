import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,Q;
    static long[] arr, tree;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        arr = new long[N+1];
        token = new StringTokenizer(input.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        tree = new long[N*4];
        init(1,N,1);
        PriorityQueue<int[]> querys = new PriorityQueue<>((o1, o2) -> {
            if (o1[1] == o2[1]) {
                return o1[0] - o2[0];
            }
            return o1[1] - o2[1];
        });
        Q = Integer.parseInt(input.readLine());
        int updateOrder = 1;
        int sumOrder = 0;
        for (int q = 0; q < Q; q++) {
            token = new StringTokenizer(input.readLine());
            int queryType = Integer.parseInt(token.nextToken());
            if (queryType == 1) {
                int i = Integer.parseInt(token.nextToken());
                int v = Integer.parseInt(token.nextToken());
                querys.add(new int[]{1,updateOrder,i,v});
                updateOrder++;
            }else{
                int k = Integer.parseInt(token.nextToken());
                int i = Integer.parseInt(token.nextToken());
                int j = Integer.parseInt(token.nextToken());
                querys.add(new int[]{2,k,i,j, sumOrder});
                sumOrder++;
            }
        }
        List<Integer> orders = new ArrayList<>();
        long[] resArr = new long[Q+1];
        while (!querys.isEmpty()) {
            int[] query = querys.poll();
            if (query[0]==1){
                update(1,N,1,query[2],query[3]);
            }else{
                long l = sum(1,N,1,query[2],query[3]);
                int ord = query[4];
                orders.add(ord);
                resArr[ord] = l;
            }
        }
        Collections.sort(orders);
        for (int o : orders){
            sb.append(resArr[o]).append("\n");
        }
        System.out.println(sb);
    }
    
    public static long init(int start, int end, int node){
        if (start==end) {
            return tree[node] = arr[start];
        }
        int mid = (start+end)/2;
        return tree[node] = init(start, mid, node*2)+init(mid+1, end, node*2+1);
    }

    public static long sum(int start, int end, int node, int left, int right){
        if (left>end || right<start) {
            return 0;
        }
        if (left<=start && right>=end){
            return tree[node];
        }
        int mid = (start+end)/2;
        return sum(start,mid,node*2,left,right) + sum(mid+1,end,node*2+1,left,right);
    }

    public static void update(int start, int end, int node, int idx, long val) {
        if (idx < start || idx > end) return;
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start+end)/2;
        update(start, mid, node*2, idx, val);
        update(mid+1, end, node*2+1, idx, val);
        tree[node] = tree[node*2] + tree[node*2+1];
    }
}