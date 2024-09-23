import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N = 1000000;
    static int M;
    static int[] tree;

    public static void main(String[] args) throws IOException {
        M = Integer.parseInt(input.readLine());
        tree = new int[N*4];

        for (int i=0; i<M; i++){
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            if (a==1){
                int tempIdx = binarySearchSum(1,N,b);
                if (tempIdx<0){
                    tempIdx = -tempIdx-1;
                }
                int tempVal = sum(1,N,1,1,tempIdx);
                int low = 1;
                int high = tempIdx;

                while (low < high) {
                    int mid = (low + high) >>> 1;
                    if (sum(1, N, 1, 1, mid) == tempVal) {
                        high = mid;
                    } else {
                        low = mid + 1;
                    }
                }
                tempIdx = low;
                sb.append(tempIdx).append("\n");
                update(1, N, 1, tempIdx, -1);
            }else{
                int c = Integer.parseInt(token.nextToken());
                update(1,N,1,b,c);
            }
        }
        System.out.println(sb);
    }
    private static int binarySearchSum(int fromIndex, int toIndex, int key) {
        int low = fromIndex;
        int high = toIndex;

        while (low <= high) {
            int mid = (low + high) >>> 1;
            int midVal = sum(1,N,1,1,mid);

            if (midVal < key)
                low = mid + 1;
            else if (midVal > key)
                high = mid - 1;
            else
                return mid;
        }
        return -(low + 1);
    }

    public static int sum(int start, int end, int node, int left, int right){
        if (left>end || right<start){
            return 0;
        }
        if (left<=start && right>=end){
            return tree[node];
        }
        int mid = (start+end)/2;
        return sum(start,mid,node*2,left,right) + sum(mid+1,end,node*2+1,left,right);
    }
    public static void update(int start, int end, int node, int idx, int val){
        if (idx<start || idx>end){
            return;
        }
        if (start==end){
            tree[node] += val;
            return;
        }
        int mid = (start+end)/2;
        update(start,mid,node*2,idx,val);
        update(mid+1,end,node*2+1,idx,val);
        tree[node] = tree[node*2]+tree[node*2+1];
    }

}