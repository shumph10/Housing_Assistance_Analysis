# Housing_Assistance_Analysis
# Final-Project 

------------------------------ 

[Google Slide Presentation](https://docs.google.com/presentation/d/1s9Ti4Zeszc62lfZDuPkzGOmQ0C_9or1eFGBapOgqS2o/edit?usp=sharing)
[Dashboard](https://analysis-housing-assistance.herokuapp.com/results)

------------------------------ 

##**Overview**  

  

Our project focuses on affordable housing voucher's strain on governmental assistance programs as rent prices for many across the US skyrocket. We will use data from the US Department of Housing and Urban Development(HUD) to establish the fair market price for 2 bedroom houses in 2017 and 2022 as this is the figure primarily used to establish amount of governmental assistance awarded, subtracting income based recipient payments. HUD describes fair housing prices idealy being below 30% of total household income, requireing that participants in either Section 8(general housing assistance) or Section 202(elderly housing assistance) pay a minimum 30% adjusted monthly income towards rent. The rest of rent is the responsibility of the HUD voucher program. Low income thresholds (those eligible for assistance) will be established, corresponding by county to determine the typical amount of rent paid by assistance recepients in that area for both years.  

  

Our hypothesis is while incomes have remained similar between years, rent prices have increased in many areas drastically putting significant strain on governmental assistance program to make the difference as recepients have a maximum threshold set by income. We aim to determine what the government payout difference is and use a machine learning model to determine clusters of areas with greater voucher payout increase as well as what factors have the most significant weight in this increase. The alternative hypothesis is there is no correlation between increased rent and government assistance program payout in 2017 and 2022.  

  

These years (2017 & 2022) were selected to examize rent increase in the wake of the influence of the COVID-19 pandemic. As supply-chain issues insued, many jobs were lost or suspended for long periods of time, and temporary halt in residential evictions left landlords attempting to recoupe profit, rent in many areas of the United States have increased. A year before the onslought of the pandemic (2017) and the most recent data as the pandemics effect lessen (2022) were chosen for the best possible representation of changes. While our project will attempt to analyze the changes in governmental housing assistance programs, this is important to note as it is a major influence in the rent increase the HUD assistance programs will need to cover.  


---------------------------------- 


##**Data Sources** 


Our data was sourced from the U.S. Department of Housing and Urban Development as it offers the most up to date information on fair market rents, section 8 & 202 housing vouchers, and guidelines for determining amount of assistance and qualification. 

Data was selected from 2017 and 2022 to get the best possible image of rent prices and voucher programs before the pandemic and with the most recent data since.

Additionally, this is the department that gathers information to advise changes in payout standards for the Housing Choice Voucher program. As a goverment run department, data from this source should be plentiful and contain minimal bias.  

  
------------------------------------ 

##**Questions We Hope to Answer with the Data** 

- What is considered a fair market price to the HUD? 

   - This will aid in establishing the baseline for HUD requirement for housing assistance voucher amounts, as it is their major contributing factor. 

- What areas have had the most increase in housing voucher assistance payouts and rent between years? 

  - This will establish areas where the strain on governmental assistance programs will be the highest. 

  - Machine learning model will be used to establish clusters based on increase. 

  - Information from these models will be used to draw conclusions about factors having most influence on increase. 


-----------------------------------

##**Machine Learning Model**

An unsupervised machine learning model(MLM) must be used as there is no target feature to test a supervised machine learning model against. The unsupervised MLM will utilize a joined dataset comprised of the fair market rent datasets from 2017 and 2022 as well as county data containing additional features used to determine housing voucher amount. This will allow calcuation of the rent increases pre- and postpandemic for 0 (studio) to 4 bedroom rentals, income limits, median income, wait times, and utility allowances. Additionally, a feature will be created to house the concatenated version of the state and county codes, used to join the two previously mentioned datasets. A final feature will be created through a function designed to assign the census region based on state code. The resulting dataset will be double-checked for any nulls or duplicated, and redundant columns will be dropped. The columns chosen to be dropped are as follows:

- County, Metro, State names were dropped as they have numerical counterparts that are representative of them.
- _id columns were dropped as they are unique identifiers for each data point in the system and thus do not add anything to the machine learning model.
- Entities were dropped as they are the identifier for the state & county codes concatenated to the area names, all of which is already represented in the dataset.
- Program labels were dropped as they are all labeled as "Housing Choice Voucher" as shown above, since there is only one value in this column it does not add anything to the final machine learning model.

After cleaning, these features will be put through the model to help decipher which features have the most weight in determining the rate of increase. K-means algorithm was chosen as it can handle and scale to large datasets. Since with K-means algorithms you are unaware of the number of clusters before starting the machine learning process, the KElbowVisualizer was used to identify the best possible number of datasets for this model. This graph shows the number of clusters vs inertia of the model and fitting time, measuring the amount of variation in the data set. The number of clusters will then be chosen where the graph depicts the best model fitting time and least loss. The data was scaled and PCA was used to reduce feature numbers. A new K-means model was fit with 4 clusters based on the elbow graph. 

![kelbow_visualizer](https://user-images.githubusercontent.com/100040705/183316793-49cee4aa-3d1c-46da-a5a3-f13f565ee443.png)


To explore pairwise feature correlation after the K-means algorithm was completed, the correlation method was used on the new clustered dataframe. Spearman's coefficient was chosen to depict the strength and direction of linear relationships between features and class. Class is the focus here as we are exploring if certain features cause a class to be assigned.
From the correlation method below, it can be concluded that there is a moderate negative correlation between the difference in the two fmr's is shown as well (around -0.17). This shows as the frm's difference increase the class number decreases. This could indicate lower fmr differences are assigned to a lower class number. As extremely low income limits and median imcomes differences increase, the class does as well, meaning those with the large increase were likely assigned to a higher class number, representing a large population of the dataset.
There are more data points assigned to class 2, this is consistent with our hypothesis, meaning a large population of the dataset showed high increases in rent, thus large increase in difference. Data points assigned to class 0 would therefore be of high concern for governmental assistant programs. Additionally, since this group occupies majority of the dataset 54.1%, there are many areas that may need adjustment to ease governmental strain.
There is also a weak correlation between the metro binary identifier and class(0.24), which may warrant further investigation as there has been an increase interest in metro vs non. In recent years, this feature has been found to have more influence than previously thought, and changes may have been put into action during the time difference studied.

![corr_results_unsup](https://user-images.githubusercontent.com/100040705/183316757-88e0759c-2e1b-4f68-8227-97ef6e8c1083.png)


The clustered dataframes 3D graph is shown below.Cluster 0 is the most distinct class, but was also the smallest. The proximity of other clusters may be of concern, especially with low correlation between many features of interest. Other methods of study may be needed to draw concrete conclusions.

![clusters_3d_1](https://user-images.githubusercontent.com/100040705/183316803-959c9902-19b9-4456-80ef-e8602d273bb5.png)
![clusters_3d_2](https://user-images.githubusercontent.com/100040705/183316806-d2ad408b-89b9-44d8-bd9e-2d60c57952fc.png)
![clusters_3d_3](https://user-images.githubusercontent.com/100040705/183316807-62d0f427-d4f5-49f7-92e9-ff8231aed6d7.png)


With the information gathered from the unsupervised machine learning model as well as additional resource, futher exploration of the metro vs non feature was done. To accomplish this, a deep neural network model was created in attempt to design a model that could predict if the data point was labeled as a metro or not. The data was prepaired in the same way, except differences were not taken, so data for all previously mentioned features for both years were supplied. **(change maybe, or justification)**

Again, the data was scaled. The data was then split into stratified training and testing group to ensure that both target populations (metro or non) would be balanced within the both the training and testing group. The training group would represent 70% of the population, and testing 30% to assure ample training data for the model while reserving some for testing that the model has never interacted with. Keras Tuner was used to determine the best possible hyperparameters for the neural network, as shown below.

![best_hypervalues_kera](https://user-images.githubusercontent.com/100040705/183318016-6e481fcf-888d-415a-81d9-ce61e808bd91.png)

The neural network model had high accuracy at 86% predictions being correct, but also had relatively high loss at 35%, as shown below:

![nn_results](https://user-images.githubusercontent.com/100040705/183318057-bb32f83b-1b92-4439-9ba9-b24b5bbaf968.png)


-----------------------------------

##**Final Dashboard**


A final dashboard will be made using a flask application and deployed with Heroku. This will contain multiple routes for information on processing of data, information on our MongoDB database, machine learning segment, and conclusions. We are working on building interactive maps with Pandas and GMaps, with a heatmap of feature increases. These will focus on fair market rate 2 bedrooms and wait times as they are the main deciding factor in housing assistance voucher amounts. The main page will include the purpose of our projects, links to other sections, and our contact information so it is ready for use in our portfolios. A first draft of the website is as follows:

![website_mockup1](https://user-images.githubusercontent.com/100040705/183319066-a916f6b9-9619-4f48-8915-8c078366691c.png)

![website_mockup](https://user-images.githubusercontent.com/100040705/183319071-443b4908-d42b-45ab-b4ce-3846b0f7d209.png)

-----------------------------------

##**Database**

The original datasets for this database can be found at the following links via the years tab (2017 and 2022) the Data tab:
Income limits:
https://www.huduser.gov/portal/datasets/il.html#2022_data
Fair Market Rates and Unadjusted Rents:
https://www.huduser.gov/portal/datasets/fmr.html

### Database Column Names:

#### 17_22_merged:
_id	State_Alpha_x	cbsasub_x	median2017	Metro_Area_Name_x	county_town_name_x	l50_2_x	ELI_2_x	l80_2_x	fmr0	fmr1	fmr2	fmr3	fmr4	State	County_Name_x	state_name_x	metro_x	State_Alpha_y	cbsasub_y	median2022	Metro_Area_Name_y	county_town_name_y	l50_2_y	ELI_2_y	l80_2_y	fmr_0	fmr_1	fmr_2	fmr_3	fmr_4	state	County_Name_y	state_name_y	metro_y

#### unadj_17_22:
stusps_x	fips2010	name	unadj_br0_x	unadj_br1_x	unadj_br2_x	unadj_br3_x	unadj_br4_x	stusps_y	areaname22	unadj_br0_y	unadj_br1_y	unadj_br2_y	unadj_br3_y	unadj_br4_y

### Database Explanation:

Six datasets were utilized to create this database. These datasets were cleaned and joined via excel and Pyton. The Python pandas library was also employed in this process. MongoDb compass was implemented to create both the database titled “17_22” and the collections titled “17_22_merged” and “unadj_17_22”. The Fair Market Rates datasets and the Income limits datasets were joined by year and via a common column: “fips2010”. This was performed to allow JSON files to not have an _id column conflict. Also, the Unadjusted Rents datasets were joined by year.
