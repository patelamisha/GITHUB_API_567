""" Author  :: Amisha Patel 
    Created :: 03/08/2021
    Assigment ::GIT Repositories & Commits """
import requests
import json
"""This function to interface with an external REST-based APIs."""
def UserRepos(userName):       
    userData = requests.get("https://api.github.com/users/" + userName + "/repos")
    repositories = json.loads(userData.text)
    userRepos = []    
    for repository in repositories:
        try:
            userRepos.append(repository.get("name"))
        except:
            userRepos = []        
    return userRepos
def UserCommit(userName, repoName):         
    repoData = requests.get("https://api.github.com/repos/" + userName + "/" + repoName + "/commits")
    commits = json.loads(repoData.text)
    NumberOfCommit = len(commits)
    return NumberOfCommit
"""This main function defines that lists of all the repositories and 
    all commits count given a specific github user name."""
def main():
    userName = input("Please Enter Your Github name: ")     
    userRepos = UserRepos(userName) 
    print("User Name: " + userName)
    for repository in userRepos:               
        NumberOfCommit = UserCommit(userName, repository)
        print("Repository: " + repository + " Number of Commits: " + str(NumberOfCommit))
if __name__ == "__main__":
    main()