# Final Project Progress Report
## 1. Project info
• Team Name Runaway  
• Team Members (first and last name, email)  
  Agens XU jingzhi@uchicago.edu  
  Anny Liu hanyunl@uchicago.edu  
  Huanrui CHEN hchen0628@uchicago.edu  
  Tianle YE tye1@uchicago.edu  
• GitHub Repository Link 
[https://github.com/macs30122-winter24/final-project-runaway](https://github.com/macs30122-winter24/final-project-runaway)

## 2. Project Description
The 2019-2020 Hong Kong Anti-Extradition Bill Movement was a series of massive demonstrations against the introduction of a bill to extradite Fugitive Offenders Ordinance and the intervention of the China Communist Party (CCP) into Hong Kong domestic political system. The movement caught global attention but ended bitterly in 2020 with the CCP’s promulgation of the Hong Kong National Security Law on 30 June 2020. The law claimed to safeguard national security within the Hong Kong Special Administrative Region and deal with acts of secession, subversion of state power, terrorist activities, and collusion with foreign or offshore forces that endanger national security. Based on this law, the Hong Kong government prosecuted a large number of dissidents and political activists who were previously engaged in the movement. In 2021, the CCP restructured the Hong Kong electoral system with the introduction of the National People's Congress Standing Committee’s amendments to Hong Kong Basic Law, significantly undercutting prospects of universal suffrage in Hong Kong’s future elections. With the new amendments, only 88 out of the 470 seats in the Hong Kong Legislative Council are directly voted by Hong Kong citizens, with the rest controlled by the CCP to varying degrees. The turnout rate of the latest 2023 Hong Kong local elections dropped by 44% compared with the 2019 election, plummeting to a historical low of 27%. It could be expected that the public sphere in Hong Kong has been dramatically transformed after the Anti-Extradition Bill Movement.

How might public opinion in Hong Kong have been changed after the authoritarian crackdown by the CCP? Studies on the effect of the states’ repression on dissents is an inconclusive field (e.g., Lichbach, 1987; Opp and Roehl, 1990). Recent research in this field still shows mixed results. While some studies find that repression could radicalize backlash (e.g., Sullivan and Davenport, 2017), other research shows a deterrence effect to the challenges against the state authority (e.g., Deibert, 2015; Pan and Siegel, 2020). Some scholars classify the repressions’ effect on dissents based on regime types. For example, Gupta, Singh, and Sprague (1993) argue that while in democratic nations state repression would provoke a higher level of demonstrations, it might significantly reduce political oppositions in nondemocratic societies. However, as a society with democratic institutions but living under the shadow of authoritarian control, Hong Kong fits neither the category of a fully democratic nor nondemocratic society neatly. The hybrid political system in Hong Kong makes it more complex to disentangle the state crackdown’s effect on its public sphere.

Moreover, the political attitudes in authoritarian-controlled societies differ publicly and privately. Kuran (1997) claims that citizens’ private preferences and public preferences toward a regime might differ dramatically. It could then be asked if in the case of Hong Kong, there is a gap between citizens’ publicly claimed political opinion gathered through survey and more privately communicated political preferences on social media. If so, what might this gap look like? We ask this question based on the fact that although the political system in Hong Kong has been altered, the Chinese government has not mandated the same internet Great Wall and censorship systems in Hong Kong, allowing space for relatively free political discussion. We hypothesize that the political preferences collected from social media might show more dissents than survey data in Hong Kong after the CCP’s crackdown.

The specific research questions we answer in this project are: What is the impact of CCP’s authoritarian crackdown on public opinion in Hong Kong society? Specifically, how does public opinion, particularly the attitude towards the Hong Kong government, differ before and after the CCP’s authoritarian crackdown? How does the political opinion after the crackdown differ between preferences gathered by surveys and preferences shown on social media? To do so, we collect public opinion data from a Hong Kong political platform and survey data from the Hong Kong Public Opinion Research Institute and analyze their differences using methods including sentimental analysis. We hypothesize that 1) the attitude towards the Hong Kong government turns more negative after the crackdown, and 2) the social media discussion shows more negative sentiments then in survey data.

Our studies offer two advantages over the existing literature. First, the Hong Kong case could show how the foreign authoritarian rule impacts public opinion in a free and democratic society. The Anti-Extradition Bill Movement is a transiting point in Hong Kong history, marking the CCP’s hijack of its electoral and legal system. This special case may uncover more nuances in the study of the state repressions’ effect on public opinion. Second, our studies utilize social media posts and sentimental analysis to study public opinion. Few current studies use large-scale social media posts to study offline crackdown’s impact on online public opinion, with Pan and Siegel in 2020 claim that they are the first scholars to do so. Moreover, in the case of Hong Kong where censorship at large allows for free political discussion, the social media posts might better capture the average citizens’ political opinion. Our comparison between social media data and survey data could further more comprehensively represent the political orientations of Hong Kong citizens after the crackdown.

## 3. Data Sources
We create a [Keyword table](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Keywords.md?raw=true) based on previous research on Hong Kong's digital political vocabulary, it is categorised into: Democracy and Justice, Protest and Resistance, Government and Governance. Our discussion primarily focuses on two aspects: firstly, the shift in Hong Kong residents' attitudes towards the Hong Kong government, and secondly, the differences between social media and survey data. Therefore, our data sources need to be relevant to political discussions and involve both social media and survey data sources. Consequently, we chose LIHKG, the largest political discussion forum in Hong Kong, as our data crawling target, and obtained historical public opinion survey data from the database of the Hong Kong Public Opinion Research Institute, the largest opinion survey center in Hong Kong.

