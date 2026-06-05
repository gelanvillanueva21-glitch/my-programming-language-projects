package DSA;

public class Prac5ArrayList {
    public static void main(String[] args) {
        Dynamic_Array dynamic_Array = new Dynamic_Array(5);

        dynamic_Array.add("A");
        dynamic_Array.add("B");
        dynamic_Array.add("C");
        dynamic_Array.add("G");
        dynamic_Array.add("N");
        dynamic_Array.delete("A");
        dynamic_Array.delete("B");
        dynamic_Array.delete("C");

        //dynamic_Array.insert(0, "X");
        //dynamic_Array.delete("A");
        //System.out.println(dynamic_Array.search("C"));
        System.out.println(dynamic_Array);
        System.out.println("Size: " + dynamic_Array.size);
        System.out.println("Capacity: " + dynamic_Array.capacity);
        System.out.println("Empty: " + dynamic_Array.isEmpty());

        //System.out.println(dynamic_Array.capacity);
    }
    
} class Dynamic_Array {

    int size = 0;
    int capacity;
    Object[] array;

    public Dynamic_Array() {
        this.array = new Object[capacity];
    }
    public Dynamic_Array(int capacity) {
        this.capacity = capacity;
        this.array = new Object[capacity];
    }

    public void add(Object data) {
        if (size >= capacity) {
            grow();
        }
        array[size] = data;
        size++;
    }
    public void insert(int index, Object data) {
        if (size >= capacity) {
            grow();
        }
        for (int i = size; i > index; i--) {
            array[i] = array[i - 1];
        }
        array[index] = data;
        size++;
    }
    public void delete(Object data) {
        
        for (int i = 0; i < size; i++) {
            if (array[i] == data) {
                for (int j = 0; j < (size - i - 1); j++) {
                    array[i + j] = array[i + j + 1];
                }
                array[size - 1] = null;
                size--;
                if (size <= (capacity/3)) {
                    shrink();
                }
                break;
            }
            
        }
    }
    public int search(Object data) {

        for (int i = 0; i < size; i++) {
            if(array[i] == data) {
                return i;
            }
        }
        return -1;
    }
    public void grow() {

        int newCapacity = (int)(capacity * 2);
        Object[] newArray = new Object[newCapacity];

        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        capacity = newCapacity;
        array = newArray;
    }
    private void shrink() {

        int newCapacity = (int)(capacity / 2);
        Object[] newArray = new Object[newCapacity];

        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        capacity = newCapacity;
        array = newArray;
    }
    public boolean isEmpty() {
        return size == 0;
    }
    public String toString() {

        String string = "";

        for (int i = 0; i < size; i++) {
            string += array[i] + ", ";
        }
        if (string != "") {
            string = "["+string.substring(0, string.length() - 2)+"]";
        } else {
            string = "[]";
            }
        return string;
    }
}