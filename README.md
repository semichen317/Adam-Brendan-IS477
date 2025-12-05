# How Weather Changes and Time of Year in Chicago affect Bike Rental Usage 
### Contributors 
* Brendan Speckmann 
* Adam Chen

## Data Quality 
Data quality is super important for these two datasets. For the NOAA dataset, they use their own units for temperature, wind speed, and precipation. So we have to make sure that we are adjusting their units to benefit our needs. Secondly, missing values or inconsistent values are plausible when looking at weather data tracked in real time. Making sure these are dealt with helps make our analysis more accurate. For the Divvy dataset, we had to check to make sure there are no missing values or inconsistent values so that we can more accurately predict number of trips based on the weather. For both datasets, making sure that hour was properly formatted for our merge is important so that we don't accidentally have duplicate data points. 

For Data Completeness, I would say the data was quite complete. We had every variable that we wanted to do analysis for, and there were not too many missing values that would harm prediction. Since this data is recorded every hour, even if data was missed for a certain hour, that wouldn't effect our analysis too much since the datapoints around that hour would be quite similar.

For Data Accuracy, I would say the data was somewhat accurate. We did have to clean for inconsistent values. For example, the NOAA missing value code was 9999, so we had to change those values to NaN for better accuracy in analysis. For the divvy data, we had to make sure that semantically the trips variable was accurate. Syntactically, there were a few adjustments with punctuation and making sure datatypes matched. 

For Data Timeliness, I think our research question did a really good job making sure our data was quite timely. We used data from May 2024 - May 2025 inclusive. This data is is within two years of current time, so any future predictions should be based off of recent data. 

For Data Consistency, the datasets were very clean to start with. There weren't any datatype mismatches, incorrect spellings of station_id's (that we could see), or incorrect data in the hour column. Besides the cleaning mentioned below, the data was quite consistent which is very helpful for analysis

Data Profiling steps for the NOAA Weather data:
1. Checked for missing and syntactically wrong data in the raw data fields
2. Identified the missing value codes 9999 or 99999
3. Standardized and checked for irregularities of the Date variable
4. Checked for duplicates within the raw data fields

Data Profiling steps for Divvy Bike data:
1. Checked for missing start_station_id's
2. Verified that the trips column could be changed to numeric
3. Checked for semantically incorrect trip values
4. Made sure hour variable could be converted to datetime
5. Checked for duplicates within the raw data fields

Data Cleaning steps for the NOAA Weather data:
1. Imports raw data CSV file from the data directory
2. Checks raw data for missing values or NOAA's missing value code
3. For temperature, the script extracts the first four digits and rounds to the tenth place in degrees Celsius
4. For wind speed, the script converts the wind speed into meters per second and replaces commas with periods for conversion to floats.
5. For precipitation, the script takes in the accumaltion of all rain water into one hour and converts it into milimeters
6. The cleaning script also takes the Date variable and converts it into pandas datetime variable, and floors the minutes so that the hours are uniform.
7. The script get's rid of exact duplicate hours samples, and converts all missing data into numpy's NaN
8. Finally, the script only keeps the variables hour, temp, wind speed, and precipation and saves it as a CSV. 

Data Cleaning steps for the Divvy Bike data:
1. Checks for missing start_station_id's and ensures the datatype is a string
2. Makes sure hour is a numpy datetime and trips is numeric
3. Removes rows where trips is missing
4. Sorts rows by station_id and hour, and converts this cleaned dataframe to a CSV
