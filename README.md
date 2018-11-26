## Getting the project to work you need to follow few steps:

###### NOTE: Get PyCharm (Download it!)

1. Before you edit the code. Please update your libraries every time.

    ```pip install -r requirements.txt```

2. If you have installed any new libraries then update the requirements.txt before you push the code.

    ```pip freeze >> requirements.txt```

__________________________________________________________________

### Steps:
1. Create "**New Project**" in PyCharm. Make sure you have Virtual Environment setup properly.
2. Once project starts, to the bottom left corner press "**Terminal**" and execute the following commands:

    ```git init```\
    ```git remote -v```
    
    If you don't see the url with *https://github.com/bivav/MongoProject.git* \
    then do the following:\
    ```git remote add origin https://github.com/bivav/MongoProject.git```\
    If you are getting error saying already initialized url then use this \
    ```git remote set-url origin https://github.com/bivav/MongoProject.git```
3. Once the url is set now we can pull the code.
4. Use the following command to pull the code from git.

    ```git pull origin master```
    
    ***NOTE: Put the username as bivav and for password (ask me)***
    
5. Once the code is fetched, sometimes you might need to restart PyCharm or refresh it.


### STEPS TO PUSH THE CODE:
1. Once you have edited the code, you can add or update the code to github.\
    ***NOTE: Please ask me and show me before you push***
    
    ```git add (filename1, filename2, etc etc.....)```
    
2. Then commit your changes:

    ```git commit -m "(updates done by you)"```
 
3. Then add the git url or set-url
    
    ```git remote add origin https://github.com/bivav/MongoProject.git```

4. Then push your code:

    ```git push -u origin master```
    
    