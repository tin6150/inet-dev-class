
Run 1
------

Run 1 started on domingo, using CPU only, as the Quadro 4000 didn't have proper drivers
start: 2022.0605
end:   still running, 9 days and counting
dir:   **^ tin domingo ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**

only use 1 core per htop

screen output for rough idea of performance:
16797000        109.3529        560.1980        -450.8451       2019.94         0.38124         18.0822         1       12.21 hours/million states
16798000        106.3553        554.8540        -448.4987       2019.95         0.28896         17.5313         1       12.21 hours/million states


Run 2
-----

start: 2022.0609 16:53
end:   still running, 5 days and counting
dir:   **^ tin n0264.savio3 ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**

67% gpu util on 1 A40.  
0.7 cpu load avg

the one running on n0262.s3 started on June 9, been 5 days, still running.  
note the FP64 of this A40 GPU is ~0.5 TFlops, well short of the recommended 3+ from the K40c a tutorial/paper referred.  next will try to run on a V100.

screen output for rough idea of performance:

96340000        110.9508        548.3715        -437.4207       2019.96         1.98999E-2      12.3354         1       1.2 hours/million states
96341000        101.0038        525.7903        -424.7866       2019.94         0.13089         14.6711         1       1.2 hours/million states
96342000        99.0277         526.3170        -427.2893       2019.94         0.13891         14.9664         1       1.2 hours/million states
  M  k
# apparently it was specified for chainLength=200M, so it will likely take ~12 days on the A40
# it it took almost 6 days to get to 100M
# 100k took 8.56 min on n0264
# can manually change chainLength in XML to smaller number for quick test
# the GUI also allow choosing FP32 so then it would be much faster, not sure if it needs the accuracy... 
100709000       159.0779        597.6445        -438.5667       2019.97         2.48853E-4      16.0665         1       1.2 hours/million states
100710000       161.2898        597.7857        -436.4959       2019.96         4.60863E-5      16.1708         1       1.2 hours/million states
   M  k

