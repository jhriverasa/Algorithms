import java.util.*;
import java.lang.*;
import java.io.*;

class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		  System.out.println("Enter an n:");
 
        int n= 30; //put your n
        int A[][] = new int[n][n];
        int B[][] = new int[n][n];
        int C[][] = new int[n][n];
        long mean =0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                A[i][j]=1;
                B[i][j]=2;          
            }
        }
        long startTime = System.nanoTime();
        for(int row=0;row<n;row++){   
            for(int col=0;col<n;col++){
                int result=0;
                for(int m=0;m<n;m++){
                    
                    result= result + A[row][m]*B[m][col];   
                   
                    
                    
                }
                C[row][col] = result;
                //System.out.print(result + " ");
            }
              //System.out.print("\n");
        }
         long endTime = System.nanoTime();
         long duration = (endTime - startTime);
         System.out.println(duration + " ns.");
        //System.out.println("---------");
        //System.out.println("Avg: "+ mean/(n*n*n)+ " ms.");
	}
}
