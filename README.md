# How Weather Changes and Time of Year in Chicago affect Bike Rental Usage 
## Contributors 
* Brendan Speckmann 
* Adam Chen

## Data Profile
Developing-Adam

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
Developing-Adam
To reproduce workflow:
1. Download or clone the repository
2. Make sure system dependencies is the same
3. Run the workflow script

Output locations:
The data is stored in the data folder. Acquisition and raw data is in the prepare folder (some raw data not available due to licensing). Cleaned data is in the cleaned folder. The integrated dataset is in the integrated folder. Visualizations are in the figures folder.

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
Developing-Adam
