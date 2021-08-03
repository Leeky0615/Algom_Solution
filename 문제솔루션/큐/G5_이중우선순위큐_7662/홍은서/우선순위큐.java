package 큐.G5_이중우선순위큐_7662.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeMap;

public class 우선순위큐 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tests  = Integer.parseInt(br.readLine());

        while (tests --> 0){
            int k = Integer.parseInt(br.readLine());
            TreeMap<Integer, Integer> queue = new TreeMap<>(); // 정렬된 map

            for(int i=0; i<k; i++){
                String [] orders = br.readLine().split(" ");
                char c = orders[0].charAt(0);
                int n = Integer.parseInt(orders[1]);

                if(c == 'I'){
                    queue.put(n, queue.getOrDefault(n,0)+1);
                }else {
                    if (queue.size() == 0) {
                        continue;
                    }
                    // 이렇게 써보고 싶었음...
                    int num = n == 1 ? queue.lastKey() : queue.firstKey();
                    if (queue.put(num, queue.get(num) - 1) == 1) {
                        queue.remove(num);
                    }
                }
            }
            System.out.println(queue.size() == 0 ? "EMPTY" : queue.lastKey() + " "  + queue.firstKey());
        }
    }
}
