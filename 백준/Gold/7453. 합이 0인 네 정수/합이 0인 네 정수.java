import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static long[] groupA, groupB, groupC, groupD, groupLeft, groupRight;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        groupA = new long[N]; groupB = new long[N]; groupC = new long[N]; groupD = new long[N];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            groupA[i] = Integer.parseInt(token.nextToken());
            groupB[i] = Integer.parseInt(token.nextToken());
            groupC[i] = Integer.parseInt(token.nextToken());
            groupD[i] = Integer.parseInt(token.nextToken());
        }
        groupLeft = new long[N*N]; groupRight = new long[N*N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                groupLeft[i*N+j] = groupA[i]+groupB[j];
                groupRight[i*N+j] = groupC[i]+groupD[j];
            }
        }
        long res = 0;
        Arrays.sort(groupRight);
        double[] groupRightDouble = new double[groupRight.length];
        for (int i = 0; i < groupRight.length; i++) {
            groupRightDouble[i] = (double) groupRight[i];
        }
        for (long l: groupLeft) {
            if (Arrays.binarySearch(groupRight, (-l))>=0){
                long marginLeft = Arrays.binarySearch(groupRightDouble,((double)-l)-0.5);
                long marginRight = Arrays.binarySearch(groupRightDouble,((double)-l)+0.5);
                long len = marginLeft-marginRight;
                res += len;
            }
        }
        System.out.println(res);
    }
}