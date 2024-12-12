import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static char[] chars;
    static int[] charCount;

    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(input.readLine());
        for (int t = 0; t < testCase; t++) {
            String s = input.readLine();
            chars = s.toCharArray();
            Arrays.sort(chars);
            charCount = new int[26];

            for (char c : chars) {
                charCount[c - 'a'] ++;
            }
            permutations(chars.length, new char[chars.length], 0);
        }
        System.out.println(sb);
    }

    private static void permutations(int length, char[] result, int depth) {
        if (depth == length) {
            sb.append(result).append("\n");
            return;
        }

        for (int i = 0; i < 26; i++) {
            if (charCount[i] > 0) {
                charCount[i]--;
                result[depth] = (char) (i + 'a');
                permutations(length, result, depth + 1);
                charCount[i]++;
            }
        }
    }
}
