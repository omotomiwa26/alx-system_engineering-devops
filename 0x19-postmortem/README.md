# This directory contains the tasks for file 0x19. Postmortem

## DevOps SysAdmin

### Issue Summary

Duration:

- Start Time: January 18, 2024, 12:30 W.A.T

- End Time: January 18, 2024, 13:00 W.A.T

Impact: Users were tyring to access a wordpress ![website](127.0.0.1) from their web breowser the apache webserver was returning a 500 internal error.

Root Cause: The Apache error was discovered to be caused by an incorrect file extension in one of the web application configuration files.

### Timeline

-  12:30 W.A.T: The server error was detected when a user experincing the issue filled and the support form and the mail was immediatly received by my, the engineer on duty.

- 12:35 W.A.T: I immediately swung into action by first trying to access the ![website](127.0.0.1) from my browser to accertain the issue and i also encountered the same error.

- 12:40 W.A.T: I initiated the troubleshooting process according to standard software engineering and debugging procedures.

- 12:55 W.A.T: I identified the cause of server error as bein an incorrect file extention in the web application configuration file precisely `class-wp-locale.phpp` file having a `.phpp` extension instead of `.php` extension.

- 13:00 W.A.T: I fixed the error and the ![website](127.0.0.1) was fully back and running perfectly with no issues.

### Root Cause and Resolution

Root cause:

- I traced and trobleshooted the cause of error by intially loging-in via SSH to the server and then run `curl -sI 127.0.0.1 which return the internalserver error on my terminal.

`
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html
`

- The next thing i did was to get The `PID` of the running Apache proccess and attach it to strace to debug the apache process currently running while i opened another terminal next to it to allow me to effectively read and debug the running procces.

- I printed the output of the strace result to an `error.txt` file and then opened the file in the other termial to exmaine and read line ny line.

- It was during the process of reading the `error.txt` file that i noticed the line that executed the `class-wp-locale.phpp` has a _1_ exit status isntead of _0_ which indicates an error exit status.

- I then `cd` into the directory that contained the file to properply examine the cause of error and then discovered theincorrect file extention being `.phpp` instead of `.php`.

- I discovered immediately that was the cuase of the _1_ exit status and the `500 Internal Server Error`.

Resolution:

- I fixed the error by simply correcting the `.phpp` extension in the file to `.php`.

- To achieve this i automated the process by writing a bash script to fix the incorrect extension.

`
#!/usr/bin/env bash

# This bash script fixes why Apache is returning a 500 errorin the ![website](127.0.0.1)

sed -i 's/phpp/php/g' /var/www/html/wp-settings.php
`

### Corrective and Preventative Measures
