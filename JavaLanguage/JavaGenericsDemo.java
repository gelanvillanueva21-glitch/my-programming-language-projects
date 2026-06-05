import java.io.*;
import java.util.*;
import java.lang.reflect.Array;
import java.util.Arrays;
import javax.swing.*;
import java.awt.*;


public class JavaGenericsDemo {

    // Generic method to convert primitive int[] to T[]
    public static <T> T[] convert(int[] primitiveArray, Class<T> clazz) {
        if (primitiveArray == null) {
            throw new IllegalArgumentException("Input array cannot be null");
        }
        if (clazz == null) {
            throw new IllegalArgumentException("Class type cannot be null");
        }

        // Create a new generic array of the wrapper type
        @SuppressWarnings("unchecked")
        T[] result = (T[]) Array.newInstance(clazz, primitiveArray.length);

        // Box each primitive into its wrapper type
        for (int i = 0; i < primitiveArray.length; i++) {
            result[i] = clazz.cast(primitiveArray[i]); // Autoboxing
        }
        return result;
    }

    public static double Average(int[] a){
		int Sum=0;
		for (Integer n: a){Sum+=n;}
		return (Sum/a.length);
	}

    public static void main(String[] args) throws IOException, InterruptedException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		//Gene<Integer> i = new Gene<>();
        String 	text, nums[], names[], charRegEx, nameRegEx;
        int		noel;
        boolean repeat=false;
        //char	charArr[];

		new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
		try {
			do {
				System.out.print("Type at least seven (7) integers separated by punctuation marks or common value separators : \n\t");
				text = bf.readLine();
				nums = text.split("[,.;: \\|\\?\\<\\>\\(\\)\\[\\]\\{\\}/&]+");
				noel = nums.length;
				System.out.print(Arrays.toString(nums));System.out.printf("\tNumber of Elements is %d\n",noel);
				if (noel<7) {
					System.out.println("The integers you entered are fewer than the minimum requirement.\n");repeat=true;
				}
				else repeat=false;
			} while (repeat);

			int[] arr= new int[noel];
			for (int cnt=0; cnt < noel; cnt++) {
				try {
					arr[cnt] = Integer.parseInt(nums[cnt]);
				} catch (NumberFormatException e) {
					System.out.printf("%s is not a valid number!",nums[cnt]);
				}
			}
			Integer[] b = convert(arr, Integer.class);
			System.out.print("\n\tTheir Sorted Version :");
        	sort_generics(b);
        	System.out.printf("\tTheir Average        :%.2f\n\n",Average(arr));
		} catch (IndexOutOfBoundsException e) {
			System.out.printf("Error has been found: %s\n\n",e.getMessage());
		}

		try {
			do {
				System.out.print("Type exactly 10 of your classmates by their first names separated by pipes : \n\t");
				text = bf.readLine();
				names = text.split("[ \\|]+");
				nameRegEx = "[A-Z a-z.\\|]+";
				System.out.print(Arrays.toString(names));System.out.printf("\tNumber of Elements is %d\n",names.length);
				if (names.length!=10 || !text.matches(nameRegEx)) {
					repeat=true;
					System.out.println("Names entered aren't exactly 10 or names contain foreign characters ...\n");
				}
				else repeat=false;
			} while (repeat);
			System.out.print("\n\tTheir Sorted Version : ");
        	sort_generics(names);
		} catch (IndexOutOfBoundsException e) {
			System.out.printf("Error has been found: %s\n\n",e.getMessage());
		}

		try {
			do {
				System.out.printf("Type exactly a dozen consonants in the English alphabet with no space or separator between :\n\t");
				text = bf.readLine().trim();
				charRegEx = "[^AEIOUaeiou]{12}";
				if (!text.matches(charRegEx)) {
						System.out.println("You didn't follow the instruction. Try again ...\n");
						repeat=true;
				} else repeat=false;
			} while (repeat);
			noel = text.length();

			Character[] charArr = new Character[noel];

			for (int i = 0; i < noel; i++) {
				charArr[i] = text.charAt(i); // autoboxing from char to Character
			}
			System.out.println("\nThe Consonants you entered are :"+Arrays.toString(charArr));
			System.out.print("\n\tTheir Sorted Version : ");
			sort_generics(charArr);

		} catch (IndexOutOfBoundsException e) {
				System.out.printf("Error has been found: %s\n\n",e.getMessage());
		}
		UIManager.put("OptionPane.background", Color.ORANGE);
        UIManager.put("OptionPane.messageForeground", Color.RED);
        UIManager.put("OptionPane.buttonForeground", Color.BLUE);
        UIManager.put("OptionPane.buttonFont", new Font("Alegreya SC", Font.BOLD, 16));
        UIManager.put("OptionPane.messageFont", new Font("Rockwell Condensed", Font.BOLD, 16));
        UIManager.put("Panel.messageForeground", Color.RED);
        UIManager.put("Panel.messageFont", new Font("Rockwell Condensed", Font.BOLD, 16));
        UIManager.put("Panel.buttonFont", new Font("Rockwell Condensed", Font.BOLD, 16));
        UIManager.put("Panel.background", Color.YELLOW);

        Object[] options = {"Clueless", "Rising", "Sinking", "Neither"};
        Object clicked = JOptionPane.showInputDialog(
                null,
                "How are array elements were sorted ...",
                "Your Observation",
                JOptionPane.QUESTION_MESSAGE,
                null,
                options,
                options[0]
        );
        System.out.printf("\nYou clicked: %s\n", clicked);
    }

    // Generic bubble sort for Comparable types
    public static <T extends Comparable<T>> void sort_generics(T[] a) {
        int x, y;
        T temp;
        for (x = 0; x < a.length - 1; x++) {
            for (y = x + 1; y < a.length; y++) {
                if (a[x].compareTo(a[y]) < 0) {
                    temp = a[x];
                    a[x] = a[y];
                    a[y] = temp;
                }
            }
        }
    }
}

