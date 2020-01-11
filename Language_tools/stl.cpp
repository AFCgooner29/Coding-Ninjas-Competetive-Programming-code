#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> v(5);
    vector<int>::iterator it;
    for(it=v.begin();it<v.end();it++){
        *it=*it+1;
        cout<<*it<<endl;
    }
    return 0 ;
}