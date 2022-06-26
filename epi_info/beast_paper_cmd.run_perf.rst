
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
end:   2022.0619 16:13 ie almost 10 days
dir:   **^ tin n0262.savio3 ~/tin-gh/inet-dev-class/epi_info/travHistProtocol/software ^**>
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
# apparently it was specified for chainLength=200M, it end up taking ~10 days on the A40
# (100k took 8.56 min on n0264)
# can manually change chainLength in XML to smaller number for quick test
# the GUI also allow choosing FP32 so then it would be much faster, not sure if it needs the accuracy... 
100709000       159.0779        597.6445        -438.5667       2019.97         2.48853E-4      16.0665         1       1.2 hours/million states
100710000       161.2898        597.7857        -436.4959       2019.96         4.60863E-5      16.1708         1       1.2 hours/million states
   M  k
199998000       90.9418         524.6762        -433.7344       2019.96         0.78733         14.2925         2       1.2 hours/million states
199999000       104.9138        527.2996        -422.3858       2019.94         0.19801         15.3818         2       1.2 hours/million states
200000000       89.1225         510.7208        -421.5982       2019.96         0.20709         15.4647         1       1.2 hours/million states

Operator analysis
Operator                                          Tuning   Count      Time     Time/Op  Pr(accept) Smoothed_Pr(accept)
deltaExchange(gtr.rates)                          3.204   1467976    700035   0.48     0.234       0.19
deltaExchange(frequencies)                        1.348   1464815    700602   0.48     0.234       0.28
scale(alpha)                                      0.125   1466530    2878912  1.96     0.234       0.26
scale(default.clock.rate)                         0.184   4395912    8766378  1.99     0.2339      0.2
up:nodeHeights(treeModel) down:default.clock.rate 0.999   4403426    17661857 4.01     0.234       0.26
scale(location.clock.rate)                        0.496   4402359    25909338 5.89     0.234       0.26
up:nodeHeights(treeModel) down:location.clock.rate 1.0     4397880    17313177 3.94     0.2341      0.2
subtreeSlide(treeModel)                           0.008   44002546   162986692 3.7      0.234       0.26
Narrow Exchange(treeModel)                                43990754   140885523 3.2      0.4706      0.52
Wide Exchange(treeModel)                                  4401436    1295470  0.29     0.0122      0.02
wilsonBalding(treeModel)                                  4400292    25646899 5.83     0.0599      0.05
scale(treeModel.rootHeight)                       0.159   4398821    26150584 5.94     0.2339      0.14
uniform(nodeHeights(treeModel))                           43998106   262954759 5.98     0.7431      0.76
scale(exponential.popSize)                        0.68    4400011    5995378  1.36     0.2341      0.2
exponential.growthRate                            5.499   4399049    5990197  1.36     0.234       0.27
location.coefficients                             10.24   7335322    47341205 6.45     0.2341      0.19
bitFlip(location.coefIndicators)                          7337093    46062190 6.28     0.0763      0.22
location.coefficients                             28.206  7337672    47530264 6.48     0.2338      0.25

9.974227164351852 days

# ie almost 10 days to run on the A40 GPU on n0262.s3
# resulting dir (output files)


-rw-rw-r-- 1 tin users       676 Jun 14 22:50 sn50_cmd.rst
-rw-rw-r-- 1 tin users    150368 Jun 19 16:13 travelHist.checkpoint
drwxrwxr-x 1 tin users       552 Jun 19 16:13 .
-rw-rw-r-- 1 tin users      2159 Jun 19 16:13 282_GISAID_GLM_base.ops
-rw-rw-r-- 1 tin users   1078999 Jun 19 16:13 282_GISAID_GLM_base.log
-rw-rw-r-- 1 tin users    218695 Jun 19 16:13 282_GISAID_GLM_base.location.glm.log
-rw-rw-r-- 1 tin users 129609255 Jun 19 16:13 282_GISAID_GLM_base.trees
-rw-rw-r-- 1 tin users  93810349 Jun 19 16:13 282_GISAID_GLM_base.location.history.trees
-rw-rw-r-- 1 tin users 103340876 Jun 19 16:13 noanc_282_GISAID_GLM_base.trees

but no csv file for this R cmd needed in the very last step...
travelHistPaths <- loadPaths(fileName = "EPI_ISL_413597.travel_hist.csv")
