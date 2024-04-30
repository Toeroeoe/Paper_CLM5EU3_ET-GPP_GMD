# CLM5EU3_Ecosystem_Processes

## Usage
- Download and install my_py (LINK)
- Confirm the sites that you want to investigate in user_in/csv/stations.csv
- Specify the gridded and in-situ sources you want to use in ´user_in/run_analyses.py´
- Check the details, e.g., start and end year, time resolution, etc., in ´user_in/run_analyses.py´
- Confirm the analysis that you want to do in user_in/run_analyses.py
- run the analyses: ´python user_in/run_analyses.py´

## Data
- Intermediary data for each ICOS WARMWINTER2020 station (https://www.icos-cp.eu/data-products/2G60-ZHAK) used in this study is stored in the folder out/CLOSE_<variable_names>/parquet/ as parquet files.
- The 'Extracted_*' parquet files contain the extracted data for each station per data set.
- The 'In_Situ_*' parquet files contain the corresponding data from the ICOS observations.
- The 'Resampled_*' files contain the data from above, resampled to 8-daily time frequency. These were used for the analyses.
  
