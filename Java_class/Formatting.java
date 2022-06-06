import java.text.NumberFormat;

public class Formatting {
    public static void main(String[] args) {
        // $1,424,567
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String result = currency.format(1234567.891);
        System.out.println(result);
        // NumberFormat per = NumberFormat.getPercentInstance().format(0.1);
        String res = NumberFormat.getPercentInstance().format(0.1);
        System.out.println(res);
    }    
}