### Data source #2 PORI survey data
The Hong Kong Public Opinion Research Institute (PORI), formerly known as the Public Opinion Programme at the University of Hong Kong, is a non-profit organization in Hong Kong specializing in public opinion surveys and research, established in 1991. The institute primarily utilizes telephone interviews, online surveys, and face-to-face interviews as its main data collection methods, focusing on gathering views and attitudes of the Hong Kong public on various domains such as society, politics, and the economy. The institute promotes open data and technology sharing, as well as freedom of thought, knowledge, and information, allowing us to use the data without violating ethical and copyright rules at no cost.
(See Data folder in PORIHK-survey folder in the Github repository for complete data; Due to the large number, not all data files were uploaded, only one sample from each survey was uploaded)

• Data type: Downloading

• Time frame: 2017.1 - 2024.1

• Data size so far: 
We have surveys categorized by themes, such as Freedom Indicators and Social Indicators, with each survey encompassing several subtopics. For instance, Freedom Indicators include a total of 9 subtopics, such as Appraisal of Freedom of Speech. To match the 19 keywords we chose, we selected 19 surveys in the following 8 themes: Social Conditions Evaluation, Social Policy Evaluation, Freedom Indicators, Rule of Law Indicators, Chief Executive Popularity, Government Popularity, Public Sentiment Index, and Trust and Confidence Index. Each surveys containing public opinion results on specific topics from Hong Kong citizens from 1993 to 2024. The original data volume is around 100,000. We conducted data cleaning and integration based on the time frame, reducing the data volume to under 30,000.

## 4. Data cleaning/wrangling 

### Data source #2 PORI survey data
(See testLCJ, test2017.ipynb, and testtrust_democracy.ipynb in the PORIHK-survey folder for data cleaning code)

For these surveys, since the survey dataset itself is relatively clean, only scores exceeding the range (scores greater than 100) and some invalid options (including some negative scores representing "refuse to answer") have been excluded, and the data types of some columns have been adjusted to facilitate statistics and graphing. In addition to this, for the CE-scored survey dataset, the data is currently integrated by month (rather than day) for the time being, to make the data further available for subsequent analysis and presentation, we translated the Cantonese data into English versions and created numeric indicators and baselines.


## 5. Data analysis and visualization

### Data source #2 PORI survey data
We also used the keywords from the political vocabulary list utilized in the crawler as filtering criteria to select related questionnaire content, enabling us to compare the results of the public opinion survey with the outcomes of the internet discussions crawled. In the following example, we present the visualization of data about the Chief Executive of Hong Kong, trust in the government, and evaluation of the Hong Kong government's development of democracy, which corresponds to "Chief Executive" and "Government" in the keywords of the topic "Government and Governance" and "Democracy" of the topic "Democracy and Justice"

Examples:
• Rating of Chief Executive John Lee

![Rating of Chief Executive John Lee by month](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Image/Rating%20of%20Chief%20Executive%20John%20Lee%20by%20month.png?raw=true)


• Satisfaction level of the development of democracy by the Hong Kong Government

![Democracy](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Image/Democracy.png?raw=true)


•Level of trust in the Hong Kong Government

![Trust](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Image/Gov_trust.png?raw=true)


## 6. Responsibilities
Data collection: 
Agens XU Anny Liu

Data cleaning/wrangling: 
Agens XU

Data analysis: 
Anny Liu

Data visualization: 
Anny Liu

Presentation script: 
Huanrui CHEN Tianle YE

Short video: 
Tianle YE Agens XU

Final report: 
Huanrui CHEN Tianle YE

README: 
Huanrui CHEN

## 7. Workplan (optional)
Before February 10th (Completed Work): 
Completed the literature review, designed the crawler program, and successfully crawled sample data from the forum. Confirmed the data cleaning workflow for the public opinion survey.

February 17th: 
Complete the crawling of forum data, finish the analysis and visualization of the public opinion survey data, write the presentation script, and start the production of the project report and video.

February 24th: 
Complete the analysis and visualization of all crawled data, compare the crawled data with the public opinion survey data, rehearse the presentation, and continue the production of the project report and video.

March 3rd: 
Complete the final project report and video.

## Bibliography

Deibert, R. (2015). Authoritarianism Goes Global: Cyberspace Under Siege. Journal of Democracy, 26(3), 64–78. https://doi.org/10.1353/jod.2015.0051

Gupta, D. K., Singh, H., & Sprague, T. (1993). Government Coercion of Dissidents: Deterrence or Provocation? Journal of Conflict Resolution, 37(2), 301–339. https://doi.org/10.1177/0022002793037002004

Kuran, T. (1997). Private truths, public lies: The social consequences of preference falsification (sec. print). Harvard Univ. Press.

Lichbach, M. I. (1987). Deterrence or Escalation?: The Puzzle of Aggregate Studies of Repression and Dissent. Journal of Conflict Resolution, 31(2), 266–297. https://doi.org/10.1177/0022002787031002003

Opp, K.-D., & Roehl, W. (1990). Repression, Micromobilization, and Political Protest. Social Forces, 69(2), 521. https://doi.org/10.2307/2579672

Pan, J., & Siegel, A. A. (2020). How Saudi Crackdowns Fail to Silence Online Dissent. American Political Science Review, 114(1), 109–125. https://doi.org/10.1017/S0003055419000650

Sullivan, C. M., & Davenport, C. (2017). THE REBEL ALLIANCE STRIKES BACK: UNDERSTANDING THE POLITICS OF BACKLASH MOBILIZATION*. Mobilization: An International Quarterly, 22(1), 39–56. https://doi.org/10.17813/1086-671X-22-1-39
