# Basic run configuration for `mothra_2044`
- Identical config to `baseline2018a`
- HA bonus = 0.3, HA max = 3.0 for WFD
- Airmass bonus = 0.0
- Only difference is `mothra_2044` was run with `python3` vs `baselin2018a` which was run with `python2`

# Table of Contents
1. [fO](#fo)
2. [Total Effective Time](#total-effective-time)
3. [Normalized Effective Time](#normalized-effective-time)
4. [Open Shutter Fraction](#open-shutter-fraction)
5. [Parallax](#parallax)
6. [Proper Motion](#proper-motion)
7. [Rapid Revisit](#rapid-revisit)
8. [Fraction in Paris](#fraction-in-paris)
9. [Slews](#slews)
10. [Filter Changes](#filter-changes)
11. [Nvisits](#nvisits)
12. [Proposal Fractions](#proposal-fractions)
13. [Median Nvisits WFD](#median-nvisits-wfd)
14. [Median CoaddM5 WFD](#median-coaddm5-wfd)
15. [Median Airmass WFD](#median-airmass-wfd)
16. [Median Seeing WFD](#median-seeing-wfd)
17. [Skymap comparisons](#skymap-comparisons)
18. [Histrogram comparisons](#histrogram-comparisons)
# fO
|                                                       |   baseline2018a |   mothra_2044 |
|:------------------------------------------------------|----------------:|--------------:|
| fOArea: Nvisits (#) fO All visits HealpixSlicer       |         836     |       831     |
| fOArea: Nvisits/benchmark fO All visits HealpixSlicer |           1.013 |         1.007 |
| fONv: Area (sqdeg) fO All visits HealpixSlicer        |       18056.6   |     18056.6   |
| fONv: Area/benchmark fO All visits HealpixSlicer      |           1.003 |         1.003 |
| fOArea: Nvisits (#) fO WFD HealpixSlicer              |         835     |       830     |
| fOArea: Nvisits/benchmark fO WFD HealpixSlicer        |           1.012 |         1.006 |
| fONv: Area (sqdeg) fO WFD HealpixSlicer               |       18040.6   |     18040.6   |
| fONv: Area/benchmark fO WFD HealpixSlicer             |           1.002 |         1.002 |

# Total Effective Time
|                          |   baseline2018a |   mothra_2044 |
|:-------------------------|----------------:|--------------:|
| Total Teff all bands     |     3.9733e+07  |   3.96197e+07 |
| Total Teff WFD all bands |     3.59424e+07 |   3.57826e+07 |

# Normalized Effective Time
|                                                    |   baseline2018a |   mothra_2044 |
|:---------------------------------------------------|----------------:|--------------:|
| Normalized Teff WFD all bands                      |           0.585 |         0.583 |
| Median Normalized Teff WFD all bands HealpixSlicer |           0.584 |         0.585 |
| Normalized Teff WFD all bands HealpixSlicer        |       21495     |     21495     |

# Open Shutter Fraction
|                                                 |   baseline2018a |   mothra_2044 |
|:------------------------------------------------|----------------:|--------------:|
| OpenShutterFraction All visits                  |           0.716 |         0.715 |
| Median OpenShutterFraction Per night OneDSlicer |           0.718 |         0.718 |
| OpenShutterFraction Per night OneDSlicer        |        3025     |      3025     |

# Parallax
|                                                                |   baseline2018a |   mothra_2044 |
|:---------------------------------------------------------------|----------------:|--------------:|
| Median Parallax Error @ 22.4 All visits HealpixSlicer          |           1.849 |         1.832 |
| Median Parallax Error @ 24.0 All visits HealpixSlicer          |           7.212 |         7.187 |
| Median Parallax Coverage @ 22.4 All visits HealpixSlicer       |           0.548 |         0.56  |
| Median Parallax Coverage @ 24.0 All visits HealpixSlicer       |           0.541 |         0.557 |
| Median Parallax-DCR degeneracy @ 22.4 All visits HealpixSlicer |           0.219 |         0.226 |
| Median Parallax-DCR degeneracy @ 24.0 All visits HealpixSlicer |           0.214 |         0.224 |
| Median Parallax Error @ 22.4 WFD HealpixSlicer                 |           1.638 |         1.631 |
| Median Parallax Error @ 24.0 WFD HealpixSlicer                 |           6.32  |         6.329 |
| Median Parallax Coverage @ 22.4 WFD HealpixSlicer              |           0.549 |         0.561 |
| Median Parallax Coverage @ 24.0 WFD HealpixSlicer              |           0.544 |         0.557 |
| Median Parallax-DCR degeneracy @ 22.4 WFD HealpixSlicer        |           0.172 |         0.164 |
| Median Parallax-DCR degeneracy @ 24.0 WFD HealpixSlicer        |           0.165 |         0.161 |

# Proper Motion
|                                                            |   baseline2018a |   mothra_2044 |
|:-----------------------------------------------------------|----------------:|--------------:|
| Median Proper Motion Error @ 20.5 All visits HealpixSlicer |           0.173 |         0.173 |
| Median Proper Motion Error @ 24.0 All visits HealpixSlicer |           1.85  |         1.841 |
| Median Proper Motion Error @ 20.5 WFD HealpixSlicer        |           0.169 |         0.169 |
| Median Proper Motion Error @ 24.0 WFD HealpixSlicer        |           1.713 |         1.717 |

# Rapid Revisit
|                                                      |   baseline2018a |   mothra_2044 |
|:-----------------------------------------------------|----------------:|--------------:|
| Area (sq deg) RapidRevisits All visits HealpixSlicer |         9073.64 |       9033.86 |
| Median RapidRevisits All visits HealpixSlicer        |            0    |          0    |
| RapidRevisits All visits HealpixSlicer               |        31116    |      31116    |
| Area (sq deg) RapidRevisits WFD HealpixSlicer        |         9192.91 |       9177.56 |
| Median RapidRevisits WFD HealpixSlicer               |            0    |          0    |
| RapidRevisits WFD HealpixSlicer                      |        21495    |      21495    |

# Fraction in Paris
|                                                                          |   baseline2018a |   mothra_2044 |
|:-------------------------------------------------------------------------|----------------:|--------------:|
| Median Fraction of visits in pairs (15-60 min) gri HealpixSlicer         |           0.895 |         0.894 |
| Median Fraction of visits in pairs (15-60 min) gri WFD+NES HealpixSlicer |           0.901 |         0.901 |

# Slews
|                            |   baseline2018a |   mothra_2044 |
|:---------------------------|----------------:|--------------:|
| Mean slewTime All visits   |           7.92  |         7.966 |
| Median slewTime All visits |           5.175 |         5.198 |
| Min slewTime All visits    |           2     |         2     |
| Max slewTime All visits    |         143     |       142.998 |

# Filter Changes
|                                                |   baseline2018a |   mothra_2044 |
|:-----------------------------------------------|----------------:|--------------:|
| Filter Changes Whole Survey                    |       10644     |     10750     |
| Filter Changes Per Night OneDSlicer            |        3025     |      3025     |
| Max Filter Changes Per Night OneDSlicer        |          23     |        25     |
| Mean Filter Changes Per Night OneDSlicer       |           3.135 |         3.152 |
| Median Filter Changes Per Night OneDSlicer     |           2     |         2     |
| Min Filter Changes Per Night OneDSlicer        |           0     |         0     |
| N(+3Sigma) Filter Changes Per Night OneDSlicer |          59     |        61     |
| N(-3Sigma) Filter Changes Per Night OneDSlicer |           0     |         0     |
| Rms Filter Changes Per Night OneDSlicer        |           3.471 |         3.502 |

# Nvisits
|                                     |   baseline2018a |   mothra_2044 |
|:------------------------------------|----------------:|--------------:|
| Fraction of total Nvisits All props |      1          |    1          |
| Nvisits All props                   |      2.3727e+06 |    2.3701e+06 |
| Median Nvisits All props OneDSlicer |    785          |  783          |
| Nvisits All props OneDSlicer        |   3025          | 3025          |

# Proposal Fractions
|                                                  |   baseline2018a |   mothra_2044 |
|:-------------------------------------------------|----------------:|--------------:|
| Fraction of total Nvisits All props              |           1     |         1     |
| Fraction of total Nvisits WFD                    |           0.864 |         0.863 |
| Fraction of total Nvisits DeepDrillingCosmology1 |           0.046 |         0.046 |
| Fraction of total Nvisits NorthEclipticSpur      |           0.055 |         0.055 |
| Fraction of total Nvisits WideFastDeep           |           0.864 |         0.863 |
| Fraction of total Nvisits DD                     |           0.046 |         0.046 |
| Fraction of total Nvisits GalacticPlane          |           0.016 |         0.016 |
| Fraction of total Nvisits SouthCelestialPole     |           0.02  |         0.02  |

# Median Nvisits WFD
|                                            |   baseline2018a |   mothra_2044 |
|:-------------------------------------------|----------------:|--------------:|
| Median NVisits WFD y band HealpixSlicer    |             182 |           183 |
| Median NVisits WFD all bands HealpixSlicer |             912 |           912 |
| Median NVisits WFD z band HealpixSlicer    |             183 |           183 |
| Median NVisits WFD i band HealpixSlicer    |             199 |           197 |
| Median NVisits WFD u band HealpixSlicer    |              62 |            62 |
| Median NVisits WFD r band HealpixSlicer    |             200 |           200 |
| Median NVisits WFD g band HealpixSlicer    |              87 |            87 |

# Median CoaddM5 WFD
|                                         |   baseline2018a |   mothra_2044 |
|:----------------------------------------|----------------:|--------------:|
| Median CoaddM5 WFD y band HealpixSlicer |          24.892 |        24.887 |
| Median CoaddM5 WFD z band HealpixSlicer |          25.707 |        25.716 |
| Median CoaddM5 WFD i band HealpixSlicer |          26.613 |        26.606 |
| Median CoaddM5 WFD u band HealpixSlicer |          25.615 |        25.622 |
| Median CoaddM5 WFD r band HealpixSlicer |          27.188 |        27.187 |
| Median CoaddM5 WFD g band HealpixSlicer |          27.11  |        27.105 |

# Median Airmass WFD
|                                                   |   baseline2018a |   mothra_2044 |
|:--------------------------------------------------|----------------:|--------------:|
| Median Median airmass WFD y band HealpixSlicer    |           1.079 |         1.077 |
| Median Median airmass WFD all bands HealpixSlicer |           1.048 |         1.048 |
| Median Median airmass WFD z band HealpixSlicer    |           1.057 |         1.056 |
| Median Median airmass WFD i band HealpixSlicer    |           1.05  |         1.049 |
| Median Median airmass WFD u band HealpixSlicer    |           1.044 |         1.044 |
| Median Median airmass WFD r band HealpixSlicer    |           1.045 |         1.045 |
| Median Median airmass WFD g band HealpixSlicer    |           1.046 |         1.045 |

# Median Seeing WFD
|                                                     |   baseline2018a |   mothra_2044 |
|:----------------------------------------------------|----------------:|--------------:|
| Median Median seeingEff WFD y band HealpixSlicer    |           0.806 |         0.811 |
| Median Median seeingEff WFD all bands HealpixSlicer |           0.836 |         0.835 |
| Median Median seeingEff WFD z band HealpixSlicer    |           0.816 |         0.807 |
| Median Median seeingEff WFD i band HealpixSlicer    |           0.823 |         0.82  |
| Median Median seeingEff WFD u band HealpixSlicer    |           0.956 |         0.962 |
| Median Median seeingEff WFD r band HealpixSlicer    |           0.849 |         0.851 |
| Median Median seeingEff WFD g band HealpixSlicer    |           0.906 |         0.904 |

# Skymap comparisons
- [Nvisits all bands](figures/baseline2018a_mothra_2044_NVisits_all_bands_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.baseline2018a_mothra_2044_NVisits_all_bands_HEAL_ComboSkyMap.png)
- [Nvisits alt/az all bands](figures/baseline2018a_mothra_2044_Nvisits_as_function_of_Alt_Az_all_bands_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.baseline2018a_mothra_2044_Nvisits_as_function_of_Alt_Az_all_bands_HEAL_ComboSkyMap.png)
- [Median airmass all bands](figures/baseline2018a_mothra_2044_Median_airmass_all_bands_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.baseline2018a_mothra_2044_Median_airmass_all_bands_HEAL_ComboSkyMap.png)
- [Max airmass all bands](figures/baseline2018a_mothra_2044_Max_airmass_all_bands_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.baseline2018a_mothra_2044_Max_airmass_all_bands_HEAL_ComboSkyMap.png)
- [CoaddM5 r band](figures/baseline2018a_mothra_2044_CoaddM5_r_band_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.baseline2018a_mothra_2044_CoaddM5_r_band_HEAL_ComboSkyMap.png)
- [Normalized Proper Motion at 20.5](figures/baseline2018a_mothra_2044_Normalized_Proper_Motion_@_20_5_All_visits_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.baseline2018a_mothra_2044_Normalized_Proper_Motion_@_20_5_All_visits_HEAL_ComboSkyMap.png)
- [Normalized Parallax at 22.4](figures/baseline2018a_mothra_2044_Normalized_Parallax_@_22_4_All_visits_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.baseline2018a_mothra_2044_Normalized_Parallax_@_22_4_All_visits_HEAL_ComboSkyMap.png)
# Histrogram comparisons
### CoaddM5 r band HealPix Histrogram
![png](figures/thumb.baseline2018a_mothra_2044_CoaddM5_r_band_HEAL_ComboHistogram.png)
### Slew Distance Histogram
![png](figures/thumb.baseline2018a_mothra_2044_Slew_Distance_Histogram_All_visits_ONED_ComboBinnedData.png)
### Slew Time Histogram 
![png](figures/thumb.baseline2018a_mothra_2044_Slew_Time_Histogram_All_visits_ONED_ComboBinnedData.png)