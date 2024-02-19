# This directory contains the tasks for file 0x19. Postmortem

## DevOps SysAdmin

<div align="center">

<p>

<img src="https://github.com/omotomiwa26/alx-system_engineering-devops/blob/master/0x19-postmortem/debug.jpg"/> <img src="https://github.com/omotomiwa26/alx-system_engineering-devops/blob/master/0x19-postmortem/fingerPaint-variables.gif"/>

</p>

</div>


### Issue Summary

Duration:

- Start Time: January 18, 2024, 12:30 W.A.T

- End Time: January 18, 2024, 13:00 W.A.T

Impact: Users were trying to access a wordpress [website](https://127.0.0.1) from their web browser the apache webserver was returning a 500 internal error.

Root Cause: The Apache error was discovered to be caused by an incorrect file extension in one of the web application configuration files.

### Timeline

-  12:30 W.A.T: The server error was detected when a user experincing the issue filled and the support form and the mail was immediatly received by my, the engineer on duty.

- 12:35 W.A.T: I immediately swung into action by first trying to access the [website](https://127.0.0.1) from my browser to accertain the issue and i also encountered the same error.

- 12:40 W.A.T: I initiated the troubleshooting process according to standard software engineering and debugging procedures.

- 12:55 W.A.T: I identified the cause of server error as bein an incorrect file extention in the web application configuration file precisely `class-wp-locale.phpp` file having a `.phpp` extension instead of `.php` extension.

- 13:00 W.A.T: I fixed the error and the [website](https://127.0.0.1) was fully back and running perfectly with no issues.

### Root Cause and Resolution

Root cause:

- I traced and trobleshooted the cause of error by intially loging-in via SSH to the server and then run `curl -sI 127.0.0.1 which return the internalserver error on my terminal.

```
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html
````

- The next thing i did was to get The `PID` of the running Apache proccess and attach it to strace to debug the apache process currently running while i opened another terminal next to it to allow me to effectively read and debug the running procces.

- I printed the output of the strace result to an `error.txt` file and then opened the file in the other termial to exmaine and read line ny line.

- It was during the process of reading the `error.txt` file that i noticed the line that executed the `class-wp-locale.phpp` has a _1_ exit status isntead of _0_ which indicates an error exit status.

- I then `cd` into the directory that contained the file to properply examine the cause of error and then discovered theincorrect file extention being `.phpp` instead of `.php`.

- I discovered immediately that was the cuase of the _1_ exit status and the `500 Internal Server Error`.

Resolution:

- I fixed the error by simply correcting the `.phpp` extension in the file to `.php`.

- To achieve this i automated the process by writing a bash script `apache_error_fix.sh` to fix the incorrect extension.

```
#!/usr/bin/env bash

#This bash script fixes why Apache is returning a 500 errorin the [website](https://127.0.0.1)

sed -i 's/phpp/php/g' /var/www/html/wp-settings.php
```

- I changed the permission of the file `apache_error_fix.sh`using `chmod +x apache_error_fix.sh` then ran the file `./ apache_error_fix`.

- After running the file succesfully i then ran `curl -sI 127.0.0.1` and discovered the error has being fixed by returning `200 OK`

```
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8
````

- I also ran `curl -s 127.0.0.1:80 | grep Holberton` as a final test to accertain that everything is now working perfectly with no server errors.

````
root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
````

### Corrective and Preventative Measures

- The fix was finally deployed to production with everything up and running perfectly and the users were updated that the [website](https://127.0.0.1) is back up with apologies for any inconviniences caused during the time the [website](https://127.0.0.1) was inaccessible.
