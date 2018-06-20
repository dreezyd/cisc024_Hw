
# coding: utf-8

# # CIS024C - Summer 2018 - Mon/Tues/Wed/Thurs 3-5:50pm
# 
# ## Homework 1
# 
# Homework 1 covers some of the basics including setup and installation of Github and Anaconda/Jupyter for python development
# 
# You will need to download this notebook and use this as a starting point for your homework. You will just need to fill in the content of each code-block (cell) and execute. Once you have completed all the exercises, you will need to save and upload this to your github repository under a folder called hw1.
# 
# Note also the exercises build on top of one another so you might be able to do the next exercise if you have not completed the previous exercise.
# 
# Post any questions you have on our Slack at **cis-024c1.slack.com**

# ### 1. Install Anaconda/Jupyter Notebook on your computer
# 
# #### Steps
# 1. Go to https://www.anaconda.com/download and download the appropriate anaconda distribution for your Windows or Mac computer. Make sure to select the version of Anaconda corresponding to Python 3.6
# 2. Install the Anaconda distribution on your computer. 
# 3. Open the newly installed Anaconda application.
# 4. Launch Jupyter Notebook from the set of Anaconda applications.
# 5. You should see a page open in your browser. This is where you will enter your Python code.
# 
# Use the screen-shots here and the lecture slides to help with the installation.
# 
# * Environment Tools setup: https://drive.google.com/open?id=0B1lcsFkP-bjVUTFFeDZpUkRBVjg
# * Week 1 Lecture slides:  https://docs.google.com/presentation/d/1X2EUPSro2ljGJ76iMgXOZMGPwGH3xROiAs8jXf58Cyc/edit?usp=sharing
# 

# ### 2. Set up Github on your computer
# 
# Github is the tool that we will be using to upload assignment and project code. 
# 
# #### Steps
# 
# 1. Open your browser and navigate to https://github.com/
# 2. Sign up for a github account. You will need to pick a username, provide your email and a password.
# 3. Github will send you an email that you will need to click to verify your email address.
# 4. Once you have successfully logged in to Github, you will need to create a new repository for your cis024c class. You can call the repository cis024c if you like. This is a sample repository that we created in class on week 1 - https://github.com/dorairajsanjay1/cis024c
# 5. Once the repository is created you should be able to upload your assignments here using the "Upload files" button.
# 6. Make sure that you create each homework and project in a directory (or folder) and upload the folder so that the top level of repository is not cluttered.
# 
# Use the screen-shots here and the lecture slides to help with the installation.
# 
# * Environment Tools setup: https://drive.google.com/open?id=0B1lcsFkP-bjVUTFFeDZpUkRBVjg
# * Week 1 Lecture slides:  https://docs.google.com/presentation/d/1X2EUPSro2ljGJ76iMgXOZMGPwGH3xROiAs8jXf58Cyc/edit?usp=sharing
# 

# ### 3 Coding Exercises
# 
# In this section of the homework, you will be doing some simple coding exercise to familiarize yourself with your Python development environment - Jupyter. A development environment is also referred to as an IDE or Integrated Development Environment. 
# 
# Below are some useful commands to know when using Jupyter
# 
# 1. You can add a new cell by clicking on the "+" icon on top.
# 2. You can delete a cell by selecting that cell and clicking on the "scissors" icon on top.
# 3. You can execute a cell by either pressing shift+enter or selecting the "play" button on top.
# 4. You can create a new file in Jupyter via the File menu->New Notebook option. Make sure to select Python 2 when creating your notebook.
# 5. Also, for your code blocks make sure that Code is selected instead of another option like Markdown.
# 6. Use the Enter key to go to the next line in a cell to enter the next statement.
# 7. You can clear results by clicking on the Cell menu item and selecting Current Output->Clear or All Output->Clear depending on whether you are trying to just clear the output for one cell or for all cells.
# 8. In case your program has crashed for some reason (infinite loop, for example), you can restart your Python session by select Kernel in the menu and selecting Restart.
# 

# #### Sample Exercise 1
# 
# Create two variables x and y. Assign the value of 5 to x and 10 to y. Display the result for x and y

# In[2]:


x = 5
y = 10
print(x,y)


# #### Sample Exercise 2
# 
# Create two variables x and y. Assign an arbitrary value to them. Find the sum of x and y and assign to a new variable z. Display the result for z

# In[3]:


x = 10
y = 20
z = x + y
print(z)


# In[1]:


x = 5
y = 10
print(x,y)


# In[2]:


x =10
y = 20
z = x + y
print(z)

