import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        String s = input.readLine();
        for (int i = 0; i < s.length(); i++) {
            int a = s.charAt(i) - '0';
            if (a==0){
                sb.append("0000\n0  0\n0  0\n0  0\n0000\n");
            }else if (a==1){
                sb.append("   1\n   1\n   1\n   1\n   1\n");
            }else if (a==2){
                sb.append("2222\n   2\n2222\n2\n2222\n");
            }else if (a==3){
                sb.append("3333\n   3\n3333\n   3\n3333\n");
            }else if (a==4){
                sb.append("4  4\n4  4\n4444\n   4\n   4\n");
            }else if (a==5){
                sb.append("5555\n5\n5555\n   5\n5555\n");
            }else if (a==6){
                sb.append("6666\n6\n6666\n6  6\n6666\n");
            }else if (a==7){
                sb.append("7777\n   7\n   7\n   7\n   7\n");
            }else if (a==8){
                sb.append("8888\n8  8\n8888\n8  8\n8888\n");
            }else if (a==9){
                sb.append("9999\n9  9\n9999\n   9\n   9\n");
            }
            if (i != s.length()-1){
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }
}