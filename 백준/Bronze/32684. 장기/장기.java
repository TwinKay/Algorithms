import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        int[] scores1 = new int[6];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < 6; i++) {
            scores1[i] = Integer.parseInt(token.nextToken());
        }
        int[] scores2 = new int[6];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < 6; i++) {
            scores2[i] = Integer.parseInt(token.nextToken());
        }
        int sco1 = calScore(scores1);
        int sco2 = calScore(scores2)+1;
        if (sco1 <= sco2) {
            System.out.println("ekwoo");
        }else{
            System.out.println("cocjr0208");
        }
    }
    static int calScore(int[] scores){
        return scores[0]*13 + scores[1]*7 + scores[2]*5 + scores[3]*3 + scores[4]*3 + scores[5]*2;
    }
}