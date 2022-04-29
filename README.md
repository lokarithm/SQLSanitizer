# SQLSanitizer

## A simple tool to convert SQL keywords into upper case.

### **Version** 0.1

### **Requirement**
python version 3.0+

### **Use Case**

e.g. When you have a script file like this and you want to convert all the SQL keywords(*select*, *from*, *group by*, etc.) into uppercase:

> select count(1) as myCount  
    from TableA ta  
    group by ta.someColumn  
    having count(myId) > 5

**Output:**

> SELECT COUNT(1) AS myCount  
    FROM TableA ta  
    GROUP BY ta.someColumn  
    HAVING COUNT(myId) > 5  

### **How To Use**
To convert the keywords to uppercases, download the SQLSanitizer.py script and keywords.csv. Then run the following command:

> python SQLSanitizer.py -i \<input filename\> -o \<output filename\>

- The **-o** flag and **output filename** is *optional*. By default, the output filename is *output.sql* if it is not speficied.

e.g. if you run:
> python SQLSanitizer.py -i sampleScript.sql

The output file will be created under the same directory as *output.sql*.

If output.sql already exist, the script will create a different file *output2.sql*. In theory, this script can be run multiple times without overwriting any existing file.

### **To Support Me**
You can [buy me a coffee](https://www.buymeacoffee.com/lokc)☕. 😊
