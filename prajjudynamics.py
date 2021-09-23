# libraries required
import xarray as xr
import numpy as np
import glob
import pandas as pd





#function for calculating relative humidity using specific humidity,temperature and pressure data
def RH(spec_hum,T,pre):
	vp = (spec_hum*pre)/0.622 # in pascals
	a = -6096.9385
	b = 21.2409642
	c = -2.711193e-2
	d = 1.673952e-5
	e = 2.433502
	vs = xr.ufuncs.exp( (a/T) + b + (c*T) + (d*T**2) + e*xr.ufuncs.log(T))

	RH = 100*(vp / vs)
	return (RH)

# function for converting UTC to Local Time
def LST(utc,longitude):
	lst = utc+(longitude/15)
	return (lst)
