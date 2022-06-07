import java.util.Scanner;

public class Reading {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Age: ");
        byte age = scanner.nextByte();
        System.out.println("You are " + age);
    }
}
