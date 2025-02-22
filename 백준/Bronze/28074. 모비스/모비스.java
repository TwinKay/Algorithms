import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        char[] chars = input.readLine().toCharArray();
        int[] cnt = new int[26];
        for (char c : chars) {
            cnt[c - 'A']++;
        }
        if (cnt['M'-'A']!=0 && cnt['O'-'A']!=0 && cnt['B'-'A']!=0 && cnt['I'-'A']!=0 && cnt['S'-'A']!=0) {
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
}