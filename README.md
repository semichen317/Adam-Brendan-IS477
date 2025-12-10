# How Weather Changes and Time of Year in Chicago Affect Share Bike Usage 
## Contributors 
* Brendan Speckmann 
* Adam Chen

## Summary

Our project was set out to answer How Weather Changes and Time of Year in Chicago Affect Share Bike Usage. The datasets we used were Divvy’s monthly trip data and the National Oceanic and Atmospheric Administration’s (NOAA) hourly weather data. We saw an opportunity to merge these two public datasets and predict hourly ridership data. The goal was not only to attain the results of this analysis but also to construct an automated and reproducible pipeline from data merge to visualization. 

For Divvy datasets, we selected a time range from May 2024 to May 2025 to reflect recent riding habits. We downloaded twelve monthly files from Divvy, which brought the data count to over 1.2 million rows. Each row is a trip, and our research was based on specific start times. This enabled the individual rides to be bundled together as hourly counts. 

NOAA’s Global Hourly weather data was acquired from the O’Hare (ORD) station, selected as a representative geography for the Chicago region. Standard parameters were selected: temperature, wind speed, pressure, and precipitation. The cleansing process was more complex since data was stored in coded formats in some cases. For example, temperature is recorded in tenths of degrees Celsius. It was necessary to convert the columns to metric numeric quantities and then filter the rows to match the Divvy dataset exactly.

Once both datasets were cleaned, we merged them by the hourly timestamp. This created a single dataset which determined the ride counts with weather and time parameters for every single hour of the year. Such a structure was optimal for identifying trends, allowing for direct demand comparisons for warm summer afternoons versus cold winter mornings.

For the modeling part, we chose a Random Forest Regressor. Since the dataset was huge, we sampled 50% of it to keep training times reasonable without sacrificing too much information, using an 80/20 train-test split. The model actually performed pretty well. The baseline standard deviation for hourly trips is about 3.09, but our model achieved an RMSE of 2.11. That’s roughly a 33% improvement over the baseline, which tells us that weather and time variables definitely explain a significant chunk of the variance in share bike demand.

Visualization of the findings consisted of a correlation heatmap and subsequent actual-predicted scatter plot. The heatmap indicated that temperature is the strongest correlation to ridership. Wind and rain lack stronger correlations, possibly due to fewer instances of extremes weather occurring on an hourly basis. The scatter plot served as a sanity check to ensure that the model was consistent without bias. 

In conclusion, the project was able to show that while weather is not the only determining factor, temperature is a very strong signal for Divvy demand prediction. In addition to the results, it was able to incorporate the entire workflow into a fully automated process. This can be achieved by executing run_all.py to trigger the code for every step from raw data intake to the final visualization.

## Data Profile

### Divvy
The Divvy dataset is our main source for shared bike activities in Chicago. For this project, we used time range from May 2024 through May 2025. Divvy publishes monthly trip files on its website, which are open to everyone. After putting everything together, the dataset had well over one million rows. 

For its content, each trip record includes ride started time, ride ended time, and which stations were used. It also tells us the latitude and longitude of each station and whether the rider is a member or a casual user. The start time was the most important field for us, because it allowed us to group rides by hour. Once we counted trips for every station in every hour, we could compare bike demand to the weather at that same time.

For ethical and legal constraints. Divvy datasets does not include any personal or sensitive data about riders. There are no names, home addresses, phone numbers, or anything that could be used to identify someone. Everything is at the trip level or station level. Because of that we did not have to deal with privacy concerns, and our analysis stays within an acceptable ethical boundary. Divvy makes these files public specifically for research and public use, so using them for a class project is allowed. However, the data should not be used to guess personal travel patterns or anything that targets individuals. Our project only looks at overall trends and hourly demand, so we remained within the intended use of the dataset.

### NOAA
The second dataset we used for this project was from the NOAA Global Hourly system. NOAA collects weather information from stations across the country. We chose one station (ORD) located in the Chicago area and downloaded weather data for the same date range as the Divvy data. We used the NOAA API to get the files. 

