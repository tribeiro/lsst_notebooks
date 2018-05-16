| Run name      | HA bonus      | HA max| X bonus | Python | dome crawl | New OL correction  | OpsimV3 run   |
| ------------- |:-------------:|:-----:|:------: |:------:|:----------:| :----------------: | :-----------: |
| [baseline2018a](#baseline2018a) | 0.3           | 3.0   | 0.0     | 2      |     no     | no                 | minion_1016   |
| mothra_2044   | 0.3           | 3.0   | 0.0     | 3      |     no     | no                 | N/A           |
| kraken_2026   | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | N/A           |
| pontus_2002   | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | minion_1020   |

# Simulations

### `baseline2018a`
- current opsimv4 baseline

### `mothra_2044`
- recreation of baseline using Python3 code
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_mothra2044_comp/README.md)

### `kraken_2026`
- recreation of baseline using Python3 code, dome crawl, and new delay for OL correction
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_kraken2026_comp/README.md)

### `pontus_2002`
- Simulation of a PanSTARRs like survey
- WFD + DD WFD having 274000 deg sq (X<1.5, DeMin = -78, DecMax = +18)
- [comparison with baseline2018a](https://github.com/oboberg/lsst_notebooks/blob/master/whitepaper_runs/baseline2018a_pontus2002_comp/README.md)
