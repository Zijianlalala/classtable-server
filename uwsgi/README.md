# Nginx服务
为Nginx添加当前目录下的`classtable`配置文件,

# uWSGI服务

## 启动
```
uwsgi --ini uwsgi.ini
```

## 关闭

```
uwsgi --stop /tmp/classtable.pid
```
