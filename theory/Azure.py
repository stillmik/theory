"""
Q:: Azure Subscriptions
A:: Azure Subscriptions are the billing and access control units in Azure. They allow you 
    to manage resources, set budgets, and control access to resources. Each subscription 
    has a unique ID and can be associated with one or more Azure Active Directory tenants.


Q:: Azure Tenant
A:: An Azure Tenant is a dedicated instance of Azure Active Directory (AAD) that an organization 
    receives when it signs up for a Microsoft cloud service. It provides identity and access 
    management for users, groups, and applications within the organization.
    

Q:: Azure Virtual Machines
A:: Azure Virtual Machines (VMs) are EC2-like compute resources in Azure.


Q:: Management Groups
A:: Management groups are containers that help you manage multiple Azure subscriptions. 
    They allow you to organize subscriptions into a hierarchy for better governance.


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


Q:: Azure Resource Groups
A:: Azure Resource Groups are logical containers that hold related Azure resources.



"""