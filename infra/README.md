# Considerations 
while implementing this solution, there where a few key factors to keep in mind 
- Security
- Scalability
- Fault tolerance
- Implementation of best code pratices


## Security 
To keep this deployment secure, I made use of containers as these provide an isolated environment for applications to run and reduce attack surface ,  as well as using IAM roles where necessary 

## Scalability  
Scalability is the main reason for choosing ECS it is able to run multiple replicas of a service and an application loadbalancer ensures requests are distributed amongst replicas. ECS also allows to for autoscaling which can help to meet sudden load spikes

## Fault tolerance 
Fault tolerance , This can be handled by having the ECS cluster in more than one availability zone 

## IAC
For infrastructure as code. and most of this code can be controlled via variables. 

## Running 

Simply edit `"ecs_image_url` to the desired image and run `terraform init` `terrafrom plan` and `terraform apply`