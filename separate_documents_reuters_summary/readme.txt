1) Create a folder name "separate_dict_documents" inside the folder having prefetch.py code 
2) First run the prefetch.py file which will generate the separate 10788 json files inside  separate_dict_documents folder. It is one time effort.

3) After that on every request main.py call get_summary in which 10788 json file will load as dict for each word to calculate word_frequency dict after it will calculate tf-idf which will be used for sentences score calculation.

4) Time consuming process not suitable for real time summarisation
