
// Solution for the kingdom's economy (hackerrank problem) by Jhonatan Rivera S.
//Using floyd-Warshall algorithm (java Implementation) found in :
//https://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/

import java.util.*;
 
class AllPairShortestPath
{
    final static int INF = 99999;
 
    void floydWarshall(int graph[][], int V,int money)
    {
        int dist[][] = new int[V][V];
        int i, j, k;
 
        /* Initialize the solution matrix same as input graph matrix.
           Or we can say the initial values of shortest distances
           are based on shortest paths considering no intermediate
           vertex. */
        for (i = 0; i < V; i++)
            for (j = 0; j < V; j++)
                dist[i][j] = graph[i][j];
 
        /* Add all vertices one by one to the set of intermediate
           vertices.
          ---> Before start of an iteration, we have shortest
               distances between all pairs of vertices such that
               the shortest distances consider only the vertices in
               set {0, 1, 2, .. k-1} as intermediate vertices.
          ----> After the end of an iteration, vertex no. k is added
                to the set of intermediate vertices and the set
                becomes {0, 1, 2, .. k} */
        for (k = 0; k < V; k++)
        {
            // Pick all vertices as source one by one
            for (i = 0; i < V; i++)
            {
                // Pick all vertices as destination for the
                // above picked source
                for (j = 0; j < V; j++)
                {
                    // If vertex k is on the shortest path from
                    // i to j, then update the value of dist[i][j]
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
 
        // Print the shortest distance matrix
        printSolution(dist,V,money);
    }
 
    void printSolution(int dist[][], int V, int money)
    {
        /*
        System.out.println("The following matrix shows the shortest "+
                         "distances between every pair of vertices");
        for (int i=0; i<V; ++i)
        {
            for (int j=0; j<V; ++j)
            {
                if (dist[i][j]==INF)
                    System.out.print("INF ");
                else
                    System.out.print(dist[i][j]+"   ");
            }
            System.out.println();
        }
        */
        //look for the longest path
        int longest= 0;
        for(int i=0;i<V;i++){
            for(int j=0;j<V;j++){
                if (dist[i][j] != INF ){
                    longest = Math.max(longest,dist[i][j]);
                }
            }
        }
        if(longest == 0){
            System.out.println("-1");
        }else{
            System.out.println( longest * money);
        }
        
    }
 
    // Main 
    public static void main (String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int V=sc.nextInt();
        int money=sc.nextInt();
        int graph[][] = new int[V][V];
        
        //fill distance matrix
        for(int i=0;i<V;i++){
            String line = sc.next();
            for(int j=0;j<V;j++){
                if(line.charAt(j) == 'N'){
                    graph[i][j] = INF;
                }
                if(line.charAt(j) == 'Y'){
                    graph[i][j] = 1;
                }
                // distance to itself is zero
                if(i==j)graph[i][j]=0;
            }
        }
        
        
        //print (Matrix)
        /*
        for(int i=0;i<V;i++){
            System.out.println("");
            for(int j=0;j<V;j++){
                if(graph[i][j] == INF){
                    System.out.print("INF ");
                }else{
                    System.out.print(graph[i][j] + " ");
                }
            }
        }
        
        int graph[][] = { {0,   5,  INF, 10},
                          {INF, 0,   3, INF},
                          {INF, INF, 0,   1},
                          {INF, INF, INF, 0}
                        };
        */
        
        AllPairShortestPath a = new AllPairShortestPath();
 
        // Print the solution
        a.floydWarshall(graph,V,money);
    }
}
 
