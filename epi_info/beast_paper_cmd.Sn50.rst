**^ tin n0262.savio3 ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**>
# n0262.savio3 (not in slurm yet, so direct run in ssh)
this is the command running as per ps
java -cp beast.jar dr.app.beast.BeastMain -seed 2020 -beagle_double -beagle_gpu -save_every 1000000 -save_state travelHist.checkpoint ../files/Protocol3/282_GISAID_sarscov2_travelHist_masked.xml


# instructions from README / pdf

export LD_LIBRARY_PATH=$HOME/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$HOME/lib/pkgconfig:$PKG_CONFIG_PATH

java -cp beast.jar dr.app.beast.BeastMain -seed 2020 -beagle_double -beagle_gpu -save_every 1000000 -save_state travelHist.checkpoint   \
  ../files/Protocol3/282_GISAID_sarscov2_travelHist_masked.xml   # 10 days on n0262.s3 A40 gpu, cuda 11.2.



eventually run Rstudio
see beast_paper_nCoV2.Rmd

