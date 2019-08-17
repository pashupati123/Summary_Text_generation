import os
import summary as sum
#import same_doc_tf_idf_summary as sum
#import retuers_corpus_tf_idf_summary as sum
article_text=""
with open("in.txt", "r") as lines:
    for line in lines:
        article_text=article_text+line

summary_text=sum.get_summary(article_text)
f = open("out.txt", "w") 
f.write(summary_text)
f.close()


