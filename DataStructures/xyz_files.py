# Script to fix sparse .xyz files - adapted from https://www.gpxz.io/blog/fixing-sparse-xyz-files

import numpy as np
import pandas as pd

def get_files(in_path, out_path,res, val):
  # in_path is the path to the text file, outpath is the path to the .csv to be created, res is the resolution, val is the value to be inserted where there is no data.
  input_file = in_path
  output_file = out_path
  df = pd.read_csv(input_file, sep='\s+', header=None, names=['x', 'y', 'z'])
  # Figure out which x and y values are needed.
  x_vals = set(np.arange(df.x.min(), df.x.max() + res, res))
  y_vals = set(np.arange(df.y.min(), df.y.max() + res, res))
  # For each x value, find any missing y values, and add a NODATA row.
  dfs = [df]
  for x in x_vals:
      y_vals_missing = y_vals - set(df[df.x == x].y)
      if y_vals_missing:
          y_val_miss_array=[i for i in y_vals_missing]
          data={'x': x, 'y': y_val_miss_array, 'z': val}
          df_missing = pd.DataFrame(data)
          dfs.append(df_missing)
  # Build full csv, and sort to xyz spec.
  df = pd.concat(dfs, ignore_index=True)
  df = df.sort_values(['y', 'x'])
  # Check.
  assert len(df) == len(x_vals) * len(y_vals)
  # Output.
  df.to_csv(output_file, index=False, header=False)
  
if __name__ == '__main__':
  resolution=10
  value=-9999
  input_path='C:/WRITE_PATH_HERE/Sheet233v4.txt'
  output_path='C:/WRITE_PATH_HERE/Sheet001v4.csv'
  get_files(input_path, output_path,resolution, value)
