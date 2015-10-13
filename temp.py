def join(seperator = "-",*str):
    return seperator.join(str);


a = ["sddsd","111","dada"]
print join("/",*a)

import pickle
test = {"one":1,"two":2}
with open("1.txt","w") as file:
    pickle.dump(test,file)
   # print pickle.load(file)
str = ""
str = "'nj cnhjrf/htgd/fsf"
str = str.replace('/','//###')
print str
