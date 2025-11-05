# 快速开发 Web (Python)

```
sudo apt install python3-venv
python3 -m venv vbuild

激活虚拟环境
pip install fastapi
//pip install "uvicorn[standard]"
pip install uvicorn  # ASGI服务器
pip install pydantic # 校验数据
pip install jinja2
pip freeze > requirements.txt

$ uvicorn quickstart:app --reload --host 0.0.0.0  --port 8000  

自动生成swagger接口文档，浏览器访问
http://127.0.0.1:8080/docs

RESTful规范
POST /student/  增加
GET  /student/  获取所有
GET  /student/1 获取id=1
PUT  /student/1 更新id=1
DELETE /student/1  删除id=1
```

目录结构
```
http://192.168.1.1:3000/cnki/2025Q3-pyfast-monitor
http://192.168.1.1:3000/cnki/2025Q3-pyfast-monitor2

web/opentui/web-desktop
====== 硕士学位论文/MSE/Master of Software Engineering/  mse-thesis-2025
HOWTO
Dockerfile
main.py
lib.py
router/util.py
static/image/favico.ico
public/main.js
templates/react.html
```


https://gitee.com/mizhexiaoxiao/vue-fastapi-admin
```
ORM SQLAlchemy sync/async engines
表单 WTForms form building
ORM SQLModel support
UI组件 Tabler
SQLAlchemy 示例, SQLModel 好像更简单
https://cloud.tencent.com/developer/article/2561405


https://github.com/ChristopherGS/ultimate-fastapi-tutorial
https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-6-jinja-templates/
```

# 快速开发 WEB (PHP)

https://github.com/filamentphp/filament

借助Livewire快速构建与部署管理后台及应用系统

### 安装 php
```
只安装php 依赖 apache2, php-cli, php-common
sudo apt install php php-cli php-common
sudo apt install php-dev

$ php --version
$ php --ri redis
php --ri <extension>：输出PHP扩展的信息。

$ php test.php
<?php
echo "hello php cli\n";
var_dump($_SERVER['argc']);
?>
```

## 安装 composer

https://getcomposer.org/
```
wget https://getcomposer.org/download/2.8.12/composer.phar
sudo mv composer.phar /usr/local/bin/composer
composer --version

=== 切换到cnki
composer require predis/predis
安装在   $HOME/vendor
配置文件 $HOME/composer.json

=== 加载位置 vendor/autoload.php
<?php
require 'vendor/autoload.php';
Predis\Autoloader::register();

$redis = new Predis\Client('tcp://127.0.0.1:6379');
$rs = $redis->xread(1,null, ['icinga:stats'], '0');
echo is_array($rs);

$redis->set('foo', 'predis');
echo $redis->get('foo');
?>
```


### 创建项目 Laravel

https://github.com/leokhoa/laragon/releases  收费的
```
自带php,mysql,apache。 nodejs, python, redis, php-composer, HeidiSQL客户端
https://laravel-study.catchadmin.com/start/hello-laravel

登录 mysql:
127.0.0.1:3306
root
密码空

打开命令行
composer -v
# 安装镜像
composer config -g repos.packagist composer https://packagist.pages.dev
# 删除镜像
composer config -g --unset repos.packagist

初始化 Larvel
composer global require laravel/installer
Laravel -v
laravel.bat -v
laravel.bat new myapp

访问 :8000  :5173
cd myapp
composer run dev
```


### 创建项目 filament
https://crowall.com/2025/10/31/Filament-Laravel-12.html
https://juejin.cn/post/7462295981250674727
```
sudo apt install php-intl  php-zip

# 创建项目
composer create-project laravel/laravel:"^12.0" filament-skeleton
cd filament-skeleton

# 安装 Filament（v3）
composer require filament/filament:"^3.3" -W
php artisan filament:install --panels

创建用户账号，浏览器访问 /admin
php artisan make:filament-user
```


# 快速开发 WEB (Java)

https://github.com/spring-projects/spring-petclinic.git

基于 Spring 的示例应用程序，替换thymeleaf为freemarker，更适合layout布局

```
start.spring.io  JDK17
  implementation 'org.springframework.boot:spring-boot-starter-web'
  implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
  implementation 'org.springframework.boot:spring-boot-starter-freemarker'
  implementation 'org.springframework.boot:spring-boot-starter-validation'
  implementation 'org.springframework.boot:spring-boot-starter-cache'
  implementation 'javax.cache:cache-api'
  runtimeOnly 'org.springframework.boot:spring-boot-starter-actuator'

  implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
  runtimeOnly 'com.h2database:h2'
  runtimeOnly 'com.mysql:mysql-connector-j'
  runtimeOnly 'org.postgresql:postgresql'

其他依赖
  implementation 'jakarta.xml.bind:jakarta.xml.bind-api'
  runtimeOnly "org.webjars:webjars-locator-lite:1.1.1"
  runtimeOnly "org.webjars.npm:bootstrap:5.3.8"
  runtimeOnly "org.webjars.npm:font-awesome:4.7.0"
  runtimeOnly 'com.github.ben-manes.caffeine:caffeine'
```

配置、数据库
```
# database init, supports mysql too
database=h2
spring.sql.init.schema-locations=classpath*:db/${database}/schema.sql
spring.sql.init.data-locations=classpath*:db/${database}/data.sql

# Web
spring.thymeleaf.mode=HTML

# JPA
spring.jpa.hibernate.ddl-auto=none
spring.jpa.open-in-view=false

# Actuator
management.endpoints.web.exposure.include=*

# Logging
logging.level.org.springframework=INFO
# logging.level.org.springframework.web=DEBUG
# logging.level.org.springframework.context.annotation=TRACE
```
