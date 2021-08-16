package 큐.S1_절댓값힙_11286.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class 절대값힙 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> queuePlus = new PriorityQueue<>(); // 오름차순
        PriorityQueue<Integer> queueMinus = new PriorityQueue<>(Collections.reverseOrder()); // 내름차순

        StringBuilder sb = new StringBuilder();

        while (N --> 0) {
            int n = Integer.parseInt(br.readLine());
            if(n==0){
                if(queueMinus.isEmpty() || queuePlus.isEmpty()){
                    if(queueMinus.isEmpty() && queuePlus.isEmpty()){
                        sb.append("0").append("\n");
                    }else{
                        if(queueMinus.isEmpty() ){
                            sb.append(queuePlus.poll()).append("\n");
                        }else{
                            sb.append(queuePlus.poll()).append("\n");
                        }
                    }

                }else{
                    if(Math.abs(queueMinus.peek()) == Math.abs(queuePlus.peek())){
                       sb.append(queueMinus.poll()).append("\n");
                    }else{
                        int a = Math.abs(queueMinus.peek()) < Math.abs(queuePlus.peek()) ? queueMinus.poll() : queuePlus.poll();
                        sb.append(a).append("\n");
                    }
                }
            }else{
                if(n>0){
                    queuePlus.add(n);
                }else{
                    queueMinus.add(n);
                }
            }
        }
        System.out.println(sb);
    }
}