About its content, the dataset includes temperature, wind speed, rain measurements, pressure, and more. Some fields are stored in coded formats, so we had to clean them. For example, temperature values are given in tenths of a degree Celsius, so a number like “0134” means 13.4°C. Wind speed is also coded inside a string of numbers. We converted these into normal numeric values so we could actually use them. We also made sure that every row represented one hour, because we wanted it to match the hourly bike counts from Divvy.

For ethical and legal constraints, NOAA weather data is very easy to work with. It is public domain information, meaning anyone can use it without restrictions. It does not contain any personal data, and all the readings come from automated weather stations. The only real rule is that users should not overload the API with nonstop requests. Our project only needed a small number of calls, so we followed the guidelines without any issues.

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

## Findings, Visualizations, Workflow Automation
Our whole goal for this research question was how does weather and time of year effect bike rental usage. If put into affect, this model could be used by Divvy Bikes to see when their bikes are used most and least frequently. Then, we could predict future number of trips based off of the weather and the season. After finding our datasets and preparing, cleaning, and integrating the datasets, it was finally time to start analyzing. 

For some summary statistics, there were 1,266,795 rows in the dataset. For the years we looked at the data, the average bike trips per hour were 2.67, with a standard deviation of 3.09. That is a lot of data, and training that data would take too long. So I decided to sample half the data. This drastically improved train time for our model while still able to make generally accurate predictions. This is due to the fact that our data is taken every hour. In theory sampling half the data removes 1 out of every two hours. But the temperature, wind, and precipitation don't change that drastically per hour, so our predictions would be relatively safe from random variance by sampling. 

For the model, I decided to use a RandomForestRegressor from the scikit-learn ensemble library with 200 trees. 200 trees is double the standard paramter number of 100. This is due to the fact that we have around 600,000 samples, and more trees would help learn the pattern of the data. I got an RMSE of 2.11. Based off of the standard deviation of 3.09 and a baseline RMSE with no analysis of 3.06, this is about a 33% increase in performance, which is solid. 

For visualizations. I decided to use two: a correlation heat map and a actual vs. predicted scatter plot. For the correlation heat map, it looked at the correlation between temperature, wind speed, precipitation, and trips. The goal was to see which weather patter, if any, had the most effect on number of trips. Looking at the graph, wind speed and precipation had almost no effect, while temperature had a slight correlation. This makes sense, since high wind speeds and precipation are rare in the dataset, so the amount of trips wouldn't be effected as much overall. But temperature swings a lot, so it is easier to capture a relationship between temperature and trips. For the actual vs. predicted scatter plot, we can see that the our model performed well. If the model overfit to the data, we would see much more variance in the graph. If the model was biased in any way, we would see a curve. By looking at the data, it seems well dispersed, and not too variable based on how many samples we had. 

Data Analysis Script:
1. Reads the integrated dataset from the interim data folder
2. Preproccesses the data by: 
3. Dropping any row with NaN values
4. Encodes categorical variable start_station_id
5. Adjusts hour to datetime data type
6. Splits hour into 3 different numeric columns of hour_of_day, day_of_week, month
7. Drops the original hour and start_station_id variables for testing
8. Samples 50% of the original data since dataframe is too big for analysis
9. Splits the data further into 80% of the sample data as training data, and 20% as testing
10. Fit a RandomForestRegressor from scikit learns ensemble library
11. Used Root Mean Squared Error to see model performance

Data Visualization Script:
Created a Correlation Heatmap using the seaborn module. Checks which weather types are more correlated to the amount of trips taken during that hour. Created a Scatter Plot from the Matplotlib.pyplot module for actual trips vs predicted trips. Shows if the model is biased and the variance between actual and predicted trip values.

Workflow Automation Script:
This project includes a fully automated Run All script that reproduces the entire data pipeline from raw acquisition to final analysis and visualizations. Running this script allows any user to regenerate all intermediate and cleaned datasets, integrate the sources, build the predictive model, and recreate all figures used in the project.
The data workflow is split into 4 parts:
1. Data Acquisition of the NOAA and Divvy datasets
2. Data Cleaning and preprocessing
3. Data integration for analysis
4. Analysis and Visualization

