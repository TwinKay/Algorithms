import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;
    static String S;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        S = input.readLine();
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            if (Integer.valueOf((S.charAt(i)))%2==0){
                cnt++;
            }else{
                cnt--;
            }
        }
        if(cnt==0){
            System.out.println(-1);
        }else if(cnt>0){
            System.out.println(0);
        }else{
            System.out.println(1);
        }
    }
}