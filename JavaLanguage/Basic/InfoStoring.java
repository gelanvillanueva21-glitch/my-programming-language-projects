import java.util.InputMismatchException;
import java.io.IOException;
import java.io.FileWriter;
import java.util.Scanner;

public class InfoStoring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.println("How many info you want to store");
            System.out.print("Enter: ");
            int size = sc.nextInt();

            String[] name = new String[size];
            int[] age = new int[size];
                sc.nextLine();
            for (int i = 0; i < size; i++) {
                System.out.print("Enter Name: ");
                name[i] = sc.nextLine();
                System.out.print("Enter Age: ");
                age[i] = sc.nextInt();

                sc.nextLine();
            }

            FileWriter filewrite = new FileWriter("Info.txt", true);

            for (int i = 0; i < size; i++) {
                filewrite.write("Name: " + name[i] + "\nAge: " + age[i] + "\n\n");
            }
                filewrite.close();
                System.out.println("Stored Succesfull");

        } catch (InputMismatchException e) {

            System.out.println("Your Input Is Incorrect!");
 
        } catch (StringIndexOutOfBoundsException e) {

            System.out.println("Index Not Found!");

        } catch (IOException e) {

            System.out.println("Can't Find File!");

        }
        sc.close();
    }
    
}
