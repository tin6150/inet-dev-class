
compiling this package called beagle for use with GPU.
oh hmm... need to be on a gpu node...
beagle: https://github.com/beagle-dev/beagle-lib/wiki/LinuxInstallInstructions


  use n0262.savio3
  2x A40 nvidia.  not great, the FP64 for this is low, TFlops of 1.169 (1:32)
     K80  has 1.37 (1:3).
     V100 has 7.06 (1:2)


####


module load cmake/3.22.0    # from consultsw
module load java/1.8.0_121
module load cuda/11.2


git clone --depth=1 https://github.com/beagle-dev/beagle-lib.git
cd beagle-lib
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=$HOME ..
make install


### to use

export LD_LIBRARY_PATH=$HOME/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$HOME/lib/pkgconfig:$PKG_CONFIG_PATH
