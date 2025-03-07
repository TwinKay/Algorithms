import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static int[] arr, minTree, maxTree;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        arr = new int[N+1];
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(input.readLine());
        }
        minTree = new int[N*4];
        maxTree = new int[N*4];
        initMinTree(1,N,1);
        initMaxTree(1,N,1);
        for (int m = 0; m < M; m++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            int max = findMax(1,N,1,a,b);
            int min = findMin(1,N,1,a,b);
            sb.append(max - min).append("\n");
        }
        System.out.println(sb);

    }
    public static void updateMin(int start, int end, int node, int idx, int val) {
        if (idx<start || idx>end) return;
        if (start==end) {
            minTree[node] = val;
            return;
        }
        int mid = (start+end)/2;
        updateMin(start,mid,node*2,idx,val);
        updateMin(mid+1,end,node*2+1,idx,val);
        minTree[node] = Math.min(minTree[node*2],minTree[node*2+1]);
    }
    public static void updateMax(int start, int end, int node, int idx, int val) {
        if (idx<start || idx>end) return;
        if (start==end) {
            maxTree[node] = val;
            return;
        }
        int mid = (start+end)/2;
        updateMax(start,mid,node*2,idx,val);
        updateMax(mid+1,end,node*2+1,idx,val);
        maxTree[node] = Math.max(maxTree[node*2],maxTree[node*2+1]);
    }

    public static int findMin(int start, int end, int node, int left, int right) {
        if (start>right || end<left) {
            return Integer.MAX_VALUE;
        }
        if (left<=start && end<=right) {
            return minTree[node];
        }
        int mid = (start + end)/2;
        return Math.min(findMin(start,mid,node*2,left,right),
                findMin(mid+1,end,node*2+1,left,right));
    }
    public static int findMax(int start, int end, int node, int left, int right) {
        if (start>right || end<left) {
            return Integer.MIN_VALUE;
        }
        if (left<=start && end<=right) {
            return maxTree[node];
        }
        int mid = (start + end)/2;
        return Math.max(findMax(start,mid,node*2,left,right),
                findMax(mid+1,end,node*2+1,left,right));
    }
    public static int initMinTree(int start, int end, int node) {
        if (start == end) {
            return minTree[node] = arr[start];
        }
        int mid = (start + end) / 2;
        return minTree[node] = Math.min(initMinTree(start, mid, node*2),
                initMinTree(mid+1, end, node*2+1));
    }
    public static int initMaxTree(int start, int end, int node) {
        if (start == end) {
            return maxTree[node] = arr[start];
        }
        int mid = (start + end) / 2;
        return maxTree[node] = Math.max(initMaxTree(start, mid, node*2),
                initMaxTree(mid+1, end, node*2+1));
    }
}