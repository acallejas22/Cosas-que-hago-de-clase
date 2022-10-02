package principal;
import java.util.Scanner;

public class Input {

    static Scanner input = new Scanner (System.in);


  public static void main(String[] args) 
  {

    Scanner input = new Scanner(System.in);
     
    System.out.print  ("ingresa la primera nota: ");
    float n1 = input.nextFloat();
    System.out.print  ("ingresa la segunda nota: ");
    float n2 = input.nextFloat();
    System.out.print  ("ingresa la tercera nota: ");
    float n3 = input.nextFloat();
 

   double media = (float)((n1 + n2 + n3)/30)*10;
   

  

    
   
    System.out.println("La media de notas es: " + media ); 

  }

}
