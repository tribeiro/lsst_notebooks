| Run name                        | HA bonus      | HA max| X bonus | Python | dome crawl | New OL correction  | Note                                                         |
| --------------------------------|:-------------:|:-----:|:------: |:------:|:----------:| :----------------: | :-----------:                                                |
| [baseline2018a](#baseline2018a) | 0.3           | 3.0   | 0.0     | 2      |     no     | no                 | Current opsimv4 baseline                                     |
| [mothra_2044](#mothra_2044)     | 0.3           | 3.0   | 0.0     | 3      |     no     | no                 | Python 3 baseline2018a replacement                           |
| [kraken_2026](#kraken_2026)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Python 3 baseline2018a replacement                           |
| [pontus_2002](#pontus_2002)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Simulation of a PanSTARRs like survey                        |
| [pontus_2003](#pontus_2003)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                |  baseline2018_dc (**Finished**)                       |
| [mothra_2045](#mothra_2045)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                |  whitepaper2018\_2rolling\_decbands (**Finished**)                       |
| [pontus_2487](#pontus_2487)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                |  whitepaper2018_manyvisits (**Running** - started @ 2018-05-17 08:36)                       |
| [kraken_2028](#kraken_2028)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                |  whitepaper2018\_2rolling\_decbands\_wfdbg (**Running** - started @ 2018-05-16 ??:??)                      |


# Simulations

### `baseline2018a`
- current opsimv4 baseline
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018a/config_run)

### `mothra_2044`
- recreation of baseline using Python3 code
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018_py3/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_mothra2044_comp/README.md)

### `kraken_2026`
- recreation of baseline using Python3 code, dome crawl, and new delay for OL correction
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018_dc_cl/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_kraken2026_comp/README.md)

### `pontus_2002`
- Simulation of a PanSTARRs like survey
- WFD + DD WFD having 274000 deg sq (X<1.5, DeMin = -78, DecMax = +18)
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_big_wfdonly/config_run)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_pontus2002_comp/README.md)
