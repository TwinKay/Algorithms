// 공식을 직접 만들어냈다..! ㅜ.ㅜ
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        long a = Long.parseLong(token.nextToken());
        long b = Long.parseLong(token.nextToken());
        long res = accumOne(b)-accumOne(a-1);
        System.out.println(res);
    }
    public static long accumOne (long x){
        long cnt = 0;
        String stringA = Long.toBinaryString(x+1);
        int bonus = 0;
        for (int i=0; i<stringA.length(); i++) {
            if (stringA.charAt(i) == '1') {
                cnt += (long) (Math.pow(2,stringA.length()-i-1)*(stringA.length()-i-1)/2);
                cnt += (long) (Math.pow(2,stringA.length()-i-1)*bonus);
                bonus++;
            }
        }
        return cnt;
    }
}