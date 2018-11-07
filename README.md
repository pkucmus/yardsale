# yardsale

## Configuration by environment variables

| Environment Variable       | Description                                                                                                                                   | Example value                   |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| DJANGO_SETTINGS_MODULE     | Point to a Django settings module                                                                                                             | service.settings.common         |  
| YARDSALE_DATABASE_NAME     | Name of the database schema                                                                                                                   | "yardsale"                      |  
| YARDSALE_DATABASE_USER     | Database user that is allowed to reach and modify the database schema                                                                         | "postgres"                      |  
| YARDSALE_DATABASE_PASSWORD | Password for the database user                                                                                                                | "password"                      |  
| YARDSALE_DATABASE_HOST     | Host through which the service will be able to reach the database service                                                                     | "db"                            |  
| YARDSALE_DATABASE_PORT     | Port on which the database service is listening                                                                                               | 5432                            |  
| ALLOWED_HOSTS              | Django's allowed hosts protection configuration - define the host through which the service will be reached (comma separated for many values) | "127.0.0.1,10.93.7.16"          |  
| SNIPEIT_URL                | URL through which the service will be able to reach the SnipeIt service                                                                       | "https://snipeit.stxnext.local" |  
| SNIPEIT_API_JWT            | SnipeIt API JWT                                                                                                                               | ${SNIPEIT_JWT}                  |  
| SNIPEIT_HTTPS_VERIFY       | Unix path to the ca-storage containing self-signed certificates or string `false` do disable https verification                               | "false"                         |  
| EMAIL_HOST                 | Host through which the service will be able to reach the SMTP service                                                                         | "smtp"                          |  
| EMAIL_PORT                 | Port on which the SMTP service is listening                                                                                                   | 1025                            |  
| EMAIL_FROM                 | Specifies the from field in an outgoing email from the service                                                                                | "developer@stxnext.pl"          |  
| EMAIL_HOST_USER            | Username to authenticate in the SMTP service (if required)                                                                                    | "developer@stxnext.pl"          |  
| EMAIL_HOST_PASSWORD        | Password for the SMTP user (if required)                                                                                                      | "pawel.kucmus@stxnext.pl"       |  


## Development

You can use the db and smtp defined in compose

$ docker-compose up -d smtp db

Then run as normal

$ docker-compose run --rm --service-ports app

## Production

$ docker-compose -f docker-compose.yml -f docker-compose.prod.yml build app
$ docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d app web

