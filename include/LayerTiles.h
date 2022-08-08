#ifndef LayerTiles_h
#define LayerTiles_h


#include <vector>
#include <array>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <iostream>

#include "LayerTilesConstants.h"

template <uint8_t N>
class LayerTiles {
  public:
    LayerTiles(){
      layerTiles_.resize(std::pow(LayerTilesConstants::nLines,N));
    }

    void fill(const std::array<std::vector<float>,N>& coordinates) {
      auto cellsSize = coordinates[0].size();
      for(unsigned int i = 0; i< cellsSize; ++i) {
        std::vector<float> bin_coords;
        for(int j = 0; j != N; ++j) {
          bin_coords.push_back(coordinates[j][i]);
        } 
        layerTiles_[getGlobalBin(bin_coords)].push_back(i);
      }
    }

    void fill(std::vector<float> const& coords, int i) {
      layerTiles_[getGlobalBin(coords)].push_back(i);
    }

    int getBin(float coord_) const {
      constexpr float Range = LayerTilesConstants::maxCoord - LayerTilesConstants::minCoord;
      static_assert(Range>=0.);
      int coord_Bin = (coord_ - LayerTilesConstants::minCoord)*LayerTilesConstants::rCoord;
      coord_Bin = std::min(coord_Bin,LayerTilesConstants::nLines-1);
      coord_Bin = std::max(coord_Bin,0);
      return coord_Bin;
    }
    
    int getGlobalBin(std::vector<float> const& coords) const {
      int globalBin = getBin(coords[0]);
      for(int i = 1; i != N; ++i) {
        globalBin += LayerTilesConstants::nLines*getBin(coords[i]);
      }
      return globalBin;
    }
    
    int getGlobalBinByBin(std::vector<int> const& Bins) const {
      int globalBin = Bins[0];
      for(int i = 1; i != N; ++i) {
        globalBin += LayerTilesConstants::nLines*Bins[i];
      }
      return globalBin;
    }

    std::array<int,2*N> searchBox(std::array<std::vector<float>,N> const& minMax_){   // {{minX,maxX},{minY,maxY},{minZ,maxZ},....}
      std::array<int, 2*N> minMaxBins;
      int j = 0;
      for(int i = 0; i != N; ++i) {
        minMaxBins[j] = getBin(minMax_[i][0]);
        minMaxBins[j+1] = getBin(minMax_[i][1]);
        j += 2;
      }
      return minMaxBins;
    }

    void clear() {
      for(auto& t: layerTiles_) {
        t.clear();
      }
    }

    std::vector<int>& operator[](int globalBinId) {
      return layerTiles_[globalBinId];
    }

  private:
    std::vector<std::vector<int>> layerTiles_;
};


#endif //LayerTiles_h