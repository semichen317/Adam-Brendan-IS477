# IS477 Project Plan - Adam Chen & Brendan Speckmann

## **Overview**
For our project, our goal is to track weather data and bike usage to determine which times of the year bike companies see the most usage. The datasets we will use are from DivvyBikes and ncei.noaa websites. The DivvyBikes website gives information on usage of bikes. The ncei.noaa website has a ton of data on many big locations' weather stats. Combining these two datasets, we can start looking at bike usage based on weather. In a fictional scenario, we can help the bike companies determine when their bike stations are not being used so that they can store the bikes for better weather, or when their bikes are in high demand to potentially create new bike stations across Chicago.

## **Research Question**
How sensitive is hourly bike demand to weather in the Chicago metropolitan area from May 2024 to May 2025?

## **Team members**
Adam Chen- Will responsible for Module 1, 7, 8, 9, 

Brendan Speckmann- Will responsible for Module 2, 6, 11, 12

For the rest of the modules we will work together.

## **Datasets**
https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation  
This dataset will be accessed through an API key. The request is free and would return in JSON. Some parameters that would be useful would be date, station, name, precipitation, wind speed, dew point, temperature. 

https://divvybikes.com/system-data
This dataset is publicly available and needs no API key. Real-time feeds follow the GBFS standard and return JSON; historical trip data is downloadable as CSV. Some fields that would be useful include: Station ID, Station Name, Latitude, Longitude, Capacity, Number of Bikes Available, Number of Docks Available, Renting Status, Last Reported Time, Ride ID, Start Time, End Time, Start Station ID, Start Station Name, End Station ID, End Station Name, Start Latitude, Start Longitude, End Latitude, End Longitude, Rider Type (member or casual), Bike Type.

## **Timeline**
### *Data lifecycle (cf. Module 1): Week 1*
We will use the DataONE Data Lifecycle. This data lifecycle is simple to understand, effective, and communicates each step the data goes through along the way. Since our project will be reported on GitHub, having a data lifecycle that clearly expresses the processes and changes it went through is beneficial to our peers.

### *Ethical data handling (cf. Module 2): Week 1*
The API key for the weather dataset has free access. A request needs to be authorized, but the data is open access. The API follows the government HTTPS policy

### *Data collection and acquisition (cf. Module 3): Week 2*
The data collected for the weather dataset will use an API and will be requested as JSON. This will be changed into a pandas dataframe and merged with the bike dataframe. 

### *Storage and organization (cf. Modules 4-5): Week 2*
The organization of this data will be a structured, tabular dataframe. 

### *Extraction and enrichment (cf. Module 6):Week 3*
Implement two extractors: NOAA (hourly weather for Chicago) and Divvy (trip + station status). Standardize a skinny schema (timestamp, station_id/area_id) and add derived features—hour-of-day, peak flags, rolling weather means (1–3h), and lagged precipitation/wind.

### *Data integration (cf. Module 7-8): Week 3*
Align everything to America/Chicago and round to hourly bins. Resolve station name changes with a surrogate key table. Join weather to stations via nearest-weather-point (≤1 km) or area centroid, then aggregate trips to hourly demand per station and neighborhood.

### *Data quality (cf. Module 9): Week 3*
Add checks (ranges, nulls, duplicates, bikes≤capacity) with Great Expectations.

### *Data cleaning (cf. Module 10): Week 4*
Impute short gaps with time interpolation/FFILL (bounded by capacity) and flag imputed cells. Cap extreme demand with IQR/MAD rules, and drop stations with >30% missing hours or <14 active days. Keep a changelog (rows affected, rules applied) for auditability.

### *Workflow automation and provenance (cf. Module 11-12): Week 4*
Orchestrate extract to clean with Makefile/Prefect; capture run metadata (commit, params, sources).

### *Reproducibility and transparency (cf. Module 13): Week 5*
Pin environment (requirements.txt), publish docs (methods, assumptions, data dictionary) to the repository. With a README, data dictionary, and methods/assumptions page (limits, bias risks). Add license/citation files and note any API rate-limit constraints.

### *Metadata and data documentation (cf. Module 15): Week 5*
Metadata for the weather dataset can be found through the ncei.noaa website. They have extensive searching options to get exactly what we would need. You can download the metadata through JSON or XML file formats. This would be useful at the end of our project to help with reusability. 


## **Constraints**
There are many possible constraints with our research question. First, there could be missing data in either of the datasets. At this current point, we have yet to merge the datasets, so there could be a lot of potential data cleaning required. Missing data can result in over generalized predictions, however with this current research question I don’t think it will cause big issues. Another possible issue could be the time constraints on the data. DivvyBikes website has a lot of samples in their data. For our program to run smoothly, we can’t afford to have millions of samples so our time frame has to be short. With a short time frame comes hyper selective data. Only using one year, which is our current plan, could cause some issues. Maybe the 12 months we chose had higher wind, rain, or temperatures recorded than usual. Our predictions may be skewed based on the weather year that Chicago had. Our predictions also cannot be generalized outside of the Chicagoland area, since all of our data was recorded from Chicago.   
	

## **Gaps**
In terms of gaps in the data, all of the features are quite easy to understand for someone unfamiliar with the dataset. The predictions are also quite applicable and easy to explain, so there are no gaps in understanding of where the predictions came from. The datasets are quite thorough in the information provided. At this moment, I don’t think there is any information that would drastically help or change predictions made. The only gaps so far are the gaps in class knowledge of our project plan. The more we learn, the better our plan will become on how we can make this project better.
