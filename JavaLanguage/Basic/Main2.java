import java.util.Random;

public class Main2 {
    public static void main(String[] args) {
        Random rand = new Random();
        
        int[] generated = new int[5];  // stores the numbers we've picked
        int count = 0;

        while (count < 5) {
            int num = rand.nextInt(10) + 1;  // random 1–10

            // Check if num was already generated
            boolean alreadyExists = false;
            for (int i = 0; i < count; i++) {
                if (generated[i] == num) {
                    alreadyExists = true;
                    break;
                }
            }

            // Only add if it's new
            if (!alreadyExists) {
                generated[count] = num;
                count++;
                System.out.println(num);
            }
        }
    }
}