"""
EntraId identifies not only users but applications. ENtraID assigns roles.


Q:: Azure Users
A:: Azure Users are individual accounts that can be assigned permissions and roles to access Azure resources. 
    - can have a role
    - can be part of a group


Q:: Azure Roles
A:: Azure Roles are sets of permissions that can be assigned to users, groups. 
    - built-in roles: pre-defined by Azure (e.g., Owner, Contributor, Reader)
    - custom roles: created by users to fit specific needs
    Owner - creator of subscription, creates subscriptions, within subscription ypou are always an owner
    Contributor - assigned by owner czel
    Reader - popusk


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
A:: Tenant - like organization. Subs belong to subscriptions.
    

Q:: Azure Virtual Machines
A:: Azure Virtual Machines (VMs) are EC2-like compute resources in Azure.
    🟦 Azure
    - VNet is ALSO required.
    - but Azure creates it automatically if you don't.


Q:: Management Groups
A:: Management groups are containers that help you manage multiple Azure subscriptions. 
    They allow you to organize subscriptions into a hierarchy for better governance.


Q:: Azure Resourse Groups
A:: Azure Resourse Groups are logical containers that hold related Azure resources.


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


Q:: Deployment Slots
A:: Deployment slot is basically a separate live environment for the same app.
    - You can have multiple slots (e.g., staging, production).
    - Each slot receives its code from it's own GitHub branch.
    - Each slot has its own URL and configuration.
    - You can deploy to a staging slot, test it, and then swap it with production without downtime.


Q:: Azure App Service scaling
A:: - Scale up: increase the resources (CPU, memory) of the existing instance.
    - Scale out: increase the number of instances running your app.
    - Auto-scaling: automatically scale based on predefined rules (e.g., CPU usage, request count).
    - Manual scaling: you can manually adjust the number of instances or resources as needed.


Q:: Storage Accounts
A:: - Storage accounts are wrappers for Azure Storage services, for example Blob Storage, 
        File Storage, Queue Storage, Table Storage.
    - Linked to resource group.
    Storage Account
    ├── Blob Containers
    │     ├── files
    │     ├── images
    │
    ├── File Shares
    ├── Queues
    ├── Tables    
    - Inside Azure Storage Account you have:
        👉 Blob Storage (the whole system)
        👉 Containers (folders inside it)
        👉 Blobs (actual files)


Q:: Azure Container
A:: 📁 Container
    👉 a logical grouping inside Blob Storage
    - like a folder/bucket
    - holds blobs (files)


Q:: Azure RAG step by step
A:: 1) Create Resource Group
    2) Create Storage Account 
        - Create Storage Account
        - Go to Blob Storage
        - Create a Container
        - Upload your file (CSV, PDF, JSON, etc.)
    3) Create Azure AI Foundry resource
        - create
        - open this resource in Azure AI Foundry
    4) Go to deployments and create an embeddings model
        - choose model (e.g., text-embedding-3-small)
        - specify deployment type
    5) Create Search Service
        - create
        - open this resource
    6) Click import and vectorize data
        - select your blob storage data
        - select your embedding model
    7) Deploy your RAG app
        - select base model (e.g., gpt-4o)
        - add data source (your search service)
    8) Test your RAG app
        - use Azure AI Foundry playground to test your app
    9) You may find a code snippet in Azure AI Foundry to query your Azure RAG.


Q:: Fine tuning in Azure
A:: 1) Create Azure AI Foundry project
    2) Inside My Assets, click on "Deploy model", select for example "gpt-4o"
        - Select deployment type: standard, batch
    3) You may open it in a playground and test it.
    4) On the left panel, find "Fine-tuning"
        - Find a model
        - Add training data (e.g., JSONL file with prompt-completion pairs)
        - specify training parameters (e.g., epochs, learning rate)
    5) Wait for training to complete
    6) Click "Use this model" to deploy.


Q:: Azure RAG Agent
A:: 1) Create Azure AI Foundry project
    2) Deploy base model (e.g., gpt-4o)
    3) On the left above fine-tuning, find "Agents", find here your agent
    4) You can click "Knowledge" and add files knowledge to your agent (e.g., PDF, CSV, JSON) manually.
    5) Click "actions"
        - code interpreter - interprets files (.csv, .pdf, .json, .py). It will automatically read the file 
            and extract information from it.
    Code::
    1) Talk to agent via endpoint and angent ID


Q:: Tracing in Azure
A:: 1) Go to tracing in Azure AI Foundry
        - create tracing resource
    2) Click "manage data source" and grab a connection string
    3) In code:
        - create tracer
        - add this connection string to your tracing configuration 
        - with tracer
            span.set_attribute("key", "value")


Q:: Models evaluation in Azure
A:: 1) On the left panel create a new evaluation project
    2) Prepare evaluation dataset
    3) Select "Use your dataset"
    4) Select model to evaluate (e.g., gpt-4o)
    5) Make evaluation prompt
    6) Select evaluation criteria (e.g., accuracy, semantic similarity)


Q:: Azure chatbot
A:: 1) Go to templates and find chatbot template
        - go to git and copy code
    2) ???


Q:: Push image to Azure Container Registry
A:: 1) go to Portal Azure and click create Azure Container Registry
    2) go to CLI and login to Azure
    4) build your Docker image locally
    5) "docker push"



"""