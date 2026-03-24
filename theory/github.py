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




"""