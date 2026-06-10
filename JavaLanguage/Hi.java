import java.io.FileInputStream;
import java.io.IOException;

public class Hi {

    public static void main(String[] args) {
        try {
        FileInputStream file = new FileInputStream("Budots.mp3");

        int i;

        while ((i = file.read()) != -1) {
            System.out.print((char)i);
        }
        file.close();
        } catch (IOException e) {
            System.out.println("Something Error On a File");
        }
    }
}