# PACER-client
Client software stack for PACER. This client is designed to be deployed at the health department side where electronic lab report (ELR) is being reported. While the PACER is designed to generate electronic case report for a sexual transmitted diseases (STD), the architecture can easily reconfigured for another case reporting.

If you are installing on Windows, please go to https://github.com/gt-health/PACER-client-win

## Prerequisite 
There are several ways to install the PACER-client. The easiest way to install is using Docker. Please go to https://docs.docker.com/engine/ and download and install Docker engine for your linux VM.

## Redhat Distriution
If you Linux OS is Redhat, please do follows to install Docker.
1. sudo yum update
2. Follow instruction on https://docs.docker.com/engine/install/centos/
3. Follow instruction on https://docs.docker.com/engine/install/linux-postinstall/

To download, git clone --recurse https://github.com/gt-health/PACER-client.git

There will be updates. To get the latest updates, perform the following two commands in the server.
```
> git pull
```
and
```
> . ./updateSubmodules.sh
```

These two commands must be run in order to get all the updates.

## Build and Deploy using Docker Composer
1. Configure the environment in the composer file if necessary. In most cases, you can use pre-assigned environment variables. 
2. run the following command
```
> sudo docker-compose up --build -d
```
3. To bring the docker containers down
```
> sudo docker-compose down
```

> **Note**
> Bringing down the composed container will remove entire components including data in the database. 
> Thus, if there are any data in the database that needed to be maintained, those need to be backed up.

## Environment Variables
Open docker-compose.yml file to set the environment variables. The docker-composer.yml are already preconfigured to run itself with a mimnum configurations. However, it's hightly recommended to change the site-speicific information and keep them safely.

## Configuration of PACER-client
Once all components are successfully deployed, PACER-Index-API service must be configured for ELR message triggered query can be sent to the provider. From docker-compose.yml file, find a pacer-index-api component configuration section. From the ports setting (formated ####:####), the first port number is what needs to be opened on the host server and firewall for the host server. 

Use the following command to open the port on the host server. For the Redhat distribution and if the port number is 8086,

```
> sudo firewall-cmd --permanent --add-port 8086/tcp
```

This will open port 8086 on the host server. After firewall (if firewall exists between user's local computer and the host server) opens the port number as well, go to the following URL from a web browser at the user's computer.  

> http://<host_server_url>:8086/pacer-index-api/1.0.0/

This will open the Swagger API document page where user can set up the PACER-Index-API entries. First, go to manage-api-controller section from the API document. Then, click on the "GET /pacer-index-api/1.0.0/manage" then click on "Try it out" button. If asked for username and password, use the pair that you have specified in the docker-compose.yml under pacer-index-api section.

After "Try it out" button is clicked, check the response for existing pacer-index entries. If appropriate index entry is not found, new entry needs to be added. To add, click on "POST /pacer-index-api/1.0.0/manage" section. Then, click on "Try it out" button. Then, add the following content in the request body field.

```
{
  "providerName": "John Duke",
  "identifier": "ORDPROVIDER|P49430",
  "pacerSource": {
    "name": "PACER test",
    "serverUrl": "https://musctest.hdap.gatech.edu/JobManagementSystem/List",
    "security": {
      "type": "basic",
      "username": "username",
      "password": "password"
    },
    "version": "1.0.0",
    "type": "ECR"
  }
}
```

This will add the test entry for a testing PACER server at GTRI site. Once a partner site is identified, that end point must be added to the service.

## ELR Receiver testing with a testing ELR Triggering Message
PACER-client package comes with a sample ELR message that will trigger the ECR Manager with a matching provider information in the PACER-index-api. In order to test, Java must be installed. Run the following commands to install openjdk package to Redhat.

```
> yum update -y
> yum install java-openjdk
> java -version
```

The last line of commands must print the version of Java if the java is successfully installed. Next, run the following command to set up the environment variable for the ELR sender to choose right file and method.

```
> . ./env_config.sh
```

This will set up the environment variable (if default has not been changed for the port number the ELR Receiver will be listening to (default: 8087). Then, next command to send the ELR message is as follow,

```
> java -jar ./elr_sender-0.0.2-jar-with-dependencies.jar
```

This command should have a response message similar to the follow,

```
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
Received response:
MSH|^~\&|ELR|SPH| GT|Reliable|20230206192649.572+0000||ACK^R01^ACK|1|P|2.5.1
MSA|AA|20070701132554000008

End of response message
```
