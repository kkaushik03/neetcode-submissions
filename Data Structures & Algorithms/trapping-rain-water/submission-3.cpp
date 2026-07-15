class Solution {
public:
    int trap(vector<int>& height) {

std::vector<int> maxlevel(height.size(), -1); // Size 10, all filled with -1
std::vector<int> minlevel(height.size(), -1); // Size 10, all filled with -1

        int result =0;
        //max level will be this will be backwards 
        //so for index 0 the max level will be at len-1
        maxlevel[height.size()-1]=height[height.size()-1];
        minlevel[0]=height[0];


        for(int i = height.size()-2 ; i>=0; i--){
            int comp1=height.at(i);
            int comp2= maxlevel.at(i+1);

            maxlevel[i]=(max(comp1,comp2));
        }

        

        for(int j = 1; j<=height.size()-1 ; j++){
            int comp1=minlevel.at(j-1);
            int comp2= height.at(j);
            minlevel[j]=(max(comp1,comp2));
        }




        for(int minl:minlevel){
            cout<<minl<<" "; 
        }
        cout<<endl;
          for(int maxl:maxlevel){
            cout<<maxl<<" "; 
        }



        for(int index = 0; index<height.size();index++){
            int midres=  min(minlevel.at(index),maxlevel.at(index));
            result = result + midres - height.at(index);
        }

        return result;
    }
};