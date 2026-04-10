"""
Q:: Azure Users
A:: Azure Users are individual accounts that can be assigned permissions and roles to access Azure resources. 
    - can have a role
    - can be part of a group


Q:: Azure Roles
A:: Azure Roles are sets of permissions that can be assigned to users, groups. 
    - built-in roles: pre-defined by Azure (e.g., Owner, Contributor, Reader)
    - custom roles: created by users to fit specific needs


Q:: Azure Security Groups
A:: Instead of:
        - give access to Alice
        - give access to Bob
        - give access to Kris
    You do:
        - create group: Dev Team
        - add Alice, Bob, Kris
        - assign permissions once


Q:: Azure Subscriptions
A:: Azure Subscriptions are the billing and access control units in Azure. They allow you 
    to manage resources, set budgets, and control access to resources. Each subscription 
    has a unique ID and can be associated with one or more Azure Active Directory tenants.


Q:: Azure Tenant
A:: ???
    

Q:: Azure Virtual Machines
A:: Azure Virtual Machines (VMs) are EC2-like compute resources in Azure.
    🟦 Azure
    - VNet is ALSO required.
    - but Azure creates it automatically if you don't.


Q:: Management Groups
A:: Management groups are containers that help you manage multiple Azure subscriptions. 
    They allow you to organize subscriptions into a hierarchy for better governance.


Q:: Azure Resource Groups
A:: Azure Resource Groups are logical containers that hold related Azure resources.


Q:: Virtual Network (VNet)
A:: A logically isolated, private network in Azure where you can securely deploy resources 
    like Virtual Machines. It provides full control over network configuration, including 
    IP address ranges, subnets, routing, and security rules. It isolates your resources 
    from other networks while allowing controlled communication.


Q:: Functions overview
A:: Use cases:: 
    - for small lightweighted apps
    - build in security
    - no physical or virtual server
    - super cheap, pay per calls

    - called by trigger (e.g., HTTP request, timer, event from Blob storage)
    - function app is executed
    - then for example processed file can be sent to blop stogage or database.


Q:: Azure Functions creation
A:: - Choose runtime (e.g., Python, Node.js, C#)
    - Choose hosting plan (e.g., Consumption Plan, Premium Plan)
    - Subscription and resource group.
    - Region
    - Networking, storage, monitoring options.
    

Q:: Azure Functions usage
A:: - Develop code locally (e.g. VS Code) or in Azure portal.
    - Specify environment variables
    - Develop a code in VS Code
    - deploy to Azure Functions using 
        - Azure CLI 
        - VS Code extension.
        - .zip file upload
        - github actions
        - Azure container registry (for Docker images).
    - Get function URL and test using HTTP client (e.g., Postman, CURL).


Q:: Trigger types for Azure Functions
A:: - HTTP trigger: function is called when an HTTP request is made to its endpoint.
        - Get function URL and test using HTTP client (e.g., Postman, CURL).
    - Timer trigger: function is called on a schedule (e.g., every hour).  
        -  
    - Blob trigger: function is called when a new file is uploaded to Azure Blob Storage.
        - 
    - Queue trigger: function is called when a new message is added to an Azure Storage Queue.
        - 


Q:: Azure App Service
A:: Azure App Service is a platform which offers auto scaling, load balancing, and built-in 
    monitoring for your applications. 
    - Scale up (bigger machine) or out (more instances).
    - CI/CD built-in Direct deploy from GitHub / Azure DevOps. 
    - GitHub actions
    - integrated with Azure services (e.g., Azure SQL Database, Azure Storage).
    

Q:: Azure App service creation
A:: - Choose runtime (e.g., .NET, Node.js, Python, Java)
    - Choose pricing plan 
    - Subscription and resource group.
    - Resources (CPU, memory)
    - Region
    - Configure deployment options (e.g., GitHub, Azure DevOps, local Git).    



"""