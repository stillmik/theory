"""
Q:: What is IAM?
A:: An instrument in AWS which manages acess to resources.


Q:: User types, roles, groups
A:: Root user
        - This is created when you first sign up for AWS. Full access to EVERYTHING. 
            No restrictions unless you manually add them. Best practice: Use it only for 
            critical stuff. 
    IAM user
        - These are the “normal” users you create. Represent real people or services. 
            Have username/password (console), access keys (API/CLI).
    Roles
        - An IAM role is an IAM identity that you can create in your account that has specific 
            permissions. Instead of being uniquely associated with one person, a role is intended 
            to be assumable by anyone who needs it. You can use roles to delegate access to users, 
            applications, or services that don't normally have access to your AWS resources. 
    Groups
        - You create IAM groups to manage access permissions for multiple users with similar roles 
            or responsibilities. By attaching policies to these groups, you can grant or revoke 
            permissions for entire sets of users.


Q:: Connection to AWS
A:: A user can connect o AWS and manage it viaconsole, to do that you have to set up credentials.


Q:: VPC
A:: Virtual private network is a logically isolated, private network within the AWS cloud where 
    you can securely launch resources like EC2 instances. It offers full control over network 
    configuration, including IP address ranges, subnets. Isolates your resources from other networks.


Q:: Public/private nets
A:: A subnet is a range of IP addresses in your VPC. You can create AWS resources, such as 
    EC2 instances, in specific subnets. 
    Public subnet – The subnet has a direct route to an internet gateway. Resources in a public 
    subnet can access the public internet.
    Private subnet – The subnet does not have a direct route to an internet gateway. Resources 
    in a private subnet require a NAT device to access the public internet.


Q:: Lambda
A:: Lambda is a serverless AWS tool which spinns up when you call the code and shuts down when idle.
    Usually is used for simple lightweighted tasls like auth, file processing, small ML models.
    - workload is event-based
    - execution is short (<15 min)

    
Q:: How to use lambda
A:: - Load libs + code file (all are in same package level). 
    - Pack them in .zip
    - AWS will handle it automaticly
    We can test it in AWS
    - Then we have to create REST API to acess it. Use API gateways -> REST API -> method (attach Lambda).
    - Copy URL and use CURL to test.



Q:: Elastic beanstalk
A:: Elastic Beanstalk = “just deploy your app, we’ll handle the infrastructure mess.”
    It handles:
        - EC2 instances
        - load balancer
        - auto scaling
        - deployment
        - monitoring
    Beanstalk secretly creates:
        - EC2 (your servers)
        - Auto Scaling Group
        - Load Balancer (ELB)
        - Security groups
        - CloudWatch monitoring
    Great for:
        - MVPs
        - internal tools
        - startups moving fast
    * Upload your code via .zip
    * configure permissions to let it interract with other AWS services
    * place it in VPC
    * configure memory, architecture, instance type, 
    * configure monitoring, alarms


Q:: S3
A:: - Something similar to google drive, but organized askey-value general object storage. 
    - Stores big files, small files, text, media, code, spreadsheets, database backups, etc.
    - Scalable, durable, available, integrated with AWS tools.

    
Q:: S3 Bucket
A:: A storage for objects, posess unique name.
    - Max 5 TB
    - By default private
    - Encryption forward-backward
    

Q:: Storage classes
A:: - size, get, post
    - Lifecycle rules automate data movement to different tiers
    - Examples: Standart, Intelligent, Infrequent, Glazier

    
Q:: How to retrieve objects from S3 / in prod?
A:: - Retrieve object by URL: http/amazon/BUCKET_NAME/OBJECT_NAME (for public) or we can
        by code s3Client.get_object(BUCKET_NAME, OBJECT_NAME)
    In prod::
    1) Load video to s3
    2) Get s3 link and tourn it into normal via CloudFront
    3) Save to users DB
    4) Retrieve from users DB
    5) to CloudFront
    6) Fetch video.png



Q:: S3 Objects
A:: big files, small files, text, media, code, spreadsheets, database backups, etc.
"""