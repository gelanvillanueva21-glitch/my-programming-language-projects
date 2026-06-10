import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Practice {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter Something: ");
    String word = sc.nextLine();
    try {
      File myObj = new File("filename.txt");
      FileWriter filewrite = new FileWriter("filename.txt");
      filewrite.write("I am Gelan Mar G Villanueva\nAnd I Love Chanzine So MUCHHHHH\n" + word);
      filewrite.close();
      if (myObj.createNewFile()) {
        System.out.println("File created: " + myObj.getName());
      } else {
        System.out.println("File already exists.");
      }
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    sc.close();
  }
}