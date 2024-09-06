// 공식을 직접 만들어냈다..! ㅜ.ㅜ
// 수정 - 비트연산자 사용, 반복 계산 제거
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
        System.out.println(accumOne(b)-accumOne(a-1));
    }
    public static long accumOne (long x){
        long cnt = 0;
        String stringA = Long.toBinaryString(x+1);
        int bonus = 0;
        for (int i=0; i<stringA.length(); i++) {
            if (stringA.charAt(i) == '1') {
                long bitIdx = stringA.length()-i-1;
                long powVal = (1L << bitIdx);
                cnt += powVal * bitIdx / 2;
                cnt += powVal * bonus;
                bonus++;
            }
        }
        return cnt;
    }
}