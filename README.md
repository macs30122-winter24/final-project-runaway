### Project Description (600 words)
Our research project concerns the change in public opinion in Hong Kong society after the Chinese Communist Party’s crackdown on the Anti-Extradition Bill Movement in Hong Kong. Our research question is: How does public opinion towards Hong Kong society and the government differ before and after the Anti-Extradition Bill Movement? How does such public opinion gathered in survey and on online social media forums differ? We hypothesize that there is a gap between citizens’ publicly claimed political opinion gathered through survey and more privately communicated political preferences on social media platforms. This research question is deeply relevant to social science. It explores how authoritarian crackdowns could impact public opinion in a democratic local society and the difference in different public opinion sources. 

To carry out our project, we employ two data sources: LIHKG, a Cantonese political platform in Hong Kong, and the public opinion survey data from Hong Kong Public Opinion Research Institute. To scrap the web data, we prepared a keyword list segmented into three topics (democracy and justice, protest and resistance, and government and governance) and entered each keyword to the inbuilt search engine in the website. Next, we used Selenium to manually scan through and store all relevant post links for a single keyword. Then we went into each post link and scraped the messages on the first page with their content, posted time, and the amount of for and against. In the data wrangling process, we use Pandas to structure the scraped data into CSV format including each message’ poster ID, the content, and time. To segment Cantonese words, we use a tool called Pycantonese to split the content of a message into meaningful individual words or phrases for later processing. We further utilize Microsoft Translator API for automatic translation from Cantonese to English when it is needed.

To process the survey data, we download keyword-relevant csv files from the website and translate them into relevant line graphs. Each graph shows the Hong Kong public’s opinion towards a specific issue or an item in a given period of time. For the web data, we first did the exploratory data analysis by getting top tokens over the years and their frequency trend to see the changes of the popular topics. Next, we used the TensorFlow framework to fine-tune a pre-trained BERT model for sentiment analysis. Since our data consisted of Chinese and forum-like texts, we utilized a dataset of 10k posts from Weibo (the largest social media platform in mainland China) labeled with a total of six emotions to help us identify sentimental expressions in Chinese texts. In addition, we treated the collection of all posts per month under each keyword as a unit document and performed a dynamic topic modeling using the LDA model. We then compared the most relevant keywords provided by the model with our manually segmented keywords.

From the survey data, we find that Hong Kong citizens’ attitudes towards the Hong Kong government and assessment of Hong Kong society turned negative during the Anti-Extradition movement and turned positive after to a similar level as before the movement. In contrast, from the web data, we find that Hong Kong citizens’ attitudes towards the local government and society worsened considerably during the movement, and the negative sentiments such as anger could still be identified in the discussion of Hong Kong government and society after the movement. This trend is reflected both in the graphs of word frequency counts and sentimental analysis. In general, we confirm our hypothesis that the public opinion gathered from survey data and online social media platforms could have a considerable gap.

### Other information
GitHub repo navigation: ?

Data sources: LIHKG: https://lihkg.com/category/1; Hong Kong Public Opinion Research Institute: https://www.pori.hk

Required libraries with version numbers: ?

Task distribution:
- Data collection: Agens Xu, Huanrui Chen, Anny Liu
- Data cleaning/wrangling: Agens Xu, Huanrui Chen
- Data analysis: everybody
- Data visualization: Anny Liu, Tianle Ye
- Presentation script: everybody
- Short video: everybody
- README: Tianle Ye

Original presentation: https://github.com/macs30122-winter24/final-project-runaway/blob/main/Team%20Runaway%20Final%20Presentation_Original.pptx

Revised presentation: https://github.com/macs30122-winter24/final-project-runaway/blob/main/Team%20Runaway%20Final%20Presentation_Revised.pptx

Video link: ?
