#include <deque>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int getBridgeWeight(deque<pair<int, int>> const& bridge) {
  int totalWeight = 0;

  for (auto const& [weight, _] : bridge) {
    totalWeight += weight;
  }

  return totalWeight;
}

void updateBridge(deque<pair<int, int>>& bridge, int W) {
  for (auto& [_, time] : bridge) {
    time += 1;
  }

  if (!bridge.empty()) {
    auto const& [_, time] = bridge.front();
    if (time == W) {
      bridge.pop_front();
    }
  }
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N, W, L;

  cin >> N >> W >> L;

  vector<int> trucks(N);
  for (int i = 0; i < N; ++i) {
    cin >> trucks[i];
  }

  deque<pair<int, int>> bridge;
  int time = 0;
  int cnt = 0;

  while (true) {
    if (cnt == N and bridge.empty()) {
      cout << time << endl;
      break;
    }

    updateBridge(bridge, W);

    if (auto p = pair{trucks[cnt], 0};
        bridge.size() < static_cast<size_t>(W) and cnt < N and
        getBridgeWeight(bridge) + trucks[cnt] <= L) {
      bridge.push_back(p);
      ++cnt;
    }

    ++time;
  }

  return 0;
}
