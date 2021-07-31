package 해시.S4_나는야포켓몬마스터이다솜_1620.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class 나는야포켓몬마스터이다솜 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String,Integer> poketmons = new HashMap<>();
        String [] names = new String [N+1];
        StringBuilder sb = new StringBuilder();

        for(int i=1; i<N+1; i++){
            String poketmon = br.readLine();
            poketmons.put(poketmon, i);
            names[i] = poketmon;
        }

        while (M --> 0){
            String quiz = br.readLine();
            boolean isNumeric =  quiz.matches("[+-]?\\d*(\\.\\d+)?");
            if(isNumeric){ // 숫자로 물어볼 경우 values
                sb.append(names[Integer.parseInt(quiz)]);
            }else{ //문자로 물어볼 경우 key
                sb.append(poketmons.get(quiz));

            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }
}
