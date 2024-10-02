import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int K;
    static Deque<Integer> deq1R, deq2R, deq3R, deq2L, deq3L, deq4L;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t=1; t<=T; t++) {
            K = Integer.parseInt(input.readLine());
            deq1R = new ArrayDeque<>();
            deq2R = new ArrayDeque<>();
            deq3R = new ArrayDeque<>();
            deq2L = new ArrayDeque<>();
            deq3L = new ArrayDeque<>();
            deq4L = new ArrayDeque<>();

            token = new StringTokenizer(input.readLine());
            for (int i=0; i<8; i++){
                int temp = Integer.parseInt(token.nextToken());
                deq1R.add(temp);
            }
            token = new StringTokenizer(input.readLine());
            for (int i=0; i<8; i++){
                int temp = Integer.parseInt(token.nextToken());
                deq2R.add(temp);
                deq2L.add(temp);
            }
            token = new StringTokenizer(input.readLine());
            for (int i=0; i<8; i++){
                int temp = Integer.parseInt(token.nextToken());
                deq3R.add(temp);
                deq3L.add(temp);
            }
            token = new StringTokenizer(input.readLine());
            for (int i=0; i<8; i++){
                int temp = Integer.parseInt(token.nextToken());
                deq4L.add(temp);
            }

            for (int i=0; i<2; i++){
                rotateR(deq1R);rotateR(deq2R);rotateR(deq3R);
            }
            for (int i=0; i<2; i++){
                rotateL(deq2L);rotateL(deq3L);rotateL(deq4L);
            }

            for (int k=0; k<K; k++){
                boolean con1,con2,con3;
                con1 = false;
                con2 = false;
                con3 = false;
                if (!Objects.equals(deq1R.peekFirst(), deq2L.peekFirst())) con1 = true;
                if (!Objects.equals(deq2R.peekFirst(), deq3L.peekFirst())) con2 = true;
                if (!Objects.equals(deq3R.peekFirst(), deq4L.peekFirst())) con3 = true;

                token = new StringTokenizer(input.readLine());
                int num = Integer.parseInt(token.nextToken());
                int order = Integer.parseInt(token.nextToken());
                int[] orders = {0,0,0,0};
                if (num==1){
                    orders[0] = order;
                    if(con1) {
                        orders[1] = -order;
                        if(con2){
                            orders[2] = order;
                            if(con3){
                                orders[3] = -order;
                            }
                        }
                    }
                }else if (num==2){
                    orders[1] = order;
                    if(con1){
                        orders[0] = -order;
                    }
                    if(con2){
                        orders[2] = -order;
                        if(con3){
                            orders[3] = order;
                        }
                    }
                }else if (num==3){
                    orders[2] = order;
                    if(con2){
                        orders[1] = -order;
                        if(con1){
                            orders[0] = order;
                        }
                    }
                    if(con3){
                        orders[3] = -order;
                    }
                }else{
                    orders[3] = order;
                    if(con3){
                        orders[2] = -order;
                        if(con2){
                            orders[1] = order;
                            if(con1){
                                orders[0] = -order;
                            }
                        }
                    }
                }

                //orders로 rotate
                if(orders[0]==1){
                    rotateL(deq1R);

                }else if (orders[0]==-1){
                    rotateR(deq1R);
                }
                if(orders[1]==1){
                    rotateL(deq2L);
                    rotateL(deq2R);
                }else if (orders[1]==-1){
                    rotateR(deq2L);
                    rotateR(deq2R);
                }
                if(orders[2]==1){
                    rotateL(deq3L);
                    rotateL(deq3R);
                }else if (orders[2]==-1){
                    rotateR(deq3L);
                    rotateR(deq3R);
                }
                if(orders[3]==1){
                    rotateL(deq4L);
                }else if (orders[3]==-1){
                    rotateR(deq4L);
                }
            }
            // 회전 끝, 위를 보도록
            for (int i=0; i<2; i++){
                rotateL(deq1R);rotateL(deq2R);rotateL(deq3R);rotateR(deq4L);
            }
            int res = 0;
            int head1, head2, head3, head4;
            head1 = deq1R.peekFirst();
            head2 = deq2R.peekFirst();
            head3 = deq3R.peekFirst();
            head4 = deq4L.peekFirst();
            if (head1==1){
                res += 1;
            }
            if (head2==1){
                res += 2;
            }
            if (head3==1){
                res += 4;
            }
            if (head4==1){
                res += 8;
            }
            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);

    }
    public static void rotateR(Deque<Integer> deq){
        int temp = deq.pollFirst();
        deq.addLast(temp);
    }
    public static void rotateL(Deque<Integer> deq){
        int temp = deq.pollLast();
        deq.addFirst(temp);
    }
}