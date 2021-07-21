package 큐.S3_프린터큐_1966.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class S3_프린터큐 {
    public static void main(String[] args) throws IOException {
        PriorityQueue<Printer> queue = new PriorityQueue<>(Collections.reverseOrder());
        ArrayList<Integer> al = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int tests = Integer.parseInt(st.nextToken());

        while (tests-- > 0) { // 테스트 단위
            StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st1.nextToken()); // 문서 수
            int idx = Integer.parseInt(st1.nextToken()); // 인덱스
            int i=0;
            int answer=0;

            StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
            while (st2.hasMoreTokens()){
                int P = Integer.parseInt(st2.nextToken());
                queue.offer(new Printer(P,i));
                i++;
            }
            while (!queue.isEmpty()){
                if(queue.poll().i == idx){
                    answer++;
                    break;
                }else{
                    answer++;
                }
            }
            System.out.println(answer);
            queue.clear();
        }
    }

    private static class Printer implements Comparable<Printer> {
        int p;
        int i;
        public Printer(int p, int i) {
            this.p=p;
            this.i=i;
        }
        @Override
        public int compareTo(Printer o) {
            return o.p-this.p;
        }
    }
}