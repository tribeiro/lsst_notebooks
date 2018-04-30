# Table of Contents
1. [Sky map comparisons](#sky-map-comparisons)
2. [CoaddM5 r band](#coaddm5-r-band-healpixhistrogram)
3. [HA distributions](#ha-distribution-all-bands--y-band)
4. [Slew time and distance distributions](#slew-time-and-distance-distributions)
5. [SRD metrics overview](#srd-metrics)
6. [Select metrics overiew](#select-metrics)

# Sky map comparisons

 - [Nvisits all bands](figures/colossus_2646_astro-lsst-01_2022_NVisits_all_bands_HEAL_ComboSkyMap.pdf)
![Nvisits](output_38_2.png)


 - [Nvisits alt/az all bands](figures/colossus_2646_astro-lsst-01_2022_Nvisits_as_function_of_Alt_Az_all_bands_HEAL_ComboSkyMap.pdf)
![png](output_38_3.png)


 - [Median airmass all bands](figures/colossus_2646_astro-lsst-01_2022_Median_airmass_all_bands_HEAL_ComboSkyMap.pdf)
![png](output_38_4.png)


 - [Max airmass all bands](figures/colossus_2646_astro-lsst-01_2022_Max_airmass_all_bands_HEAL_ComboSkyMap.pdf)
![png](output_38_5.png)


 - [CoaddM5 r band](figures/colossus_2646_astro-lsst-01_2022_CoaddM5_r_band_HEAL_ComboSkyMap.pdf)
![png](output_38_6.png)


# CoaddM5 r band HealpixHistrogram


![png](output_40_0.png)

# HA distribution all bands / y band

![png](output_48_1.png) ![png](output_50_1.png)

# Slew time and distance distributions

![png](output_58_0.png) ![png](output_59_0.png)



# SRD metrics

|                                                                                    |   baseline2018a |   colossus_2646 |
|:-----------------------------------------------------------------------------------|----------------:|----------------:|
| fOArea: Nvisits (#) fO All visits HealpixSlicer                                    |         836     |         709     |
| fOArea: Nvisits/benchmark fO All visits HealpixSlicer                              |           1.013 |           0.859 |
| fONv: Area (sqdeg) fO All visits HealpixSlicer                                     |       18056.6   |       17738.5   |
| fONv: Area/benchmark fO All visits HealpixSlicer                                   |           1.003 |           0.985 |
| fOArea: Nvisits (#) fO WFD HealpixSlicer                                           |         835     |         432     |
| fOArea: Nvisits/benchmark fO WFD HealpixSlicer                                     |           1.012 |           0.524 |
| fONv: Area (sqdeg) fO WFD HealpixSlicer                                            |       18040.6   |       17260.9   |
| fONv: Area/benchmark fO WFD HealpixSlicer                                          |           1.002 |           0.959 |
| Median Parallax Error @ 24.0 All visits HealpixSlicer                              |           7.212 |           7.41  |
| Median Parallax Error @ 24.0 WFD HealpixSlicer                                     |           6.32  |           6.681 |
| Median Parallax Error @ 22.4 All visits HealpixSlicer                              |           1.849 |           1.879 |
| Median Parallax Error @ 22.4 WFD HealpixSlicer                                     |           1.638 |           1.712 |
| Area (sq deg) Number of revisits faster than 30.0 minutes All visits HealpixSlicer |        5834.76  |          69.747 |
| Area (sq deg) Number of revisits faster than 30.0 minutes WFD HealpixSlicer        |        8340.79  |           0     |

# Select metrics

|                                                                          |   baseline2018a |   colossus_2646 |
|:-------------------------------------------------------------------------|----------------:|----------------:|
| Fraction of total Nvisits All props                                      |           1     |           1     |
| Fraction of total Nvisits SouthCelestialPole                             |           0.02  |           0.029 |
| Fraction of total Nvisits WideFastDeep                                   |           0.864 |           0.815 |
| Fraction of total Nvisits DeepDrillingCosmology1                         |           0.046 |           0.068 |
| Fraction of total Nvisits GalacticPlane                                  |           0.016 |           0.019 |
| Fraction of total Nvisits NorthEclipticSpur                              |           0.055 |           0.068 |
| Median Fraction of visits in pairs (15-60 min) gri HealpixSlicer         |           0.895 |           0.717 |
| Median Fraction of visits in pairs (15-60 min) gri WFD+NES HealpixSlicer |           0.901 |           0.76  |
| Median NVisits WFD u band HealpixSlicer                                  |          62     |          67     |
| Median NVisits WFD i band HealpixSlicer                                  |         199     |         204     |
| Median NVisits WFD r band HealpixSlicer                                  |         200     |         204     |
| Median NVisits WFD g band HealpixSlicer                                  |          87     |          92     |
| Median NVisits WFD all bands HealpixSlicer                               |         912     |         946     |
| Median NVisits WFD z band HealpixSlicer                                  |         183     |         186     |
| Median NVisits WFD y band HealpixSlicer                                  |         182     |         192     |
| Median CoaddM5 WFD u band HealpixSlicer                                  |          25.615 |          25.644 |
| Median CoaddM5 WFD i band HealpixSlicer                                  |          26.613 |          26.526 |
| Median CoaddM5 WFD r band HealpixSlicer                                  |          27.188 |          27.13  |
| Median CoaddM5 WFD g band HealpixSlicer                                  |          27.11  |          27.149 |
| Median CoaddM5 WFD z band HealpixSlicer                                  |          25.707 |          25.808 |
| Median CoaddM5 WFD y band HealpixSlicer                                  |          24.892 |          24.816 |
| Median Median seeingEff WFD u band HealpixSlicer                         |           0.956 |           0.949 |
| Median Median seeingEff WFD i band HealpixSlicer                         |           0.823 |           0.844 |
| Median Median seeingEff WFD r band HealpixSlicer                         |           0.849 |           0.863 |
| Median Median seeingEff WFD g band HealpixSlicer                         |           0.906 |           0.895 |
| Median Median seeingEff WFD all bands HealpixSlicer                      |           0.836 |           0.856 |
| Median Median seeingEff WFD z band HealpixSlicer                         |           0.816 |           0.829 |
| Median Median seeingEff WFD y band HealpixSlicer                         |           0.806 |           0.837 |
| Median Median airmass WFD u band HealpixSlicer                           |           1.044 |           1.05  |
| Median Median airmass WFD i band HealpixSlicer                           |           1.05  |           1.051 |
| Median Median airmass WFD r band HealpixSlicer                           |           1.045 |           1.052 |
| Median Median airmass WFD g band HealpixSlicer                           |           1.046 |           1.048 |
| Median Median airmass WFD all bands HealpixSlicer                        |           1.048 |           1.054 |
| Median Median airmass WFD z band HealpixSlicer                           |           1.057 |           1.062 |
| Median Median airmass WFD y band HealpixSlicer                           |           1.079 |           1.138 |
| Median slewTime All visits                                               |           5.175 |           5.412 |
| Filter Changes Whole Survey                                              |       10644     |       21508     |
| Filter Changes Per Night OneDSlicer                                      |        3025     |        3025     |
| Median Filter Changes Per Night OneDSlicer                               |           2     |           5     |
| Normalized Teff all bands                                                |           0.558 |           0.531 |
| Median Normalized Teff all bands HealpixSlicer                           |           0.546 |           0.516 |
| Normalized Teff all bands HealpixSlicer                                  |       31116     |       31939     |
| OpenShutterFraction All visits                                           |           0.716 |           0.657 |
| Median OpenShutterFraction Per night OneDSlicer                          |           0.718 |           0.658 |
| OpenShutterFraction Per night OneDSlicer                                 |        3025     |        3025     |

# Table of Contents
1. [fO Metrics](#fo-metrics)
2. [Parallax](#parallax)
3. [Proper motion](#proper-motion)
4. [Rapid revisit](#rapid-revisit)
5. [Fraction in pairs](#fraction-in-paris)
6. [Fraction of total visits per proposal](#fraction-of-total-visits-per-proposal)
7. [Median Nvisits per filter WFD](#median-nvsits-per-filter-wfd)
8. [Median CoaddedM5 per filter WFD](#median-coaddedm5-per-filter-wfd)
9. [Median seeingEff per filter WFD](#median-seeingeff-per-filter-wfd)
10. [Slew statistics](#slew-statistics)
11. [Filter change statistics](#filter-change-statistics)
12. [Normalized effective time](#normalized-effective-time)
13. [Open shutter fraction](#open-shutter-fraction)

# fO Metrics

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>fOArea: Nvisits (#) fO All visits HealpixSlicer</th>
      <td>836.000000</td>
      <td>709.000000</td>
    </tr>
    <tr>
      <th>fOArea: Nvisits/benchmark fO All visits HealpixSlicer</th>
      <td>1.013333</td>
      <td>0.859394</td>
    </tr>
    <tr>
      <th>fONv: Area (sqdeg) fO All visits HealpixSlicer</th>
      <td>18056.563483</td>
      <td>17738.471192</td>
    </tr>
    <tr>
      <th>fONv: Area/benchmark fO All visits HealpixSlicer</th>
      <td>1.003142</td>
      <td>0.985471</td>
    </tr>
    <tr>
      <th>fOArea: Nvisits (#) fO WFD HealpixSlicer</th>
      <td>835.000000</td>
      <td>432.000000</td>
    </tr>
    <tr>
      <th>fOArea: Nvisits/benchmark fO WFD HealpixSlicer</th>
      <td>1.012121</td>
      <td>0.523636</td>
    </tr>
    <tr>
      <th>fONv: Area (sqdeg) fO WFD HealpixSlicer</th>
      <td>18040.616904</td>
      <td>17260.913107</td>
    </tr>
    <tr>
      <th>fONv: Area/benchmark fO WFD HealpixSlicer</th>
      <td>1.002256</td>
      <td>0.958940</td>
    </tr>
  </tbody>
</table>
</div>



# Parallax

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Median Parallax Error @ 24.0 All visits HealpixSlicer</th>
      <td>7.211897</td>
      <td>7.410334</td>
    </tr>
    <tr>
      <th>Median Parallax Coverage @ 24.0 All visits HealpixSlicer</th>
      <td>0.540989</td>
      <td>0.575772</td>
    </tr>
    <tr>
      <th>Median Parallax-DCR degeneracy @ 24.0 All visits HealpixSlicer</th>
      <td>0.213722</td>
      <td>0.277398</td>
    </tr>
    <tr>
      <th>Median Parallax Error @ 24.0 WFD HealpixSlicer</th>
      <td>6.320265</td>
      <td>6.680559</td>
    </tr>
    <tr>
      <th>Median Parallax Coverage @ 24.0 WFD HealpixSlicer</th>
      <td>0.543600</td>
      <td>0.598591</td>
    </tr>
    <tr>
      <th>Median Parallax-DCR degeneracy @ 24.0 WFD HealpixSlicer</th>
      <td>0.165450</td>
      <td>0.298203</td>
    </tr>
    <tr>
      <th>Median Parallax Error @ 22.4 All visits HealpixSlicer</th>
      <td>1.848632</td>
      <td>1.879195</td>
    </tr>
    <tr>
      <th>Median Parallax Coverage @ 22.4 All visits HealpixSlicer</th>
      <td>0.547516</td>
      <td>0.584661</td>
    </tr>
    <tr>
      <th>Median Parallax-DCR degeneracy @ 22.4 All visits HealpixSlicer</th>
      <td>0.219225</td>
      <td>0.285838</td>
    </tr>
    <tr>
      <th>Median Parallax Error @ 22.4 WFD HealpixSlicer</th>
      <td>1.637874</td>
      <td>1.711611</td>
    </tr>
    <tr>
      <th>Median Parallax Coverage @ 22.4 WFD HealpixSlicer</th>
      <td>0.549357</td>
      <td>0.606619</td>
    </tr>
    <tr>
      <th>Median Parallax-DCR degeneracy @ 22.4 WFD HealpixSlicer</th>
      <td>0.172049</td>
      <td>0.309513</td>
    </tr>
  </tbody>
</table>
</div>



# Proper motion

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Median Proper Motion Error @ 24.0 All visits HealpixSlicer</th>
      <td>1.850232</td>
      <td>1.840257</td>
    </tr>
    <tr>
      <th>Median Proper Motion Error @ 24.0 WFD HealpixSlicer</th>
      <td>1.712652</td>
      <td>1.730705</td>
    </tr>
    <tr>
      <th>Median Proper Motion Error @ 20.5 All visits HealpixSlicer</th>
      <td>0.173208</td>
      <td>0.169556</td>
    </tr>
    <tr>
      <th>Median Proper Motion Error @ 20.5 WFD HealpixSlicer</th>
      <td>0.169005</td>
      <td>0.166064</td>
    </tr>
  </tbody>
</table>
</div>



# Rapid revisit

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Area (sq deg) Number of revisits faster than 30.0 minutes All visits HealpixSlicer</th>
      <td>5834.756474</td>
      <td>69.747328</td>
    </tr>
    <tr>
      <th>Area (sq deg) Number of revisits faster than 30.0 minutes WFD HealpixSlicer</th>
      <td>8340.794119</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>



# Fraction in pairs

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Median Fraction of visits in pairs (15-60 min) gri HealpixSlicer</th>
      <td>0.894621</td>
      <td>0.716654</td>
    </tr>
    <tr>
      <th>Median Fraction of visits in pairs (15-60 min) gri WFD+NES HealpixSlicer</th>
      <td>0.901468</td>
      <td>0.760396</td>
    </tr>
  </tbody>
</table>
</div>



# Fraction of Total visits per proposal

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Fraction of total Nvisits All props</th>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>Fraction of total Nvisits SouthCelestialPole</th>
      <td>0.019821</td>
      <td>0.029253</td>
    </tr>
    <tr>
      <th>Fraction of total Nvisits WideFastDeep</th>
      <td>0.863711</td>
      <td>0.815402</td>
    </tr>
    <tr>
      <th>Fraction of total Nvisits DeepDrillingCosmology1</th>
      <td>0.045935</td>
      <td>0.068046</td>
    </tr>
    <tr>
      <th>Fraction of total Nvisits GalacticPlane</th>
      <td>0.016270</td>
      <td>0.019115</td>
    </tr>
    <tr>
      <th>Fraction of total Nvisits NorthEclipticSpur</th>
      <td>0.054521</td>
      <td>0.068185</td>
    </tr>
  </tbody>
</table>
</div>



# Median Nvsits per filter WFD

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Median NVisits WFD u band HealpixSlicer</th>
      <td>62.0</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>Median NVisits WFD i band HealpixSlicer</th>
      <td>199.0</td>
      <td>204.0</td>
    </tr>
    <tr>
      <th>Median NVisits WFD r band HealpixSlicer</th>
      <td>200.0</td>
      <td>204.0</td>
    </tr>
    <tr>
      <th>Median NVisits WFD g band HealpixSlicer</th>
      <td>87.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>Median NVisits WFD all bands HealpixSlicer</th>
      <td>912.0</td>
      <td>946.0</td>
    </tr>
    <tr>
      <th>Median NVisits WFD z band HealpixSlicer</th>
      <td>183.0</td>
      <td>186.0</td>
    </tr>
    <tr>
      <th>Median NVisits WFD y band HealpixSlicer</th>
      <td>182.0</td>
      <td>192.0</td>
    </tr>
  </tbody>
</table>
</div>



# Median CoaddedM5 per filter WFD

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Median CoaddM5 WFD u band HealpixSlicer</th>
      <td>25.615042</td>
      <td>25.644178</td>
    </tr>
    <tr>
      <th>Median CoaddM5 WFD i band HealpixSlicer</th>
      <td>26.613175</td>
      <td>26.526201</td>
    </tr>
    <tr>
      <th>Median CoaddM5 WFD r band HealpixSlicer</th>
      <td>27.187683</td>
      <td>27.129955</td>
    </tr>
    <tr>
      <th>Median CoaddM5 WFD g band HealpixSlicer</th>
      <td>27.110218</td>
      <td>27.149279</td>
    </tr>
    <tr>
      <th>Median CoaddM5 WFD z band HealpixSlicer</th>
      <td>25.706837</td>
      <td>25.808272</td>
    </tr>
    <tr>
      <th>Median CoaddM5 WFD y band HealpixSlicer</th>
      <td>24.892254</td>
      <td>24.815838</td>
    </tr>
  </tbody>
</table>
</div>



# Median seeingEff per filter WFD

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Median Median seeingEff WFD u band HealpixSlicer</th>
      <td>0.955978</td>
      <td>0.948973</td>
    </tr>
    <tr>
      <th>Median Median seeingEff WFD i band HealpixSlicer</th>
      <td>0.823022</td>
      <td>0.844026</td>
    </tr>
    <tr>
      <th>Median Median seeingEff WFD r band HealpixSlicer</th>
      <td>0.849100</td>
      <td>0.863123</td>
    </tr>
    <tr>
      <th>Median Median seeingEff WFD g band HealpixSlicer</th>
      <td>0.905754</td>
      <td>0.895287</td>
    </tr>
    <tr>
      <th>Median Median seeingEff WFD all bands HealpixSlicer</th>
      <td>0.836284</td>
      <td>0.855962</td>
    </tr>
    <tr>
      <th>Median Median seeingEff WFD z band HealpixSlicer</th>
      <td>0.815861</td>
      <td>0.829391</td>
    </tr>
    <tr>
      <th>Median Median seeingEff WFD y band HealpixSlicer</th>
      <td>0.805565</td>
      <td>0.837281</td>
    </tr>
  </tbody>
</table>
</div>



# Slew statistics

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mean slewTime All visits</th>
      <td>7.919872</td>
      <td>11.638055</td>
    </tr>
    <tr>
      <th>Median slewTime All visits</th>
      <td>5.174937</td>
      <td>5.412055</td>
    </tr>
    <tr>
      <th>Min slewTime All visits</th>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>Max slewTime All visits</th>
      <td>142.999591</td>
      <td>140.000000</td>
    </tr>
  </tbody>
</table>
</div>



# Filter change statistics

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Filter Changes Whole Survey</th>
      <td>10644.000000</td>
      <td>21508.000000</td>
    </tr>
    <tr>
      <th>Filter Changes Per Night OneDSlicer</th>
      <td>3025.000000</td>
      <td>3025.000000</td>
    </tr>
    <tr>
      <th>Max Filter Changes Per Night OneDSlicer</th>
      <td>23.000000</td>
      <td>26.000000</td>
    </tr>
    <tr>
      <th>Mean Filter Changes Per Night OneDSlicer</th>
      <td>3.134876</td>
      <td>6.128264</td>
    </tr>
    <tr>
      <th>Median Filter Changes Per Night OneDSlicer</th>
      <td>2.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>Min Filter Changes Per Night OneDSlicer</th>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>N(+3Sigma) Filter Changes Per Night OneDSlicer</th>
      <td>59.000000</td>
      <td>80.000000</td>
    </tr>
    <tr>
      <th>N(-3Sigma) Filter Changes Per Night OneDSlicer</th>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Rms Filter Changes Per Night OneDSlicer</th>
      <td>3.471012</td>
      <td>4.873074</td>
    </tr>
  </tbody>
</table>
</div>



# Normalized effective time

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Normalized Teff all bands</th>
      <td>0.558197</td>
      <td>0.531212</td>
    </tr>
    <tr>
      <th>Max Normalized Teff all bands HealpixSlicer</th>
      <td>0.735635</td>
      <td>0.959036</td>
    </tr>
    <tr>
      <th>Mean Normalized Teff all bands HealpixSlicer</th>
      <td>0.502386</td>
      <td>0.487929</td>
    </tr>
    <tr>
      <th>Median Normalized Teff all bands HealpixSlicer</th>
      <td>0.545690</td>
      <td>0.516255</td>
    </tr>
    <tr>
      <th>Min Normalized Teff all bands HealpixSlicer</th>
      <td>0.073872</td>
      <td>0.058435</td>
    </tr>
    <tr>
      <th>N(+3Sigma) Normalized Teff all bands HealpixSlicer</th>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>N(-3Sigma) Normalized Teff all bands HealpixSlicer</th>
      <td>0.000000</td>
      <td>15.000000</td>
    </tr>
    <tr>
      <th>Normalized Teff all bands HealpixSlicer</th>
      <td>31116.000000</td>
      <td>31939.000000</td>
    </tr>
    <tr>
      <th>Rms Normalized Teff all bands HealpixSlicer</th>
      <td>0.146207</td>
      <td>0.133986</td>
    </tr>
  </tbody>
</table>
</div>



# Open shutter fraction


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baseline2018a</th>
      <th>colossus_2646</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>OpenShutterFraction All visits</th>
      <td>0.715651</td>
      <td>0.657346</td>
    </tr>
    <tr>
      <th>Max OpenShutterFraction Per night OneDSlicer</th>
      <td>0.765440</td>
      <td>0.734834</td>
    </tr>
    <tr>
      <th>Mean OpenShutterFraction Per night OneDSlicer</th>
      <td>0.715703</td>
      <td>0.657944</td>
    </tr>
    <tr>
      <th>Median OpenShutterFraction Per night OneDSlicer</th>
      <td>0.718118</td>
      <td>0.658031</td>
    </tr>
    <tr>
      <th>Min OpenShutterFraction Per night OneDSlicer</th>
      <td>0.601392</td>
      <td>0.583334</td>
    </tr>
    <tr>
      <th>N(+3Sigma) OpenShutterFraction Per night OneDSlicer</th>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>N(-3Sigma) OpenShutterFraction Per night OneDSlicer</th>
      <td>22.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>OpenShutterFraction Per night OneDSlicer</th>
      <td>3025.000000</td>
      <td>3025.000000</td>
    </tr>
    <tr>
      <th>Rms OpenShutterFraction Per night OneDSlicer</th>
      <td>0.021834</td>
      <td>0.025913</td>
    </tr>
  </tbody>
</table>
</div>
