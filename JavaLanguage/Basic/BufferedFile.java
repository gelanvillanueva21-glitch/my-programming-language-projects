package Basic;

//import java.io.BufferedReader;
//import java.io.BufferedWriter;
//import java.io.FileReader;
//import java.io.FileWriter;
//import java.io.IOException;
//import java.io.FileInputStream;
import java.io.*;
import java.util.InputMismatchException;
import java.util.Scanner;

public class BufferedFile {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String words_in_file;

        
        try {
            System.out.println("Choose File:");
            System.out.print("> ");
            String file_name = sc.nextLine();

            BufferedReader read = new BufferedReader(new FileReader(file_name));
            BufferedWriter writer = new BufferedWriter(new FileWriter(file_name, true));
            FileInputStream input = new FileInputStream(file_name);
            while (true) {
            sc.nextLine();
                System.out.println("1. Write To The File\n2. Read The File\n3. Read The Bytes Of The File\n4. Exit");
                System.out.print("> ");
                int choose = sc.nextInt();
                String words = "";
                if (choose == 1) {
                    System.out.print("> ");
                    words = sc.nextLine();

                    writer.write(words);
                    writer.flush();
                } else if (choose == 2) {
                    while ((words_in_file = read.readLine()) != null) {
                        System.out.println(words_in_file);
                        System.out.println(words);
                    }
                } else if (choose == 3) {
                    int i;
                    while ((i = input.read()) != -1) {
                        System.out.print((char) i);
                    } input.close();
                
                } else if (choose == 4) {
                    break;
                } else {
                    System.out.println("Wrong Input!");
                }
            
                read.close();
                writer.close();
            }

        } catch (InputMismatchException e) {
            System.out.println("Wrong Input!");
        } catch (IOException e) {
            System.out.println("Something Error Occured On File");
        }
        sc.close();
    }
}