### Date created

20/02/2020

### Project Title

Explore US Bikeshare Data

### Description

I use Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.
I used pandas,numpy and datetime libraries too.
I write code to import the data and answer interesting questions about it by computing descriptive statistics.I also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.
Users are able to filter the information by city, month and weekday, in order to visualize statistics information related to a specific subset of data. The experience is interactive. The application offers the user the choice of choosing the desired city, month and weekday.
Questions analysed in project:
1 Popular times of travel (i.e., occurs most often in the start time)
most common month
most common day of week
most common hour of day
2 Popular stations and trip
most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)
3 Trip duration
total travel time
average travel time
4 User info
counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Files used

bikeshare.py
washington.csv
new_york_city.csv
chicago.csv

Requirements:
Python 3 with pandas and numpy libraries

### Credits

Link that have helped me to do the project:
counts value
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html
mode():
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html
general informations about pyhon
https://www.w3schools.com/python/default.asp
classic overflow questions in this example sum datetime
https://stackoverflow.com/questions/38229357/how-to-sum-time-in-a-dataframe
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.idxmax.html#pandas.core.groupby.DataFrameGroupBy.idxmax
