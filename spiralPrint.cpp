#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void display(vector<vector<int>> A)
{
    if (A.size() == 0)
        return;

    else if (A[0].size() == 0)
        return;

    else
    {
        for (int i = 0; i < A.size(); i++)
        {
            for (int j = 0; j < A[i].size(); j++)
            {
                cout << A[i][j] << " ";
            }

            cout << endl;
        }
        cout << endl;
    }
}

void spiral_print(vector<vector<int>> matrix, int val)
{
    int number_of_rows = matrix.size();
    int number_of_cols = matrix[0].size();
    int short_side = min(number_of_cols, number_of_rows);

    int max_col = number_of_cols - val - 1;
    int max_row = number_of_rows - val - 1;


    if (2 * val >= short_side)            //error check
        return;

    else
    {
        for (int j = val; j < max_col; j++)            //top row
            cout << matrix[val][j] << " ";

        for (int i = val; i < max_row; i++)            //rightmost column
            cout << matrix[i][max_col] << " ";


        if (max_row == val)
        {
            cout << matrix[val][max_col] << " ";
            return;
        }

        else if (max_col == val)
        {
            cout << matrix[max_row][val] << " ";
            return;
        }

        for (int j = max_col; j > val; j--)            //bottom row
            cout << matrix[max_row][j] << " ";

        for (int i = max_row; i > val; i--)            //leftmost column
            cout << matrix[i][val] << " ";
    }

}

void spiral_print(vector<vector<int>> matrix)
{
    int val = 0;

    int number_of_rows = matrix.size();
    int number_of_cols = matrix[0].size();
    int short_side = min(number_of_cols, number_of_rows);

    while (2 * val < short_side)
    {
        spiral_print(matrix, val);

        val++;
    }



    /*
    int number_of_rows = matrix.size();
    int number_of_cols = matrix[0].size();               //assume all rows of the matrix have the same size


    for (int i = 0; i < floor((number_of_rows + 1) / 2); i++)
    {
        for (int j = i; j < number_of_cols - i; j++)
            cout << matrix[i][j] << " ";

        for (int j = i + 1; j < number_of_rows - i; j++)
            cout << matrix[j][number_of_cols - i - 1] << " ";

        for (int j = number_of_cols - i - 2; j >= i; j--)
            cout << matrix[number_of_rows - i - 1][j] << " ";

        for (int j = number_of_rows - i - 2; j > i; j--)
            cout << matrix[j][i] << " ";
            */
}
/*
int main()
{
    vector<vector<int>> A = {{1,2,3,7,7}, {1,5,6,8,9}, {6,1,5,2,2}, {8,6,3,4,8}, {6,7,1,2,7}, {1,9,3,8,0}, {1,6,3,2,6}};
   // vector<vector<int>> A = {{1,2,3,4,5,1,5,3}, {4,5,6,7,8,6,3,7}, {4,2,5,1,6,9,5,2}};
    display(A);
    spiral_print(A);

    return 0;
}
*/
