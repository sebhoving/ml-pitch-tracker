## Prediction: YIN on 36 trombone takes (16 Oct)
- octave_error_rate: 0.05   because occasional notes have slightly rough tone which I think means that there is more of the higher harmonics within the note
- typical error on correct frames: 10 cents   because the median of uncertainty of my notes is around 5 cents and then and extra 5 cents is pretty standard for a tuner
MAE = (1-p)* e + p*1200
- mae_cents: 69.5   (from the formula above)
- median_cents: 10   because it shouldn't be affected much by the octave errors
- within_50c / 20c / 10c: 0.95 / 0.8 / 0.3   because just a guess based on above numbers
- worst 3 files I expect: the 3 lowest or highest notes  because they're all played with low quality, high uncertainty and rough tone.

## Actual (filled in after running)
Evaluation Results: {'instrument': 'trombone', 'n_frames': 10997, 'within_50c': np.float64(0.5215058652359734), 'within_20c': np.float64(0.503864690370101), 'within_10c': np.float64(0.4694007456579067), 'mae_cents': 669.8868682284572, 'median_cents': 0.1937371131361902, 'octave_error_rate': np.float64(0.02573429117031918)}

By file:

Evaluation Results: 
    instrument  n_frames  within_50c  within_20c  within_10c    mae_cents  median_cents  octave_error_rate
3    trombone       294    0.537415    0.527211    0.500000   267.194702     -3.182159           0.000000
4    trombone       333    0.492492    0.480480    0.450450   340.549772     -0.143638           0.003003
2    trombone       310    0.538710    0.503226    0.422581   378.883465      3.418057           0.003226
12   trombone       323    0.566563    0.544892    0.532508   425.395645      0.722292           0.000000
17   trombone       294    0.598639    0.574830    0.568027   486.079651     -0.609625           0.017007
5    trombone       287    0.560976    0.519164    0.452962   492.519030      6.990861           0.006969
1    trombone       306    0.519608    0.509804    0.454248   505.155794     -0.245503           0.013072
14   trombone       291    0.570447    0.560137    0.505155   523.663109     -1.539133           0.017182
11   trombone       320    0.537500    0.531250    0.471875   571.067781      0.219188           0.040625
6    trombone       292    0.544521    0.506849    0.441781   571.316555      2.271922           0.020548
22   trombone       256    0.566406    0.531250    0.515625   594.784798     -2.475029           0.015625
18   trombone       294    0.520408    0.503401    0.493197   600.403204     -1.375132           0.020408
15   trombone       262    0.480916    0.469466    0.446565   611.389129      0.039566           0.022901
20   trombone       262    0.549618    0.530534    0.500000   613.541136     -0.872893           0.022901
24   trombone       299    0.591973    0.571906    0.555184   617.787061     -1.588854           0.033445
13   trombone       294    0.527211    0.520408    0.486395   623.970103      2.405004           0.163265
8    trombone       305    0.481967    0.452459    0.400000   637.108257      2.106201           0.003279
0    trombone       323    0.473684    0.461300    0.417957   639.182384     -0.508320           0.021672
10   trombone       364    0.461538    0.439560    0.420330   645.930736     -2.988499           0.010989
29   trombone       323    0.585139    0.578947    0.551084   650.878087     -1.126062           0.003096
16   trombone       395    0.493671    0.478481    0.417722   651.899360      3.206793           0.002532
25   trombone       248    0.528226    0.500000    0.475806   690.558298      2.705097           0.024194
19   trombone       256    0.425781    0.410156    0.347656   699.030630     -0.478171           0.023438
26   trombone       294    0.506803    0.489796    0.479592   725.023869     -1.996585           0.163265
27   trombone       290    0.534483    0.531034    0.500000   734.173595      0.248897           0.037931
7    trombone       300    0.660000    0.650000    0.630000   751.009795      6.642648           0.043333
35   trombone       360    0.502778    0.488889    0.441667   770.348687      3.601471           0.022222
28   trombone       277    0.566787    0.555957    0.530686   787.610251      1.420967           0.046931
21   trombone       301    0.465116    0.448505    0.425249   809.532899     -1.700726           0.003322
9    trombone       339    0.442478    0.427729    0.412979   832.079461      1.753405           0.064897
30   trombone       322    0.496894    0.487578    0.481366   854.194571     -3.557542           0.009317
32   trombone       310    0.474194    0.474194    0.445161   873.780724      0.822611           0.038710
31   trombone       335    0.510448    0.486567    0.453731   946.091720      0.097364           0.011940
23   trombone       293    0.532423    0.529010    0.529010   974.829446     -1.273700           0.000000
34   trombone       342    0.464912    0.409357    0.333333  1026.166765     -1.101900           0.011696
33   trombone       303    0.511551    0.501650    0.468647  1106.856403      1.227559           0.003300
## What surprised me
I think the data is far more accurate than I thought, the reason all the metrics are close to 0.5, I believe is because most of the files are half silent so those silent frames can never be within the metrics, hence the mean average error(mae) is very high but the median is very low.
