import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
 
    public static void main(String[] args) throws IOException {
 
        for (int t=1; t<11; t++){
            sb.append("#").append(t).append(" ");
 
            int cntA = 0; //()
            int cntB = 0; //[]
            int cntC = 0; //{}
            int cntD = 0; //<>
 
            int n = Integer.parseInt(input.readLine());
            String s = input.readLine();
            char[] arr = s.toCharArray();
 
            for (char c : arr){
                if (c=='('){
                    cntA ++;
                } else if (c==')'){
                    cntA --;
                } else if (c=='['){
                    cntB ++;
                } else if (c==']'){
                    cntB --;
                } else if (c=='{'){
                    cntC ++;
                } else if (c=='}'){
                    cntC --;
                } else if (c=='<'){
                    cntD ++;
                } else if (c=='>'){
                    cntD --;
                }
            }
            if (cntA!=0 || cntB!=0 || cntC!=0 || cntD!=0){
                sb.append(0);
                sb.append("\n");
                continue;
            }
 
            cntA=0;cntB=0;cntC=0;cntD=0; // 초기화
 
            for (char c : arr){
                if (c=='('){
                    cntA ++;
                } else if (c==')'){
                    cntA --;
                } else if (c=='['){
                    cntB ++;
                } else if (c==']'){
                    cntB --;
                } else if (c=='{'){
                    cntC ++;
                } else if (c=='}'){
                    cntC --;
                } else if (c=='<'){
                    cntD ++;
                } else if (c=='>'){
                    cntD --;
                }
 
                if (cntA<0 || cntB<0 || cntC<0 || cntD<0){
                    sb.append(0);
                    sb.append("\n");
                    continue;
                }
            }
            sb.append(1);
            sb.append("\n");
            continue;
        }
        System.out.println(sb);
    }
}