package 큐.S1_최소힙_1927.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

// 🔑 우선순위 큐를 이용하면 바로 풀린다.

public class 최소힙 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        while(N --> 0){
            int n = Integer.parseInt(br.readLine());
            if(n==0){
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
