class Solution {
public:
int applyOp(string op, int a, int b) {
    if (op == "+") return a + b;
    if (op == "-") return a - b;
    if (op == "*") return a * b;
    if (op == "/") return a / b;
    return 0;
}
    int evalRPN(vector<string>& tokens) {
        stack<int> st;  // separate stack, not tokens

         for (string& token : tokens) {
         if (token == "+" || token == "-" || 
                token == "*" || token == "/") {
                int b = st.top(); 
                st.pop();
                int a = st.top(); 
                st.pop();
                st.push(applyOp(token, a, b));

                }
                else
                    st.push(stoi(token));
//Notes for later:
                //somewhere we need to change the is firstassgined flag to false!
          
        }
        return st.top();

    }
    
};
