package 큐.S1_절댓값힙_11286.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class 절대값힙 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> queue = new PriorityQueue<>((o1, o2) ->
                Math.abs(o1) == Math.abs(o2) ? Integer.compare(o1, o2) : Integer.compare(Math.abs(o1), Math.abs(o2))
        );
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<N; i++){
            int n = Integer.parseInt(br.readLine());
            if(n==0){
                sb.append(queue.size()==0? 0: queue.poll()).append('\n');
            }else{
                queue.add(n);
            }
        }
        System.out.println(sb.toString());
    }
}
