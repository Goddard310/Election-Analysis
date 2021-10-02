# Election Analysis
&nbsp;See PyPoll_Challenge.py

## Overview of Project
Tom and his manager would like to review the results and turnout of three counties in the Colorado election.  The goal will be to be able to duplicate this analysis over any future election data regardless of counties selected.   
### Purpose
We would like to compare and contrast varying sized counties and how each candidate performed.  Additionally, we can use this data to consider turnout by population in future analysis. 

## Election-Audit Results
- Total Votes:  369,711

### Total by County
- Arapahoe:  6.7% (24,801)
- Denver:  82.8% (306,055)
- Jefferson: 10.5% (38,855)

**Denver was far and away the most important county in the district with 8x the next highest county in the sample** 

### Total by Candidate
- Diana Degete:  73.8% (272,892)
- Raymon Doan:  3.1% (11,606)
- Charles Stockham:  23.0% (85,213)

**Diana Degete ran away with this election with over 3x the next highest vote getter**

![Alt text](https://github.com/Goddard310/Election-Analysis/blob/main/PyPoll%20CO%20Analysis.png)

## Election-Audit Summary

- As it should be clear to the management team, Denver is where most campaign efforts and dollars should be spent <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;While Ms. Degete won Denver by a similar margin, she didn't need the other counties <br />
- This process is replacable in different districts <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Change the imported csv and path <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update the county dictionary keys and values
- Run turnout for campaign success and voter interest <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Would need population data but not necessarily in the csv.  In fact, it would be better served in a dictioinary <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;See and update current code section 122 to 138 (incl. the above dictionary appendment <br />
  

