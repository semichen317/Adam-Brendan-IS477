# IS 477 Interim Status Report - Adam Chen & Brendan Speckmann
## **Updates**
### DataONE Data Lifecycle: 
We actually have not followed this data lifecycle that closely. This data lifecycle was not the most practical framework for our project. We followed a much more data science focused data lifecycle. One data lifecycle we could use is the Data Science Pipeline / Lifecycle created by our Data Science team here at UIUC. This one is shaped more like a pipeline and less like a cycle, which is better for our start to this project. We collected the data from the Divvy website as a CSV, and the NOAA website as an API. Next we prepared the data in order to be ready for cleaning. Finally, we cleaned the data using pandas. Next we will need to get important statistics, create visualizations, and start automating this workflow to finish the pipeline.

### Collection and Acquisition: 
For collection and acquisition, we used the requests and os library to grab the data from the websites

Divvy: Downloaded monthly trip datasets (May 2024 – May 2025).

NOAA: Queried the Chicago station for the same date range through the NOAA API.

### Storage and Organization: 
For storage and Organization, we still decided to use pandas dataframes as they are super user friendly and quite applicable to our research question. We also decided to organize our github in an easier to use file system. So far, the relevant one has been data. We split the data folder into three subfolders: raw, interim, and processed. We put the raw data from the websites into the raw folder. We used the interim folder to transfer the useful information into the processing step of data. Finally, we took the enriched data and cleaned it, and dropped it into the processed folder. In our initial plan, we had the datasets combined already. We intentionally have not combined the datasets yet, since cleaning them separately is more efficient. Integration will occur in the analysis phase.

### Extraction and Enrichment: 
For extraction and enrichment, we created two different scripts for each dataset individually. For the NOAA data, we picked the Chicago station from one full year plus an additional month, May 1st 2024 to May 31st 2025. We built two functions, one called download_year which extracted the info from the API, and another called build_raw which built the raw_dataset used to put in the interim folder to be cleaned. For the Divvy data, we extracted the bike data from May 1st 2024 to May 31st 2025. We then created multiple functions to help extract the data we wanted. First we made download_divvy to download the data. Next we made extract_zips which separates the zip files into usable files. Finally, since there are multiple csv_files, we grabbed the hourly demand with parameters started_at, start_station_id, start_lat, start_lng.

### Data Quality: 
The raw data from both sources was already structurally consistent and semantically valid. Only minimal data quality checks were required.

### Data Cleaning: 
We created two data cleaning scripts for both datasets. For the NOAA data, we adjusted a bunch of data to be readable and usable by pandas. We changed the DATE label to datetime and made it a datetime data type. We took the datetime and specifically only grabbed the hour. We changed TMP to temp_c and parsed the temperature data. We changed WND to wind_ms and parsed the wind data. We changed AA1 to precip_mm and parsed the precipitation data. For the Divvy Data, we first changed the start_station_id into a string, hour into datetime, and trips into numeric. We then dropped any trips that didn’t change to the numeric data type or were incorrect (like less than 0).

### Data Integration: 
We have not integrated the data yet. Will do later this semester.

## **Timelines**
Week 1: Dataset initial merge and alignment. Convert both datasets to a shared hourly timestamp format, align time zones and handle missing hourly intervals.

Week 2: Final integrated dataset, with all weather-Divvy related features, including trip demand. Export clean integrated dataset to processed folder.

Week 3: Snakemake workflow implementation, creat Snakefile with proper input and output for each rule.

Week 4: Fully pipeline automation and documentation/visualization.

## **Project Plan**
We did not strictly follow the original data lifecycle plan because we found that the traditional model didn’t fit the practical workflow of our project. As the work progressed, we shifted to a more linear data science pipeline that better supported our tools, data structure, and overall efficiency. All other components of the project have followed the original plan.

## **Summary of Personal Contribution**
### -Adam Chen
Developed the two data preparation scripts: divvy_prepare.py and noaa_prepare.py

Designed and organized the project folder structure to support a clean and reproducible workflow.

Wrote the remaining sections of the Status Report following the Updates section.
### -Brendan Speckmann
Developed the two data cleaning scripts: cleaned_divvy.ipynb and cleaned_noaa.ipynb, completing the cleaning and validation steps for both datasets.

Wrote the Updates section of the Status Report.

