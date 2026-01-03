#include <bits/stdc++.h>
using namespace std;

static vector<int> A_global, B_global;

void initialize(vector<int> A, vector<int> B) {
    A_global = A;
    B_global = B;
}

int answer_question(int i, int j) {
    return A_global[i] + B_global[j];
}