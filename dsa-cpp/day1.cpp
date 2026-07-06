// #include<iostream>
// using namespace std;
// int main()
// {
//     int n;
//     cin>>n;
//     int arr[n];
//     for(int i=0;i<n;i++)
//     {
//         cin>>arr[i];
//     }
//     for(int i=0;i<n;i++)
//     {
//         cout<<arr[i]<<" ";
//     }
//     // return 0;
//     // max element in the array
//     int max=arr[0];
//     for(int i=0;i<n;i++){ 
//         if(arr[i]>max){
//             max=arr[i];
//         }
//     }
//     cout<<"\n"<<max;
//     return 0;
// }
// #include <iostream>
// #include<vector>
// #include<algorithm>
// using namespace std;
// int main(){
//     int n;
//     cout<<"enter the size of the vetor:";
//     cin>>n;
//     vector<int> v;
//     for (int i=0;i<n;i++){
//         int x;
//         cout<<"element"<<i+1<<": ";
//         cin>>x;
//         v.push_back(x);
//     }
//     cout<<"\nbefore sorting:";
//     for(int i=0;i<v.size();i++){
//         cout<<v[i]<<" ";
//     }
//     cout<<endl;
//     sort(v.begin(),v.end());
//     cout<<"after sorting:";
//     for(int i=0;i<v.size();i++){
//         cout<<v[i]<<" ";
//     }
//     cout<<endl;
//     return 0;
// }

#include<iostream>
#include<unordered_map>
using namespace std;
int main(){
    int n;
    cout<<"enter the size of the array:";
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cout<<"element"<<i+1<<": ";
        cin>>arr[i];
    }
    unordered_map<int,int> m;
    for(int i=0;i<n;i++){
        m[arr[i]]++;
}
cout<<"\nFrequency:\n";
for(auto pair: m){
    cout<<pair.first<<" "<<pair.second<<endl;
}
return 0;
}