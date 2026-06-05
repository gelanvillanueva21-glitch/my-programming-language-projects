import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Hello {
    public static void main(String[] args) {
        File file = new File("info.txt");

        try {
            Scanner reader = new Scanner(file);
            while (reader.hasNextLine()) {
                String info = reader.nextLine();
                System.out.println(info);
            } reader.close();

        } catch (FileNotFoundException e) {
            System.out.println("FIle Not Found");
        }
        
    }
}
