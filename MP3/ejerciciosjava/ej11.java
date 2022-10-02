package principal;
import java.util.Scanner;

public class Input {

    static Scanner input = new Scanner (System.in);


  public static void main(String[] args) 
  {

    Scanner input = new Scanner(System.in);
    System.out.print  ("ingresa el radio del circulo: ");
    float r = input.nextFloat();
    //float n1 = Integer.parseInt(input.nextFloat());

   
    double pi=(float)3.14159265;
    double sqrt=(float)r*r;
    

    double area = (float)(pi*sqrt);

    double perimetro = (float)(2*pi*r);

  

    
   
    System.out.println("El area del circulo es " + area); 
    System.out.println("El perimetro del circulo es " + perimetro);
    
  }

}
