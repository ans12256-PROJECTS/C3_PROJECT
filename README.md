[Proposals](https://docs.google.com/document/d/1DXd0z_BNmHpS3LCCnwTf-8QQH-7FebiE_zQ_-qYw7J0/edit#)

Project Idea #1):
Topic: Google Local Reviews
High level description of project: Build recommender(s) using a variety of configurations, deploy on AWS using Spark, finalize on the web using Flask. Explore scalability and performance.
Data Source(s): [Places Data](http://deepyeti.ucsd.edu/jmcauley/datasets/googlelocal/places.clean.json.gz), [User Data](http://deepyeti.ucsd.edu/jmcauley/datasets/googlelocal/users.clean.json.gz), [Review Data](http://deepyeti.ucsd.edu/jmcauley/datasets/googlelocal/reviews.clean.json.gz)
Description of Data: These datasets contain reviews about businesses from Google Local (Google Maps). Data includes geographic information for each business as well as reviews.
Reviews:
11,453,845
Users:
4,567,431
Businesses:
3,116,785

# Data Processing
Original data *.clean.json files are rows of dictionaries, that would not import using standard pandas
```
df=pd.read_json('../data/places.clean.json')
```

* [json_convert.py]('src/json_convert.py') this script reads, processes, and saves original json files in pandas readable format. total run time 1h 43 minutes
```
base) alexey_imac@ALEXEYs-iMac src % python json_convert.py
STEP 1 df_places load time: 2.7260870933532715
STEP 2 df_places explode time: 816.2096629142761
STEP 3 df_places save json time: 13.365344047546387
STEP 4 df_places reload from json time: 39.496094942092896
STEP 1 df_reviews load time: 7.131134986877441
STEP 2 df_pdf_reviews explode time: 4040.660280942917
STEP 3 df_reviews save json time: 117.0224997997284
STEP 4 df_reviews reload from json time: 153.501229763031
STEP 1 df_users load time: 1.5642907619476318
STEP 2 df_users explode time: 934.1211636066437
STEP 3 df_users save json time: 11.650207996368408
STEP 4 df_users reload from json time: 39.83325409889221
Conversion total time: 6183.85197520256
(base) alexey_imac@ALEXEYs-iMac src %
```


(Optional) Potential Future Employer: Any business with the need to expand understanding of the customer base, and improve returning experience
Sources: [[1](https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local)], [[2](http://cseweb.ucsd.edu/~jmcauley/pdfs/recsys18a.pdf)], [[3](http://cseweb.ucsd.edu/~jmcauley/pdfs/recsys17.pdf)]
Papers:
* [Translation-based Factorization Machines for Sequential Recommendation](http://cseweb.ucsd.edu/~jmcauley/pdfs/recsys18a.pdf),
* [Translation-based Recommendation](http://cseweb.ucsd.edu/~jmcauley/pdfs/recsys17.pdf)



# ML recommender tools, performance and scalability
## What are you trying to do?
* Articulate your objectives using absolutely no jargon (i.e. as if you were explaining to a salesperson, executive, or recruiter). Again, this should be a description of a real world problem, not an algorithm you aspire to use.
* Explore ML recommender problem using one or several available recommender type databases. Demonstrate use of various tools, algorithms, and explore scalability and performance using Spark and AWS tools among others.

## How has this problem been solved before?
* If you feel like you are addressing a novel issue, what similar problems have been solved, and how are you borrowing from those? Note, at this point you should be citing papers, medium articles, or other sources from the data science community. You should have links to your research in your proposal document and cite previous work.
* [Ref. 9 Must-Have Datasets for Investigating Recommender Systems](https://www.kdnuggets.com/2016/02/nine-datasets-investigating-recommender-systems.html)
* Recommender problem is not new to the data science field. Comparison of available tools, databases of various density and size, as well as performance would be helpful in solidifyiong knowledge of the subject, and demonstrating mastery of the problem

## What is new about your approach, why do you think it will be successful?
* It's OK to be working on a problem that has been worked on before, but you do need to have some novel contribution to the project.
* There are a variety of tools available both for algorithms and scalability accommodations. Successful application of at least a subset of these should be both feasible and helpful.

## Who cares? If you're successful, what will the impact be?
* It is preferable to be asked 'Who cares' now then when you're telling someone about your project. Not every project needs to change the world, but project whose appeal is very niche might not be the best way to spend your time and energy.
* Recommender problems are some of the very common needs of any business. Having a solid mastery of the subject, as well as ability to articulate the matter to non-technical audience is required of any Data Scientist

## How will you present your work?
* Again, be ambitious in your proposals, but think about what is the most impactful way your project could exist.
*

## What are your data sources? What is the size of your dataset, and what is your storage format?
* You should no longer be analyzing csv files. Is the amount of data you have limiting the ways you can approach the problem? Would you have a different approach if you could collect more? Same as last capstone, you should have all of your data on day one.
* [REFERENCES:](https://www.kdnuggets.com/2016/02/nine-datasets-investigating-recommender-systems.html)
* [MovieLens 25M Dataset](https://grouplens.org/datasets/movielens/)
MovieLens 25M movie ratings. Stable benchmark dataset. 25 million ratings and one million tag applications applied to 62,000 movies by 162,000 users. Includes tag genome data with 15 million relevance scores across 1,129 tags. Released 12/2019
* [JESTER](http://eigentaste.berkeley.edu/dataset/)
Jester is a joke recommender system developed at UC Berkeley to study social information filtering. Jester is a joke recommender system developed at UC Berkeley to study social information filtering. Version 5.0, launched on April 1, 2015, includes new jokes and algorithms, and a redesigned interface.
* [Book-Crossings](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)
Book-Crossings is a book ratings dataset compiled by Cai-Nicolas Ziegler based on data from bookcrossing.com. It contains 1.1 million ratings of 270,000 books by 90,000 users. The ratings are on a scale from 1 to 10, and implicit ratings are also included.
The Book-Crossings dataset is one of the least dense datasets, and the least dense dataset that has explicit ratings.
* [Last.fm](https://grouplens.org/datasets/hetrec-2011/)
Last.fm provides a dataset for music recommendations. For each user in the dataset it contains a list of their top most listened to artists including the number of times those artists were played. It also includes user applied tags which could be used to build a content vector. Last.fm’s data is aggregated, so some of the information (about specific songs, or the time at which someone is listening to music) is lost. However, it is the only dataset in our sample that has information about the social network of the people in it.
* [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Database_download#English-language_Wikipedia)
Wikipedia is a collaborative encyclopedia written by its users. In addition to providing information to students desperately writing term papers at the last minute, Wikipedia also provides a data dump of every edit made to every article by every user ever. This dataset has been widely used for social network analysis, testing of graph and database implementations, as well as studies of the behavior of users of Wikipedia. One can also view the edit actions taken by users as an implicit rating indicating that they care about that page for some reason and allowing us to use the dataset to make recommendations.
As Wikipedia was not designed to provide a recommender dataset, it does present some challenges. One of these is extracting a meaningful content vector from a page, but thankfully most of the pages are well categorized, which provides a sort of genre for each. The challenge of building a content vector for Wikipedia, though, is similar to the challenges a recommender for real-world datasets would face. So we view it as a good opportunity to build some expertise in doing so.
* [OpenStreetMap](https://planet.openstreetmap.org/planet/full-history/)
OpenStreetMap is a collaborative mapping project, sort of like Wikipedia but for maps. Like Wikipedia, OpenStreetMap’s data is provided by their users and a full dump of the entire edit history is available. Objects in the dataset include roads, buildings, points-of-interest, and just about anything else that you might find on a map. These objects are identified by key-value pairs and so a rudimentary content vector can be created from that. However, the key-value pairs are freeform, so picking the right set to use is a challenge in and of itself. Some of the key-value pairs are standardized and used identically by the editing software—such as “highway=residential”—but in general they can be anything the user decided to enter—for example “FixMe!!=Exact location unknown”.
* [Python Git Repositories](https://github.com/lab41/hermes)
The final dataset we have collected, and perhaps the least traditional, is based on Python code contained in Git repositories. We wrote a few scripts (available in the Hermes GitHub repo) to pull down repositories from the internet, extract the information in them, and load it into Spark. From there we can build a set of implicit ratings from user edits.
We currently extract a content vector from each Python file by looking at all the imported libraries and called functions. In the future we plan to treat the libraries and functions themselves as items to recommend.
## Comparison
The various datasets all differ in terms of their key metrics. A summary of these metrics for each dataset is provided in the following table:
<table>
    <thead>
        <tr>
            <th colspan="6">Datasets Comparison</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Dataset</td>
            <td>Users</td>
            <td>Items</td>
            <td>Ratings</td>
            <td>Density</td>
            <td>Rating Scale</td>
        </tr>
        <tr>
            <td>Movielens 1M</td>
            <td>6040</td>
            <td>3883</td>
            <td>1,000,209</td>
            <td>4.26%</td>
            <td>[1-5]</td>
        </tr>
        <tr>
            <td>Movielens 10M</td>
            <td>69,878</td>
            <td>10,681</td>
            <td>10,000,054</td>
            <td>1.33%</td>
            <td>[0.5-5]</td>
        </tr>
        <tr>
            <td>Movielens 20M</td>
            <td>138,493</td>
            <td>27,278</td>
            <td>20,000,263</td>
            <td>0.52%</td>
            <td>[0.5-5]</td>
        </tr>
        <tr>
            <td>Jester</td>
            <td>124,113</td>
            <td>150</td>
            <td>5,865,235</td>
            <td>31.50%</td>
            <td>[-10, 10]</td>
        </tr>
        <tr>
            <td>Book-Crossing</td>
            <td>92,107</td>
            <td>271,379</td>
            <td>1,031,175</td>
            <td>0.0041%</td>
            <td>[1, 10], and implicit</td>
        </tr>
        <tr>
            <td>Last.fm</td>
            <td>1892</td>
            <td>17632</td>
            <td>92,834</td>
            <td>0.28%</td>
            <td>Play Counts</td>
        </tr>
        <tr>
            <td>Wikipedia</td>
            <td>5,583,724</td>
            <td>4,936,761</td>
            <td>417,996,366</td>
            <td>0.0015%</td>
            <td>Interactions</td>
        </tr>
        <tr>
            <td>OpenStreetMap (Azerbaijan)</td>
            <td>231</td>
            <td>108,330</td>
            <td>205,774</td>
            <td>0.82%</td>
            <td>Interactions</td>
        </tr>
        <tr>
            <td>Git (Django)</td>
            <td>790</td>
            <td>1757</td>
            <td>13,165</td>
            <td>0.95%</td>
            <td>Interactions</td>
    </tbody>
</table>

## What are potential problems with your capstone?
* More importantly, what is your plan to mitigate these problems? Again, being aware of previous solutions to similar problems gives you a template for successfully working with data of this type.
* Various densities and Rating Scales can prove to be challenging. Starting with the more straight-forward datasets, and progressing to more challenging time permitting is my mitigation plan.
## What is the next thing you need to work on?
* Getting the data, not just some, likely all? Understanding the data? Building a minimum viable product? Gauging how much signal might be in the data?
* EDA of the data
* Spark setup
* AWS setup
* Training time estimates
* Flask Web deployment
