# 0x02. Redis Basic

## Back-end | Redis

### Project Overview
**Weight**: 1  
**Ongoing second chance project**: started Jun 19, 2024, 6:00 AM, must end by Jun 22, 2024, 6:00 AM  
An auto review will be launched at the deadline.

### In a nutshell...
Auto QA review: 0.0/27 mandatory & 0.0/6 optional  
Altogether: 0.0%  
Mandatory: 0.0%  
Optional: 0.0%  
Calculation: 0.0% + (0.0% * 0.0%) == 0.0%

### Resources
Read or watch:
- [Redis Crash Course Tutorial](#)
- [Redis commands](#)
- [Redis python client](#)
- [How to Use Redis With Python](#)

### Learning Objectives
- Learn how to use Redis for basic operations
- Learn how to use Redis as a simple cache

### Requirements
- All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All of your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the pycodestyle style (version 2.5)
- All your modules should have documentation:
  ```sh
  python3 -c 'print(__import__("my_module").__doc__)'


All your classes should have documentation:
python3 -c 'print(__import__("my_module").MyClass.__doc__)'

### Install Redis on Ubuntu 18.04
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

### use redis container

service redis-server start

