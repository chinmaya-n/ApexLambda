Apex
====
ApexLambda is a sample example on how to use Apex for AWS Lambda with python runtime. 
I was not able to find the correct options and usage when I tried Apex (for python) based on its documentation.
So, this sample lambda function configuration worked for me after digging into github issue pages and some guess work.
This function returns a message with a Hello and current system time (here: AWS Lambda server's).

Apex github page: https://github.com/apex/apex

For understanding the directory and file structure please visit the link above and read the project Readme.md file.
Visit http://apex.run/ for complete options and usage of Apex.

Changes to make this sample work
================================
* In project.json, for role, I have replaced the unique id generated by AWS for a user with 12312312312. You need to create your own role with permission to write to AWS CloudWatch Logs. Copy that 'arn' and use it here.

Including python packages
=========================
In this demo I have used `arrow` package on purpose to demonstrate it. If you don't use any external package in your Lambda function, then you don't need to worry about this part.
* If you use any non native python packages in your `functions/<FunctionName>/index.py`, you need to copy that package into `functions/<FunctionName>/` (Use `virtualenv` and `pip` to get that package into a dummy directory and copy it to here).

You can change the name of the `index.py` to `main.py` but you also need to change the value for `handler` in `function.json` to `main.handle` from `index.handle`, where handle is the handling function in that file.

Using Apex
==========
* To deploy all functions
```
$ apex deploy
```
* To invoke a function (invokes on AWS Lambda and returns its result, invocation does *NOT* happen on local system)
```
$ apex invoke hello
```
* To see whats built into the .zip file created while deploying into AWS
```
$ apex build hello > test_build.zip
```

For more commandline usages and options refer to Apex documenation.


