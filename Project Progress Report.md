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

### Data source #2 PORI survey data
(See Data folder in PORIHK-survey folder for data examples; Due to the large number, not all data files were uploaded, only one sample from each survey was uploaded)

• Data type: Downloading

• Time frame: 2017.3 - 2024.1

• Data size so far: about 100 surveys

• Additional information: so far we have collected surveys on two subjects (the 2017 CE election rolling survey and the Rating of Chief Executives). Information from this data source will be used to capture citizens' public political preferences (including satisfaction of  leaders and opinions on elections). 


## 4. Data cleaning/wrangling 

### Data source #2 PORI survey data
(See testLCJ and test2017.ipynb in the PORIHK-survey folder for data cleaning code)

For both surveys, since the survey dataset itself is relatively clean, only scores exceeding the range (scores greater than 100) and some invalid options (including some negative scores representing "refuse to answer") have been excluded. In addition to this, for the CE-scored survey dataset, the data is currently integrated by month (rather than day) for the time being. Since the dates in the (first data source) forum are only recorded up to the year, further consolidation of this data may be carried out at a later stage according to the needs of specific analyses.


## 5. Data analysis and visualization

### Data source #2 PORI survey data
As the collection of all data from the first source has not yet been completed, only descriptive statistics are currently available.

Examples:

• Rating of Chief Executive John Lee (by month, gender, and age group)

![Rating of Chief Executive John Lee by month](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Image/Rating%20of%20Chief%20Executive%20John%20Lee%20by%20month.png?raw=true)

![Rating of Chief Executive John Lee by gender](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Image/Rating%20of%20Chief%20Executive%20John%20Lee%20by%20gender.png?raw=true)

![Rating of Chief Executive John Lee by age](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Image/Rating%20of%20Chief%20Executive%20John%20Lee%20by%20age.png?raw=true)

• 2017 CE election vote plot (by time, total vote count, and distribution)

![2017 vote by time](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Image/2017%20vote%20total%20count.png?raw=true)

![2017 vote total count](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Image/2017%20vote%20plot.png?raw=true)

![2017 vote distribution](https://github.com/macs30122-winter24/final-project-runaway/blob/main/Image/2017%20vote%20distribution.png?raw=true)

## 6. Responsibilities
Data collection Agens XU Anny Liu

Data cleaning/wrangling Agens XU

Data analysis Anny Liu

Data visualization Anny Liu

presentation script Huanrui CHEN Tianle YE

short video Tianle YE Agens XU

final report Huanrui CHEN Tianle YE

README Huanrui CHEN

## 7. Workplan (optional)
If useful for the group, create a plan with a list of tasks and a timeline that specifies when each task should be completed between now and the in-class presentations and final submission.

This current report will serve as the basis for the final report, which will be an updated version of this report (e.g., it will include the last version/updated version of the same info you reported here + a summary of the project’s takeaways). This and the final report lengths do not matter as long as all required information is included (typically groups write a few pages).

Bibliography

Deibert, R. (2015). Authoritarianism Goes Global: Cyberspace Under Siege. Journal of Democracy, 26(3), 64–78. https://doi.org/10.1353/jod.2015.0051

Gupta, D. K., Singh, H., & Sprague, T. (1993). Government Coercion of Dissidents: Deterrence or Provocation? Journal of Conflict Resolution, 37(2), 301–339. https://doi.org/10.1177/0022002793037002004

Kuran, T. (1997). Private truths, public lies: The social consequences of preference falsification (sec. print). Harvard Univ. Press.

Lichbach, M. I. (1987). Deterrence or Escalation?: The Puzzle of Aggregate Studies of Repression and Dissent. Journal of Conflict Resolution, 31(2), 266–297. https://doi.org/10.1177/0022002787031002003

Opp, K.-D., & Roehl, W. (1990). Repression, Micromobilization, and Political Protest. Social Forces, 69(2), 521. https://doi.org/10.2307/2579672

Pan, J., & Siegel, A. A. (2020). How Saudi Crackdowns Fail to Silence Online Dissent. American Political Science Review, 114(1), 109–125. https://doi.org/10.1017/S0003055419000650

Sullivan, C. M., & Davenport, C. (2017). THE REBEL ALLIANCE STRIKES BACK: UNDERSTANDING THE POLITICS OF BACKLASH MOBILIZATION*. Mobilization: An International Quarterly, 22(1), 39–56. https://doi.org/10.17813/1086-671X-22-1-39
