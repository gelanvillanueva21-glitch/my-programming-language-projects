import java.io.File;
import java.io.FileNotFoundException;
import java.util.InputMismatchException;
import java.util.Scanner;

public class FilePractice {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        
        
        try {
        System.out.println("-----AVAILABLE-----\n1. Read File\n2. Delete File");
        System.out.print("Enter: ");
        int choose = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter File: ");        
        String fileNAme = sc.nextLine();
        
        File object = new File(fileNAme);
        if (choose == 1) {
            Scanner reader = new Scanner(object);
            while (reader.hasNextLine()) {
                String data = reader.nextLine();
                System.out.println(data);

            } reader.close();
        } else if (choose == 2) {
            if (object.delete()) {
                System.out.println("File Deleted");
            }
        } else {
            System.out.println("Wrong Input");
        }

        } catch (FileNotFoundException e) {
            System.out.println("Could Not Find File");
        } catch (InputMismatchException e) {
            System.out.println("Wrong Input!");
        }
        sc.close();
    }
}
