import sys, os
import numpy as np
import numpy.ma as ma
import healpy as hp
import matplotlib.pyplot as plt
from astropy.io import ascii
import pandas as pd
import sqlite3
from lsst.sims.utils import _angularSeparation
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

log = logging.getLogger(__name__)

if __name__ == '__main__':
    _path = os.path.expanduser('~/maf_local/Documents/opsimv4_data/run_dir/bfs/')
    data_str = 'opsimv4_data/run_dir/bf_{}_{}_{}.npy'

    con = sqlite3.connect(os.path.join(_path, "pontus_2491.db"))

    df = pd.read_sql_query("select filter,observationId,night from SummaryAllProps", con)

    con.close()

    if not os.path.exists('movie/snaps/'):
        os.makedirs('movie/snaps/')

    for i in range(100):

        obs_filter = df['filter'][i]
        obs_id = df['observationId'][i]
        obs_night = df['night'][i]
        log.info('{} {} {}'.format(obs_filter, obs_id, obs_night))

        data_path = os.path.join(_path, data_str.format(obs_night, obs_filter, obs_id - 1))
        os.path.exists(data_path)
        log.info('{} Exists[{}]'.format(data_path, os.path.exists(data_path)))

        bfs = np.load(data_path)

        fig = plt.figure(figsize=(18, 6))

        hp.mollview(bfs[()]['reward'], title='Reward Map', sub=(1, 2, 2), min=cmin, max=cmax)
        hp.graticule()

        hp.mollview(bfs[()]['M5']['condition_features']['M5Depth'],
                    title='Feature: M5Depth', sub=(4, 4, 1), cbar=False)
        # hp.graticule()

        hp.mollview(bfs[()]['Target']['survey_features']['N_obs'],
                    title='Feature: N_obs', sub=(4, 4, 5), cbar=False)
        # hp.graticule()

        hp.mollview(bfs[()]['Slewtime']['condition_features']['slewtime'],
                    title='Feature: Slewtime', sub=(4, 4, 9), cbar=False)
        # hp.graticule()

        angular_distance = _angularSeparation(bfs[()]['Moon']['condition_features']['altaz']['az'],
                                              bfs[()]['Moon']['condition_features']['altaz']['alt'],
                                              bfs[()]['Moon']['condition_features']['moon']['moonAz'],
                                              bfs[()]['Moon']['condition_features']['moon']['moonAlt'])

        hp.mollview(angular_distance,
                    title='Feature: Moon distance', sub=(4, 4, 13), cbar=False)

        hp.mollview(bfs[()]['M5']['basis_function'],
                    title='M5 reward map', sub=(4, 4, 2), cbar=False)
        # hp.graticule()

        hp.mollview(bfs[()]['Target']['basis_function'],
                    title='Target reward map', sub=(4, 4, 6), cbar=False)
        # hp.graticule()

        hp.mollview(bfs[()]['Moon']['basis_function'],
                    title='Moon avoidance map', sub=(4, 4, 14), cbar=False)

        bfs_map = bfs[()]['Slewtime']['basis_function']
        if type(bfs_map) == float:
            bfs_map = np.zeros(hp.nside2npix(32)) + bfs_map
        hp.mollview(bfs_map,
                    title='Slewtime reward map', sub=(4, 4, 10), cbar=False)
        # hp.graticule()

        fig.savefig('movie/snaps/test_%05i.png' % (i+1))

