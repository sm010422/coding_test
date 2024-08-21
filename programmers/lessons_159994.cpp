#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    
    vector<string> new_card1;
    vector<string> new_card2;
    
    vector<string> compare_c1;
    vector<string> compare_c2;
    
    int c1_result = true;
    int c2_result = true;
    
    string result;
    
    
    for(int i = 0; i < goal.size(); i++){
        for(int a = 0; a < cards1.size(); a++){
            if(goal[i] == cards1[a]){
                new_card1.push_back(goal[i]);
                
            }
        }
        
        for(int b = 0; b < cards2.size(); b++){
            if(goal[i] == cards2[b]){
                new_card2.push_back(goal[i]);
                
            }
        }
        
    }
    
    for(int i = 0; i < new_card1.size(); i++){
        if(cards1[i] != new_card1[i]){
            c1_result = false;

        }
    }
    

    
    for(int i = 0; i < new_card2.size(); i++){
        if(cards2[i] != new_card2[i]){
            c2_result = false;

        }
    }

    
    
    if(c1_result && c2_result){
        result = "Yes";
    }
    else{
        result = "No";
    }

    cout << result << endl;
    
    string answer = result;
    return answer;
}
