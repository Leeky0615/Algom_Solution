package 수학.S4_팩토리얼0의개수_1676.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 🔑 2X5 = 10 인거를 이용한다

public class 팩토리얼0의개수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int cnt = 0;

        while (N >=5){ // 5X4X3X2X1
            cnt += N/5;
            N /= 5;
        }
        System.out.println(cnt);
    }
}
