package 수학.S4_팩토리얼0의개수_1676.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 팩토리얼0의개수_다른방법 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int cnt2=0;
        int cnt5=0;

        // 팩토리얼
        for(int i=1; i<=N; i++){
            int n = i;

            //소인수 분해
            while (n % 2 == 0){
                cnt2++;
                i/=2;
            }
            while (n % 5 == 0){
                cnt5++;
                n/=5;
            }
        }
        System.out.println(Math.min(cnt2,cnt5));
    }
}
