#ifndef tiles_h
#define tiles_h

#include <vector>

template<typename T, uint8_t Ndim>
class tiles{
private:
    std::vector<std::vector<int>> tiles_;
public:
    tiles() {}
    void resizeTiles() { tiles_.resize(nTiles); }

    int nTiles;
    std::array<float,Ndim> tilesSize;

    int getGlobalBin(std::vector<T> coords) const {
      int globalBin = getBin(coords[0]);
      int nTilesPerDim = std::pow(NTiles,1.0/Ndim);
      for(int i = 1; i != N; ++i) {
        globalBin += nTilesPerDim*getBin(coords[i]);
      }
      return globalBin;
    }

    int getGlobalBinByBin(std::vector<int> Bins) const {
      int globalBin = Bins[0];
      int nTilesPerDim = std::pow(NTiles,1.0/Ndim);
      for(int i = 1; i != N; ++i) {
        globalBin += nTilesPerDim*Bins[i];
      }
      return globalBin;
    }

    int getBin(std::vector<T> coords_, int dim_) const {
      constexpr float Range = LayerTilesConstants::maxCoord - LayerTilesConstants::minCoord;
      static_assert(Range>=0.);
      int coord_Bin = (coord_ - LayerTilesConstants::minCoord)*LayerTilesConstants::rCoord;
      coord_Bin = std::min(coord_Bin,LayerTilesConstants::nLines-1);
      coord_Bin = std::max(coord_Bin,0);
      return coord_Bin;
    }

    void fill(std::vector<T> coords, int i) {
      tiles_[getGlobalBin(coords)].push_back(i);
    }

    void fill(std::array<std::vector<T>,Ndim> const& coordinates) {
      auto cellsSize = coordinates[0].size();
      for(int i = 0; i < cellsSize; ++i) {
        std::vector<T> bin_coords;
        for(int j = 0; j != N; ++j) {
          bin_coords.push_back(coordinates[j][i]);
        } 
        layerTiles_[getGlobalBin(bin_coords)].push_back(i);
      }
    }

    std::array<int,2*Ndim> searchBox(std::array<std::vector<T>,Ndim> minMax_){   // {{minX,maxX},{minY,maxY},{minZ,maxZ},....}
      std::array<int, 2*Ndim> minMaxBins;
      int j = 0;
      for(int i = 0; i != Ndim; ++i) {
        minMaxBins[j] = getBin(minMax_[i][0]);
        minMaxBins[j+1] = getBin(minMax_[i][1]);
        j += 2;
      }

      return minMaxBins;
    }

    void clear() {
      for(auto& t: tiles_) {
        t.clear();
      }
    }

    std::vector<int>& operator[](int globalBinId) {
      return tiles_[globalBinId];
    }
};

#endif