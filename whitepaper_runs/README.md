| Run name                        | HA bonus      | HA max| X bonus | Python | dome crawl | New OL correction  | Note                                                         |
| --------------------------------|:-------------:|:-----:|:------: |:------:|:----------:| :----------------: | :-----------:                                                |
| [baseline2018a](#baseline2018a) | 0.3           | 3.0   | 0.0     | 2      |     no     | no                 | Current opsimv4 baseline                                     |
| [mothra_2044](#mothra_2044)     | 0.3           | 3.0   | 0.0     | 3      |     no     | no                 | Python 3 baseline2018a replacement                           |
| [pontus_2003](#pontus_2003)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | no                 | Python 3 baseline2018a replacement (with dome crawl)         |
| [kraken_2026](#kraken_2026)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Python 3 baseline2018a replacement (with dome crawl and OL)  |
| [pontus_2002](#pontus_2002)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Simulation of a PanSTARRs like survey                        |
| [mothra_2045](#mothra_2045)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | 2 alternating Dec bands switched every other year, WFD off                                  |
| [mothra_2046](#mothra_2046)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | No pairs survey                                                                             |
| [pontus_2487](#pontus_2487)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | "Many visits" 20s visits with single snap, 40s visits in u band                             |
| [kraken_2028](#kraken_2028)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                |  whitepaper2018\_2rolling\_decbands\_wfdbg (**Finished - Copied to opsim2**)                |
| [pontus_2488](#pontus_2488)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                |  whitepaper2018_nogp (**Finished - Copied to opsim2**)                                     |
| [kraken_2033](#kraken_2033)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                |  whitepaper2018\_2rolling\_decbands\_yr2\_9\_wfdoff (**Started** @ 2018/05/22 - 09:30)      |
| [pontus_2489](#pontus_2489)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                |  whitepaper2018\_manyvisits (**Started** @ 2018/05/)                                     |

# Simulations

## Creating a new baseline with latest code, dome crawl, and OL correction delay

### `baseline2018a`
- current opsimv4 baseline
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018a/config_run)

### `mothra_2044`
- recreation of baseline using Python3 code
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018_py3/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_mothra2044_comp/README.md)

### `pontus_2003`
- recreation of baseline using Python3 code and dome crawl
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018_dc/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_pontus2003_comp/README.md)

### `kraken_2026`
- recreation of baseline using Python3 code, dome crawl, and new delay for OL correction
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018_dc_cl/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_kraken2026_comp/README.md)
- [comparison with pontus_2003](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/pontus_2003_kraken2026_comp/README.md)

## Alternate survey strategies

### `pontus_2002`
- Simulation of a PanSTARRs like survey
- WFD + DD WFD having 274000 deg sq (X<1.5, DeMin = -78, DecMax = +18)
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_big_wfdonly/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_pontus2002_comp/README.md)

### `mothra_2045`
- Rolling cadence
- 2 alternating Dec bands switched every other year
- No WFD proposal in the background.
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_2rolling_decbands/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_mothra2045_comp/README.md)

### `pontus_2487`
- "Many visits" survey
-  20s visits with single snap in `g,r,i,z,y`
-  40s visits with single snap  un `u` band
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_manyvisits/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_pontus2487_comp/README.md)

### `mothra_2046`
- no pairs survey
- same footprint and bonus values used in `baseline2018a`
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_nopairs/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_mothra2046_comp/README.md)
