package DSA_Exercise;

import java.util.*;

public class Number_Sorting {

    private static ArrayList<Integer> num_List = new ArrayList<>();

    public static void main(String[] args)throws InputMismatchException {

        Scanner sc = new Scanner(System.in);

        try {
            System.out.println("Enter How Many Numbers To Store:");
            System.out.print("> ");
            int num = sc.nextInt();

            while (num >= 1) {
                System.out.print("Enter Random Number: ");
                num_List.add(sc.nextInt());
                num--;
            }
        } catch (InputMismatchException e) {
            System.out.println("Wrong Input!");
            System.out.println("Input A Number!");
        }

        int[] temporary_array = new int[num_List.size()];

        duplication(temporary_array);
        Merge_Sort.merge_Sort(temporary_array);
        rewrite(temporary_array);
        System.out.println(num_List);
        for (int i : temporary_array) {
            System.out.print(i + " ");
        }
        try {
            System.out.println();
            System.out.println("Enter Number To Search:");
            System.out.println("> ");
            int num_search = sc.nextInt();

            int result = binary_Search(num_search, temporary_array);
            if (result != -1) {
                System.out.println("Target Found At Index: " + num_search);
            } else {
                System.out.println("Target Not Found");
            }
        } catch (InputMismatchException e) {
            System.out.println("Wrong Input!");
            System.out.println("Input A Number!");
        }
        

        sc.close();
    } private static class Merge_Sort {
        private static void merge_Sort(int[] array) {

        int length = array.length;
        if (length <= 1) {
            return;
        }

        int middle = length / 2;
        int[] leftArray = new int[middle];
        int[] rightArray = new int[length - middle];

        int i = 0;
        int j = 0;

        for (; i < length; i++) {
            if (i < middle) {
                leftArray[i] = array[i];
            } else {
                rightArray[j] = array[i];
                j++;
            }
        }
        merge_Sort(leftArray);
        merge_Sort(rightArray);
        merge(leftArray, rightArray, array);
        } private static void merge(int[] leftArray, int[] rightArray, int[] array) {

            int leftSize = array.length / 2;
            int rightSize = array.length - leftSize;
            int i = 0, l = 0, r = 0;

            while (l < leftSize && r < rightSize) {
                if (leftArray[l] < rightArray[r]) {
                    array[i] = leftArray[l];
                    i++;
                    l++;
                } else {
                    array[i] = rightArray[r];
                    i++;
                    r++;
                }
            }
            while (l < leftSize) {
                array[i] = leftArray[l];
                i++;
                l++;
            }
            while (r < rightSize) {
                array[i] = rightArray[r];
                i++;
                r++;
            }

        }
    }private static int binary_Search(int target, int[] temporary_array) {

        int left = 0;
        int right = temporary_array.length - 1;

        while (left <= right) {
            int middle = left + (right - left) / 2;

            if (target == temporary_array[middle]) {
                return middle;
            } else if (temporary_array[middle] > target) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        return -1;

    } private static void duplication(int[] temporary_array) {

        int index = 0;
        for (int num : num_List) {
            temporary_array[index] = num;
            index++;
        }

    } private static void rewrite(int[] temporary_array) {

        num_List.clear();
        for (int index = 0; index < temporary_array.length; index++) {
            num_List.add(temporary_array[index]);
        }

    }
}
