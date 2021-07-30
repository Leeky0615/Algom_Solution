package 큐.최대힙_11279.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class 최대힙 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder()); // 높은 숫자 순

        while (N --> 0){
            int n = Integer.parseInt(br.readLine());
            if(n == 0){
                if(heap.isEmpty()){
                    System.out.println(0);
                }else{
                    System.out.println(heap.poll());
                }
            }else{
                heap.add(n);
            }
        }
    }
}
