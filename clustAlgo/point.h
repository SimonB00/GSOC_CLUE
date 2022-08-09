#ifndef Points_h
#define Points_h

#include<vector>
#include<array>
#include<stdint.h>

template <typename T,uint8_t Ndim>
struct Points {
  std::array<std::vector<T>,Ndim> coordinates_;
  std::vector<T> weight;
  
  std::vector<T> rho;
  std::vector<T> delta;
  std::vector<int> nearestHigher;
  std::vector<int> clusterIndex;
  std::vector<std::vector<int>> followers;
  std::vector<int> isSeed;
  int n;

  void clear() {
    for(int i = 0; i != Ndim; ++i) {
      coordinates_[i].clear();
    }
    weight.clear();

    rho.clear();
    delta.clear();
    nearestHigher.clear();
    clusterIndex.clear();
    followers.clear();
    isSeed.clear();

    n = 0;
  }
};
#endif