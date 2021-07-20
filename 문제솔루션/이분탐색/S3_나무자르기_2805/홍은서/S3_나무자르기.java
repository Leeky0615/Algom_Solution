package 이분탐색.S3_나무자르기_2805.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class S3_나무자르기 {
    private static int N;
    private static int M;
    private  static int[] trees;
    private  static long max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        trees=new int[N]; // 나무크기 담는 배열

        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
        for(int i=0;i<N;i++){
            trees[i]= Integer.parseInt(st2.nextToken());
            max=Math.max(max,trees[i]); // 제일 큰 크기 max
        }
        long start = 0;
        long end = max;

        while (start <= end){ // 이분탐색
            long mid = (start+end) /2;// 중간값 설정
            long sum = 0;

            for(int tree: trees){
                if(tree > mid){
                    sum += tree-mid;
                }
            }
            if(sum >= M){// 높이를 올려서 잘린 길이를 줄여야함
                start = mid +1;
            }else{
                end = mid -1;
            }
        }
        System.out.println(end);


    }
}

