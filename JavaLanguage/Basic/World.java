import java.io.File;

public class World {
    public static void main(String[] args) {
        File obj = new File("Info.txt");
        if (obj.delete()) {
            System.out.println("File Delted");
        } else {
            System.out.println("Failed TO Delete");
        }
    }
}
