import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static int[] arr, tree;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t=0; t<T; t++){
            N = Integer.parseInt(input.readLine());
            arr = new int[N+1];
            tree = new int[N*4];
            token = new StringTokenizer(input.readLine());
            for (int i=1; i<=N; i++){
                arr[i] = Integer.parseInt(token.nextToken());
            }
            init(1,N,1);
            HashMap<Integer, List<Integer>> map = new HashMap<>();
            for (int i=1; i<=N; i++){
                int val = arr[i];
                if (map.containsKey(val)){
                    map.get(val).add(i);
                }else{
                    map.put(val,new ArrayList<>());
                    map.get(val).add(i);
                }
            }
            boolean res = true;
            for (int key : map.keySet()){
                List<Integer> l = map.get(key);
                if (l.size()>=2){
                    int left = l.get(0);
                    int right = l.get(l.size()-1);
                    int rangeMax = max(1,N,1,left,right);
                    if (rangeMax>key){
                        res = false;
                        break;
                    }
                }
            }
            if (res){
                sb.append("Yes").append("\n");
            }else{
                sb.append("No").append("\n");
            }
        }
        System.out.println(sb);
    }
    public static int init(int start, int end, int node){
        if (start==end){
            return tree[node] = arr[start];
        }
        int mid = (start+end)/2;
        return tree[node] = Math.max(init(start,mid,node*2),init(mid+1,end,node*2+1));
    }
    public static int max(int start, int end, int node, int left, int right){
        if (left>end || right<start){
            return 0;
        }
        if (left<=start && right>=end){
            return tree[node];
        }
        int mid = (start+end)/2;
        return Math.max(max(start,mid,node*2,left,right),max(mid+1,end,node*2+1,left,right));
    }
}