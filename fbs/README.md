# Repos for feature based scheduler
(Working set up as of 03/27/2018)

Let's clone into a directory called `fbs_repos`

~~~
cd fbs_repos
git clone https://github.com/lsst-ts/ts_astrosky_model.git
git clone https://github.com/lsst-ts/ts_observatory_model.git
git clone https://github.com/lsst-ts/ts_scheduler.git
git clone https://github.com/lsst/sims_skybrightness_pre.git
git clone https://github.com/lsst-sims/sims_ocs.git
git clone https://github.com/lsst/sims_featureScheduler.git
git clone https://github.com/tribeiro/sims_speedObservatory.git
git clone https://github.com/lsst/sims_seeingModel.git
git clone https://github.com/lsst/sims_cloudModel.git
git clone https://github.com/lsst/sims_downtimeModel.git
~~~

# ts_observatory_model (feature/fail_state_in_get_slew_dela)

```
cd ts_observatory_model
git checkout feature/fail_state_in_get_slew_delay
eups declare ts_observatory_model -r . -t $USER
setup ts_observatory_model -t $USER
scons
```

# sims_ocs (feature/clean_fieldid_dep)

```
cd sims_ocs
git checkout feature/clean_fieldid_dep
eups declare sims_ocs -r . -t $USER
setup sims_ocs -t $USER
scons
```
# sims_seeingModel (master)

```
cd sims_seeingModel
eups declare sims_seeingModel -r . -t $USER
setup sims_seeingModel -t $USER
scons
```
# sims_cloudModel (master)

```
cd sims_cloudModel
eups declare sims_cloudModel -r . -t $USER
setup sims_cloudModel -t $USER
scons
```

# sims_downtimeModel (master)

```
cd sims_downtimeModel
eups declare sims_downtimeModel -r . -t $USER
setup sims_downtimeModel -t $USER
scons
```

# ts_scheduler (feature/cosmetics_main)

```
cd ts_scheduler 
git checkout feature/cosmetics_main
eups declare ts_scheduler  -r . -t $USER
setup ts_scheduler -t $USER
scons
```

# sims_featureScheduler (FSDriver/latest)

```
cd sims_featureScheduler 
git checkout FSDriver/latest
eups declare sims_featureScheduler  -r . -t $USER
setup sims_featureScheduler -t $USER
scons
```

# ts_astrosky_model (feature/clean_fieldid_dep)

```
cd ts_astrosky_model 
git checkout feature/clean_fieldid_dep
eups declare ts_astrosky_model  -r . -t $USER
setup ts_astrosky_model -t $USER
scons
```

# sims_speedObservatory (bugfix/work_with_latest_socs)

```
cd sims_speedObservatory
git checkout bugfix/work_with_latest_socs
eups declare sims_speedObservatory  -r . -t $USER
setup sims_speedObservatory -t $USER
scons
```

# sims_skybrightness_pre (master)

```
cd sims_skybrightness_pre
git checkout master
eups declare sims_skybrightness_pre  -r . -t $USER
setup sims_skybrightness_pre -t $USER
scons
```

If you already have the skybrightness data downloaded you can link it to this repo. For example:

```
ln -s /lsst_repos/sims_skybrightness_pre/data/healpix/ /home/username/fbs_repos/sims_skybrightness_pre/data
```

You will also need to copy over, or link to, the file `percentile_m5_maps.npz` to your `sims_skybrightness_pre` directory.

# Setup order

If things do not work, setup the packages again in this order

```
sim_ocs -t $USER
ts_scheduler -t $USER
sims_featureScheduler -t $USER
ts_astrosky_model -t $USER
```

Now run the command `which scheduler.py` and you should see something like
`~/fbs_repos/sims_featureScheduler/scripts/scheduler.py`
