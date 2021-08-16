package 문자열.S2_잃어버린괄호_1541.홍은서;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class 잃어버린괄호 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = Integer.MAX_VALUE; // 초기화
        StringTokenizer st = new StringTokenizer(br.readLine(), "-"); // -기준으로 나눔

        while (st.hasMoreTokens()){
            int result=0;

            StringTokenizer adds= new StringTokenizer(st.nextToken(),"+"); // 덧셈으로 나눔
            while (adds.hasMoreTokens()){
                System.out.println(adds.nextToken());
                //result+=Integer.parseInt(adds.nextToken());
            }

            if(sum == Integer.MAX_VALUE){ // 처음일때
                sum = result;
            }else{ // 아니면 처음 수에서 뺌
                sum-=result;
            }
        }
        System.out.println(sum);

    }
}

// 💡 최소로 만들기 위해서 최대한 큰 수를 뺀다
// 💡 큰 수를 만들기 위해서 -기준으로 나눈후 다더하면 된다.
