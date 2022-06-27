import json
import requests
import os

try:
  directoryofdownload=input("Enter the directory where your Oncrawl file was downloaded in the format: /Users/lazarinastoy/Downloads/directory1/ \n")
  oncrawlfilename=input("Enterfile name of Oncrawl download in format 'blah.json' :\n")
  folder_in_directory_of_download_for_json_files = input("Enter a subfolder of your directory where you want the json files stored in the format: /Users/lazarinastoy/Downloads/directory1/directory2/ \n")
  indexnowkey= input("enter your indexnow api key:\n")

  #upload export from Oncrawl
  not_indexed_fulllist = open(os.path.join(directoryofdownload, oncrawlfilename))

  #you need to add you path here
  with open(os.path.join(directoryofdownload, oncrawlfilename), 'r',
            encoding='utf-8') as f1:
      ll = [json.loads(line.strip()) for line in f1.readlines()]

      #this is the total length size of the json file
      print(len(ll))

      #in here 10000 means we getting splits of 10000 rows of URLs
      #you can define your own size of split according to your need
      size_of_the_split=10000
      total = len(ll) // size_of_the_split

      #in here you will get the Number of splits
      print(total+1)

      for i in range(total+1):
          json.dump(ll[i * size_of_the_split:(i + 1) * size_of_the_split], open(
              folder_in_directory_of_download_for_json_files + str(i+1) + ".json", 'w',
              encoding='utf8'), ensure_ascii=False, indent=True)

  #enter your key
  ext = ('.json')
  #reference your no_indexed_list, preferably in JSON format
  for files in os.scandir(folder_in_directory_of_download_for_json_files):
        if files.path.endswith(ext):
          with open(files) as f:
            not_indexed_list = json.loads(f.read())
            #submit to indexnow    
            data = {
              "host": "www.bing.com",
              "key": indexnowkey,
              "urlList": not_indexed_list
              }
            headers = {"Content-type":"application/json", "charset":"utf-8"}
            r = requests.post("https://bing.com/", data=data, headers=headers)
            print(r.status_code)
except EOFError:
    print("The Script won't work unless you provide the values as specified")
  
