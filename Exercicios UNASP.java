// Leia do teclado um valor inteiro, positivo e calcule a média dos números pares entre 0
// e o valor informado pelo usuário. Imprima o resultado da seguinte forma: “A media dos
// primeiros {n} números eh {valor}”, sendo {n} o valor informado e {valor} o valor
// calculado. Se o valor informado for negativo, mostre a mensagem de erro “Erro. Valor
// negativo informado.”. Exemplos:

// Caso 1:
// Valor do teclado: 5
// Resultado: A media dos primeiros 5 números eh 2

// Caso 2:
// Valor do teclado: 20
// Resultado: A media dos primeiros 20 números eh 10

// Caso 3:
// Valor do teclado: -5
// Resultado: Erro. Valor negativo informado.

package Pacote;
import java.util.Scanner;

public class Teste {
    public static void main(String[] args) {

    int valor;
    int par 0;
    double media;
    int count = 0;

    System.out.println("Digite um numero:" ); 
    Scanner nome var scanner = new Scanner(System.in);
    valor = nome_var_scanner.nextInt();

    if(valor < 0) {
        System.out.println("Erro. Valor negativo informado.");
    }else {
        for(int i = 1; i < valor; i++) {
            if(i % 2 == 0) {
                par = i + par;
                count ++;
	  }
	}
	media = par / count;
	System.out.println("A media dos primeros + valor + números ch + media);
   }
}



// Leia do teclado um valor inteiro, positivo e exiba na tela todos os números entre 0 e o
// valor informado que sejam múltiplos de treze, com o seguinte formato {13, 26, 39}. Se
// o valor informado for negativo, mostre a mensagem de erro “Erro. Valor negativo
// informado.”. Exemplos:

// Caso 1:
// Valor do teclado: 30
// Resultado: {13, 26}

// Caso 2:
// Valor do teclado: 100
// Resultado: {13, 26, 39, 52, 65, 78, 91}

// Caso 3:
// Valor do teclado: -5
// Resultado: Erro. Valor negativo informado.

// Caso 4:
// Valor do teclado: 12
// Resultado: {}

package Pacote;
import java.util.Scanner;

public class Teste2 { 
    public static void main(String[] args) {

    int valor;

    System.out.println("Digite um numero multiplo de 13: "); 
    Scanner nome var scanner = new Scanner(System.in);
    valor = nome_var_scanner.nextInt();

    if (valor < 0) {
         System.out.println("Erro. Valor negativo informado." );
    }else{
	 for (int i = 0; i < valor; i++) { 
              if(i % 13 0) {
		  System.out.println("Resultado ("+ i + "}");
              }
           }
        }
    }
}

// Leia do teclado um valor inteiro e verifique se cada número entre 2 e o valor informado
// é um número primo, ou não. A saída deve ser no formato “O numero {n} eh primo” ou
// “O numero {n} nao eh primo”. Se o valor informado for menor ou igual a 1, mostre na
// tela a mensagem “O numero deve ser maior que um”. Exemplos:

// Caso 1:
// Número: 5
// Resultado:
// O numero 2 eh primo
// O numero 3 eh primo
// O numero 4 nao eh primo
// O numero 5 eh primo

// Caso 2:
// Salário: -10
// Resultado: O numero deve ser maior que um

package Pacote;
import java.util.Scanner;

public class Teste3 {
    public static void main(String[] args) {

    int valor;

    System.out.println("Digite um numero:" ); 
    System.out.println("O numero deve ser maior que um");
    Scanner nome var scanner = new Scanner(System.in); 
    valor nome_var_scanner.nextInt();

    if(valor <= 1) {
	System.out.println("O numero deve ser maior que um" ); 
    }else {
        for (int i = 2 ; i <= valor; i++) {
             int numPrimo = i;
             int numDivisores = 0; 
             for(int j = 1; j <= numPrimo; j++) { 
	         if (numPrimo % j == 0) { 
                     numDivisores++; 
		 }
             }
             if(numDivisores == 2) {
		   System.out.println("O numero "+i+") eh prino"); 
		}else{ 
		    System.out.println("O numero "+i+ ") nao eh prino"); 
		}
	     }
	}
    }
}
