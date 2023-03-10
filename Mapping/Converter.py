# Script to fix sparse .xyz files - adapted from https://www.gpxz.io/blog/fixing-sparse-xyz-files

import numpy as np
import pandas as pd
# You will need an additional library but this one comes with Python so shouldn't need to pip install anything for this.
import re

def strip_content(in_path, text_outpath):
  """ This function reads through the text file and uses regular expressions to find entries that do not conform to the [x,y,z] column structure,
  it also removes repeated entries of (2.5, 1, 0). """
  # Creates an array to store the lines in the text file
  lines = []
  # Open the text file and read its contents line by line
  with open(in_path, "r") as input_file:
    # Open the output file for writing
    with open(text_outpath, "w") as output_file:
        for line in input_file:
            # Use regular expression to check whether the line matches either of the stated patterns in the function description.
            if re.match(r"^\s*\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s*$", line) or re.match(r"^\s*2\.5000\s+1\.0000\s+0\.0000\s*$", line):
                # If the line matches, ignore it and continue to the next time.
                continue
            # If the line doesn't match, write it to the output file
            output_file.write(line)


def get_files(in_path, out_path,res, val):
  # in_path is the path to the text file, outpath is the path to the .csv to be created, res is the resolution, val is the value to be inserted where there is no data.
  input_file = in_path
  output_file = out_path
  df = pd.read_csv(input_file, sep='\s+', header=None, names=['x', 'y', 'z'])
  print('Preview: \n',df.head())
  # Figure out which x and y values are needed.
  x_vals = set(np.arange(df.x.min(), df.x.max() + res, res))
  y_vals = set(np.arange(df.y.min(), df.y.max() + res, res))
  # For each x value, find any missing y values, and add a NODATA row.
  dfs = [df]
  print('Finding missing y values')
  for x in x_vals:
      y_vals_missing = y_vals - set(df[df.x == x].y)
      if y_vals_missing:
          y_val_miss_array=[i for i in y_vals_missing]
          data={'x': x, 'y': y_val_miss_array, 'z': val}
          df_missing = pd.DataFrame(data)
          dfs.append(df_missing)
  # Build full csv, and sort to xyz spec.
  print('Building .csv')
  df = pd.concat(dfs, ignore_index=True)
  df = df.sort_values(['y', 'x'])
  # Check.
  #assert len(df) == len(x_vals) * len(y_vals)
  ## Output.
  df.to_csv(output_file, index=False, header=False)
  
if __name__ == '__main__':
  print('Starting programme')
  resolution=10
  value=-999
  # path to original text file 
  input_path='C:/Users/Aaron/OneDrive/Documents/assembly/james code/Sheet070v4.txt'
  # path to where you want the cleaned text file to be saved
  text_cleaned_output_path='C:/Users/Aaron/OneDrive/Documents/assembly/james code/Sheet070v4_cleaned.txt'
  # path to where you want the .csv file to be saved
  output_path='C:/Users/Aaron/OneDrive/Documents/assembly/james code/Sheet070v4.csv'
  strip_content(input_path,text_cleaned_output_path)
  print('Text Cleaned')
  get_files(text_cleaned_output_path, output_path,resolution, value)
