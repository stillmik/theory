"""
Q:: SSH
A:: SSH (Secure Shell) = a way to connect to another computer over a network securely. 
    It’s most commonly used by developers and system administrators to log into remote 
    servers and manage them safely. SSH solves 2 big problems: everything you send 
    is encrypted and authentication (you prove who you are). to get access you need:
    - username
    - .pem
    - public ip of machine
    Private key (.pem file) is stored on my side and used toget access to server.
    1) chmod 400 my-key.pem
    2) ssh -i my_key_path.pem username@ip.ip.ip.ip


Q:: What are Branches, commits, merge, rebase, Pull Requests, Code Review, Forks
A:: - Branches - Parallel versions of your code.
    - Commits - Snapshots of your code over time.
    - Pull request - please merge my branch into another branch.
    - Forks - your own copy of someone else’s repo.

    
Q:: GitHub Actions, CI\CD
A::    


Q:: main, master
A:: - There is no technical difference between main and master.
    - Historically git used master as default branch name. Around 2020 industry shifted 
        to more neutral naming GitHub made main the default. 


Q:: Pull request
A:: 1) Make sure dev is clean
    2) Open a pull request
    3) Then code review happens. People must: request fixes or approve.
    4) CI/CD tests must be passed


Q:: GitHub Actions
A:: ???    
"""