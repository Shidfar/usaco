/*
    ID: Shidfar1
    TASK: gift1
    LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;


ofstream fout ("gift1.out", std::ios::out);
ifstream fin ("gift1.in", std::ios::in);

void output(map<string, int> &pAccounts, string *order, int n) {
    for (int i = 0; i < n; i++) {
        fout << order[i] << " " << pAccounts[order[i]] << endl;
    }
}

void countForUser(string name, map<string, int> *pAccounts) {
    int loan, friendCount;
    string friendName;
    fin >> loan >> friendCount;

    (*pAccounts)[name] -= friendCount != 0 ? (loan - (loan % friendCount)) : 0;

    int div = friendCount != 0 ? (loan / friendCount) : 0;
    for (int i = 0; i < friendCount; i++) {
        fin >> friendName;
        (*pAccounts)[friendName] += div;
    }
}

void run() {
    map<string, int> accounts;
    int n;
    string username;
    string order[12];

    fin >> n;

    for(int i = 0; i < n; i++) {
        fin >> username;
        order[i] = username;
        accounts[username] = 0;
    }

    for (int i = 0; i < n; i++) {
        fin >> username;
        countForUser(username, &accounts);
    }

    output(accounts, order, n);
}

int main() {
    run();
    return 0;
}