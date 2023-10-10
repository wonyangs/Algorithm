// Solved on 2023. 10. 10.
// 2578 빙고

#include <algorithm>
#include <array>
#include <iostream>

using namespace std;

void updateArr(const array<array<int, 5>, 5>& arr,
               array<array<bool, 5>, 5>& check, int n) {
  for (auto i = 0u; i < arr.size(); ++i) {
    for (auto j = 0u; j < arr[i].size(); ++j) {
      if (arr[i][j] == n) {
        check[i][j] = true;
        return;
      }
    }
  }
}

bool isBingo(const array<array<bool, 5>, 5>& check) {
  int bingoCnt = 0;

  for (const auto& row : check) {
    if (all_of(row.begin(), row.end(), [](bool v) { return v; })) ++bingoCnt;
  }

  for (auto j = 0u; j < check.size(); ++j) {
    bool isBingo = true;
    for (auto i = 0u; i < check[j].size(); ++i) {
      if (!check[i][j]) {
        isBingo = false;
        break;
      }
    }
    if (isBingo) ++bingoCnt;
  }

  bool isBingo1 = true, isBingo2 = true;

  for (auto i = 0u; i < check.size(); ++i) {
    if (!check[i][i]) isBingo1 = false;
    if (!check[i][4 - i]) isBingo2 = false;
  }

  bingoCnt += isBingo1 + isBingo2;

  return bingoCnt >= 3;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  array<array<int, 5>, 5> arr{};
  array<array<bool, 5>, 5> check{};

  // Read in the input
  for (auto& row : arr) {
    for (auto& num : row) cin >> num;
  }

  // Update and Check Bingo
  int n = 0, i = 0;

  while (i < 25) {
    cin >> n;
    updateArr(arr, check, n);
    if (isBingo(check) == true) {
      cout << i + 1 << endl;
      break;
    }
    i++;
  }

  return 0;
}
