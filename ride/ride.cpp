/*
    ID: Shidfar1
    TASK: ride
    LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream fout ("ride.out", std::ios::out);
    ifstream fin ("ride.in", std::ios::in);
    string ufo, group;
    long ufo_mul = 1, group_mul = 1;
    long ascii = 64;
    fin >> ufo;
    fin >> group;

    for (char c : ufo) {
        ufo_mul *= (c - ascii);
    }

    for (char c : group) {
        group_mul *= (c - ascii);
    }
    if ((group_mul % 47) == (ufo_mul % 47))
        fout << "GO" << endl;
    else
        fout <<"STAY" << endl;

    return 0;
}