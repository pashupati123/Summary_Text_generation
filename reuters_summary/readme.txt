1) First run the prefetch.py file which will generate the retures_idf_dict.json file inside same folder. It is one time effort.

2) After that on every request main.py call get_summary in which retures_idf_dict.json file will load as dict as word_idf which will be used for sentences score calculation in real time.
