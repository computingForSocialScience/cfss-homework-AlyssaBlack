This project was done by Alyssa Blackburn and Marie Hilliard

To run:
1) run censusFinal.py: this will create and populate the mysql tables
- Note: if this is taking too long: In line 73, restrict the number of geoIDs selected, when we presented to Michael we restricted to 3.
2) run webpage4.py: this will launch the website
Notes: 
-The html files need to be in a "templates" folder in the same folder as censusFinal.py and webpage4.py
-There needs to be a "static" folder (with a "temp" sub folder) in the same folder as censusFinal.py and webpage4.py (to embed the scatterplot).

Problems:
-Because it takes so long and is so difficult to load the entire dataset there may be errors that we have not found. Even restricted the geoIDs to 3, that's still 225 possible combinations.
The first complete dataset we ran was over 9,000 rows.
-The scatterplot does not plot a linear trend line.
-The drop down menus display all possible columns but do not indicate which table the column is selected from. We think this would have been simple to fix with the <optgroup> tag, we only lacked the time.
-Our code pulls the denominator id and values from the chosen table, but we didn't have time to code anything with those values. The linear regression and scatter plot use only the raw table values.

If something appears to be broken or cannot be found, please email either of us: alyssablackburn@uchicago.edu and amarie@uchicago.edu
We've gone through many versions of code, and there may have been a discrepancy between versions.
We really enjoyed this class! We wish it was more than a quarter, a year sequence would've been nice to get into the nuances of flask and mysql.