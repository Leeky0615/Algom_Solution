package 해시.S3_ATM_11399.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class ATM {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> queue = new PriorityQueue<>(); // 오름차순
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()){
            queue.add(Integer.parseInt(st.nextToken()));
        }

        ArrayList<Integer> al = new ArrayList<>();
        int sum = 0;
        while (!queue.isEmpty()){
            sum+=queue.poll();
            al.add(sum);
        }

        int total=0;

        for(int i : al){
            total+=i;
        }
        System.out.println(total);
    }
}