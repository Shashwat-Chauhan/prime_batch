#include<iostream>
#include <algorithm>
#include<vector>
using namespace std;
// Given an array , return all the unique subsequences which result to a target value

void print(vector<int> arr){
    for(int i = 0 ; i < arr.size() ; i++){
        cout << arr[i] << " ";
    }
}

int main(){
    vector<int> arr = {1 , 2 , 3 , 1 , 2 , 4 , 6};
    sort(arr.begin() , arr.end());

    
    void find_subsequences(vector<int> arr , int target){
        vector<int> res = {};
        vector<int> temp;

        void backtrack(int idx , int curr_sum){
            if idx >= n{
                if curr_sum == target{
                    res.pushback(temp)      
                }
            }
        }
    }


    return 0;
    
}

