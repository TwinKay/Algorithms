import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int H,W;
    static boolean[][] arr;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        H = Integer.parseInt(token.nextToken());
        W = Integer.parseInt(token.nextToken());
        int total = H*W;
        arr = new boolean[H][W];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < W; i++) {
            int num = Integer.parseInt(token.nextToken());
            total -= num;
            num--;
            while (num>=0){
                arr[num][i] = true;
                num--;
            }
        }
        for (int i=0; i<H; i++){
            if(!arr[i][0]){
                int num = 0;
                arr[i][0] = true;
                total --;
                while(num+1!=W && !arr[i][num+1] ){
                    arr[i][num+1] = true;
                    num++;
                    total --;
                }
            }
            if(!arr[i][W-1]){
                int num = W-1;
                arr[i][W-1] = true;
                total --;
                while(num!=-1 && !arr[i][num-1]){
                    arr[i][num-1] = true;
                    num--;
                    total --;
                }
            }
        }
        System.out.println(total);
    }
}