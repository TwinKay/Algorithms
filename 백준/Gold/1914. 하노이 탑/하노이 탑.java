import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
    static StringBuilder sb = new StringBuilder();
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        BigInteger one = new BigInteger("1");
        BigInteger two = new BigInteger("2");
        sb.append(two.pow(N).subtract(one));
        if (N <= 20){
            sb.append("\n");
            recu(N,1,2,3);
        }
        System.out.println(sb);
    }

    static void recu(int moveCnt, int left, int mid, int right){
        if (moveCnt == 0) return;
        recu(moveCnt-1, left, right, mid);
        sb.append(left).append(" ").append(right).append("\n");
        recu(moveCnt-1, mid, left, right);
    }
}