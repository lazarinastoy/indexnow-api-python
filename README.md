# indexnow-api-python
Submit your URLs from a JSON file export from Oncrawl OR log files (or any json list) to IndexNow API


Here is a sample of how your input should look like link by line: 

YOU WILL BE ASKED TO: 

Enter the directory where your Oncrawl file was downloaded in the format: /Users/lazarinastoy/Downloads/directory1/  

EXAMPLE INPUT: 

/Users/lazarinastoy/Downloads/notindexedtest/ ----> THIS IS THE DIRECTORY WHERE YOUR JSON FILE WITH ALL URLS YOU WANT TO SUBMIT IS 

YOU WILL BE ASKED TO:

Enterfile name of Oncrawl download in format 'blah.json' :

EXAMPLE INPUT:

notindexed.jsonl ---> THIS IS THE NAME OF THE FILE WITH URLS YOU WANT TO SUBMIT (DOESN'T MATTER HOW BIG IT IS, WE HAVE A FUNCTION TO SPLIT IT). IMPORTANT: ENSURE THAT THE FILE IS CONTAINED IN THE FOLDER ABOVE

YOU WILL BE ASKED TO:

Enter a subfolder of your directory where you want the json files stored in the format: /Users/lazarinastoy/Downloads/directory1/directory2/

EXAMPLE INPUT:

/Users/lazarinastoy/Downloads/notindexedtest/indexnowtest/ ---> THE FOLDER WHERE YOU WANT TO STORE THE JSON FILES TO SUBMIT - REMEMBER INDEXNOW HAS A LIMIT OF 10K URLS PER SUBMISSION, SO IF YOU HAVE A BIGGER FILE, EXPORTED FROM ONCRAWL (OR YOUR LOGFILES), YOU WILL NEED TO SPLIT IT INTO SMALLER JSON FILES. REST ASSURED, THIS IS ALREADY INCORPORATED IN THE FUNCTION

YOU WILL BE ASKED TO:

enter your indexnow api key:

EXAMPLE INPUT:

c989X5X2cF7f405c95a458de3324XXXX ---> YOUR INDEX NOW API KEY


Then, the magic will happen ✨ 

You will need a 200 response code in the console, as many times as your files with 10K urls each are. 

Check out more here: https://lazarinastoy.com/the-ultimate-guide-to-microsoft-indexnow-api-indexation-protocol-for-search-engines-with-python-code-examples/ 

Thank you ❤️
