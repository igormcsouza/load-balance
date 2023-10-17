# Load Balance with NGINX

Load balancing is a know issue on the development world, and there are many products out there to solve it. Nginx is one of them. It distributes the load across all the available instances so everyone has the same number of calls.

## How to test it?

I'm using docker and docker compose to orchestrate between the instances, in this case, NGINX take the role of gateway, getting the traffic and proxing it to the container ran by compose. The makefile has the instructions to run. Below there is a detailed explaination of the targets.

* `start`: Start the compose runing the NGINX and 3 instances of API, change the value on scale to update the number of instances. The NGINX configuration only allow 10 connections tho.
* `rebuild`: If changes are made no the files on the api, the container must be rebuilt.
* `stop`: Stop all components altogether.
