# Assignment_Arya


The codebase is dockerized and simple to use.
Please follow the below instructions to run the codebase.
1.	Switch on MangoDB database and keep it running.
2.	Open terminal an navigate to the codebase directory.
3.	The code is dockerize so run the following command to build the docker-compose.yml file
docker-compose build
4.	After building keep the system running using the following command.
docker-compose up
5.	For debugging purpose and easy to use, I have used POSTMAN to send Json requests.
6.	For registering a url use the following Json request. Selecting POST method and URL as localhost:5000/api

{
    "url":"789.com"
}

7.	For updating the url use the following Json request. Selecting PUT method and URL-localhost:5000/api

{

    "oldurl":"789.com"
	    “newurl”:”xyx.com”
}

8.	To retrieve the url use the following Json request. Selecting POST method and URL-localhost:5000/goto to find the requested URL.

{
    "url":"xyz.com"
}

9.	 For Deleting the url use the following Json request. Selecting DELETE method and URL-localhost:5000/api

{
    "url":"xyz.com"
}
