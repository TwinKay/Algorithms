import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());

        for (int i=1; i<n+1; i++) {
            int cnt = CntChar(i);
            if (cnt!=0) {
                for (int j=0; j<cnt; j++) {
                    System.out.print("-");
                }
            } else {
                System.out.print(i);
            }
            if (i!=n) {
                System.out.print(" ");
            }
        }
    }

    public static int CntChar(int a) {
        String str = String.valueOf(a);
        int cnt = 0;
        for (int i=0; i<str.length(); i++) {
            if (str.charAt(i) =='3' || str.charAt(i)=='6' || str.charAt(i)=='9') {
                cnt ++;
            }
        }
        return cnt;
    }
}