The run all script is structured in this order:
python scripts/prepare/noaa_prepare.py

python scripts/prepare/divvy_prepare.py

python scripts/cleaned/cleaned_noaa.py

python scripts/cleaned/cleaned_divvy.py

python scripts/integrated/integrated_script.py

python scripts/analysis/analysis.py

## Reproducing

### Before we start
The full analysis step trains a machine learning model on a large integrated dataset. This process can use a significant amount of memory and CPU. Because of this, we strongly recommend not running the full pipeline inside GitHub Codespaces. Codespaces has limited system resources, and the analysis step may terminate early or fail due to memory constraints.

### Step 1: Set up the project

Clone the repository and make sure the folder structure stays the same. The folders inside data and output will be filled automatically when the script runs.

### Step 2: Install the required packages

Run: pip install -r requirements.txt to install the tools we used. This makes sure the environment matches ours.

### Step 3: Run everything with one command

To reproduce the full workflow, simply run: scripts/python run_all.py

This script will download the Divvy and NOAA data, clean both datasets, merge them into one file, and then run all of our analysis steps. It will also generate the final plots and tables in the output folder.

### Step 4: Check the results
All results will appear in the data/processed and figures folders.


## Future Work
In this section we will look at my models performance from a heuristic approach to determine if it should be used in the real world or not.

We learned a few lessons while working with this dataset. First of all, working with a lot of samples is challenging. It slows down production and creates tough decisions on what to use and what to leave out. It was hard to train the model and tune hyperparameters because the train time would always take around 3 minutes. We also learned that an open data license and public domain license is very nice to work with. Not many restrictions, and accessing the data was easy since the datasets were already in a ready-to-use format. 

### Benefits of the model
Our model has a few benefits. First, it is incredibly timely as mentioned above. Our data is from within two years, making predictions relatively accurate since our data is current. I also think our model is excellent at accomplishing our research task. Our research task was all about bike and weather data in Chicago. Our datasets were both set in Chicago, so you could actually use the predictions in the real world since we are not extrapolating to other cities. A final benefit to our model is that it is simple and very interpretobale. We have only 7 features and one predictor. All the columns are also easy to understand from a non-technical perspective. Finally, our predictions are easy to explain to a representative from a company. We could easily pitch this model to a company and they would understand what it's task and findings would do for them.

### Limitations of the model
Our model does come with limitations. Adjusting the model takes some time since we have so many samples in our dataset. So if we want better performance or the model stopped performing up to standards, it would take a bit of time to adjust it. Besides that, I don't think there are too many limitations to this model. 

### Risks of the model
Our mdoel could be risky for the Divvy Bike company. The RMSE is low, but not low enough that there will be no bad predictions. Underestimating the amount of trips people take could really hurt the companies profits if they followed our model but don't have enough bikes out in the streets. This would fall onto us as our model wouldn't be accurate enough for them to sustain a healthy business. Another risk is the possibility of weather swings. While this isn't our model's fault, weather swings could either make it so that the company doesn't have enough bikes for trips, or that their bikes get damaged by bad weather. I don't think this would hurt our conceptually idea of the model, but it is something to look into to improve the model performance and company satisfaction. 

### Improvements to our model
I think there are many improvements for this model, specifically some are tied to the risks mentioned above. First, the model could actually just improve its RMSE value. I used 200 estimators because of the dataset size and train time. Realistically, this number could probably be higher to learn the patternd of the data better without overfitting. Setting the max_depth parameter so that the trees don't get too big would help the train time if we increased the number of trees used. Secondly, we could use a different model based on company needs. If the company was really afraid of underestimating the number of bikes needed on the streets, we could implement a bias term to help increase the predicted number of trips on average.

## References
Divvy. (2024, June 26). *Divvy-tripdata. Divvy-Tripdata.* s3.Amazonaws.com. https://divvy-tripdata.s3.amazonaws.com/index.html

*NCEI Data Service API User Documentation.* (2017, June 20). National Centers for Environmental Information (NCEI). https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation
