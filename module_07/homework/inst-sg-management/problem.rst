*********************
 Problem Description
*********************
Write a program using Python and Boto3 to automate all
of the following tasks.


Part 1. Create your EC2 instances
---------------------------------
Create five identical EC2 instances with type ``t2.micro``
and name ``YellowTail``. Output the id of each instance.


Part 2. Terminate EC2 Instances
-------------------------------
Terminate the instances you just created.


Part 3. Creating security group with inbound rule
-------------------------------------------------
* Create a security group that allows SSH ingress.
* Create three instances with that security group.
* Show that port 22 is up and listening on each
  instance.


Part 4. Assesing your AWS environment
-------------------------------------
Generate a report that lists all:

* running instances
* security groups
* unused security groups

To determine if a security group is used, check
against the running instances.
