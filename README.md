# PACER-client
Client stack for PACER client.

Environment variables:

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

