#include <iostream>
#include <vector>

using namespace std;

int dijkstra(vector<vector<int>> matrix, int source, int dest)
{
    int N = matrix.size();

    //an array that stores shortest distance from source to destination
    int dist[N];

    //array that stores the visited nodes
    bool visited[N];

    //initializing values
    for (int i = 0; i < N; i++)
        dist[i] = INT_MAX, visited[i] = false;

    //distance to source node is zero
    dist[source] = 0;

    //run through the remaining N-1 vertices updating the dist array
    for (int j = 0; j < N - 1; j++)
    {
        //calculate the index of the closest node which has not been visited
        int minIndex;
        int minValue = INT_MAX;

        for (int i = 0; i < N; i++)
        {
            if (dist[i] <= minValue && visited[i] == false)
            {
                minValue = dist[i];
                minIndex = i;
            }
        }

        //set the minIndex as visited
        visited[minIndex] = true;

        //update the distances for vertices adjacent to minIndex
        for (int i = 0; i < N; i++)
        {
            /*only update if:
            -node i has not been visited
            -there is an edge between minIndex and i
            -the distance to minIndex is not INT_MAX (this will only happen if the graph is not connected)
            -finally, the distance to minIndex plus the edge length from minIndex to i does not exceed the current distance value for node i
            */
            if (visited[i] == false && matrix[minIndex][i] > 0 && dist[minIndex] < INT_MAX && dist[minIndex] + matrix[minIndex][i] < dist[i])
                dist[i] = dist[minIndex] + matrix[minIndex][i];
        }
    }

    if (dist[dest] < INT_MAX)
        return dist[dest];

    else
        return -1;
}

int main()
{
    vector<vector<int>> matrix =

    {{0,1,0,0},
    {1,0,0,0},
    {0,0,0,1},
    {0,0,1,0}};

    cout << dijkstra(matrix,0,3);

    return 0;
}
