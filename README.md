# PACER-client
Client software stack for PACER. This client is designed to be deployed at the health department side where electronic lab report (ELR) is being reported. While the PACER is designed to generate electronic case report for a sexual transmitted diseases (STD), the architecture can easily reconfigured for another case reporting.

If you are installing on Windows, please go to https://github.com/gt-health/PACER-client-win

## Prerequisite 
There are several ways to install the PACER-client. The easiest way to install is using Docker. Please go to https://docs.docker.com/engine/ and download and install Docker engine for your linux VM.

To download, git clone --recurse https://github.com/gt-health/PACER-client.git

Environment variables:

Howe to install using Docker composer:
1. Configure the environment in the composer file if necessary. In most cases, you can use pre-assigned environment variables. 
2. run the following command
```
> sudo docker-compose up --build -d
```
3. 

ecr-manager

| env variable         |      value                                                       |
|----------------------|------------------------------------------------------------------|
| JDBC_URL             |  jdbc:postgresql://ecr-postgresql:5432/ecr                       |
| JDBC_USERNAME        |  put_your_username                                               |
| JDBC_PASSWORD        |  put_your_password                                               |
| PACER_INDEX_SERVICE  |  http://pacer-index-api/1.0.0/search                             |


ecr-receiver

| env variable         |      value                                                       |
|----------------------|------------------------------------------------------------------|
| ECR_URL              |  http://ecr-manager:8080/ecr-manager/ECR                         |
| PARSER_MODE.         |  ECR                                                             |
| TRANSPORT_MODE       |  MLLP                                                            |

