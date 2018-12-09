# synonym-replace

### How to run
1. git clone https://github.com/liudonghua123/synonym-replace.git (或者下载Zip源码)
2. cd synonym-replace
3. pip install -r requirements.txt (安装依赖库)
4. python main.py

### More details

```
# 查看帮助
>python main.py -h
usage: main.py [-h] [-d [DICT]] [-u [USERDICT]] [-i [INPUT]] [-o [OUTPUT]]
               [-r [REPLACEWITHDICT]] [-p [REPLACEWITHUSERDICT]]

optional arguments:
  -h, --help            show this help message and exit
  -d [DICT], --dict [DICT]
                        指定内置同义词字典文件路径，默认为当前路径下的 synonym.txt
  -u [USERDICT], --userDict [USERDICT]
                        指定自定义的同义词字典文件路径，默认为当前路径下的 userSynonym.txt
  -i [INPUT], --input [INPUT]
                        指定输入的文件，默认为当前路径下的 demo.txt
  -o [OUTPUT], --output [OUTPUT]
                        指定输出的文件，默认为当前路径下的 result.txt
  -r [REPLACEWITHDICT], --replaceWithDict [REPLACEWITHDICT]
                        指定是否使用内置同义词字典替换，默认值是 True
  -p [REPLACEWITHUSERDICT], --replaceWithUserDict [REPLACEWITHUSERDICT]
                        指定是否使用用户自定义同义词字典替换，默认值是 True
```

例如
```
# 处理 C:/input.txt，仅使用内置内置同义词字典替换，输出为 C:/result.txt
python main.py -i 'C:/input.txt' -o 'C:/result.txt' -p False
```

1. `-d` 指定内置同义词字典文件路径，默认是`synonym.txt`
2. `-u` 指定自定义的同义词字典文件路径，默认是`userSynonym.txt`
3. `-i` 指定输入的文件，默认为当前路径下的`demo.txt`
4. `-o` 指定输出的文件，默认为当前路径下的`result.txt`
5. `-r` 指定是否使用内置同义词字典替换，默认值是`True`
6. `-p` 指定是否使用用户自定义同义词字典替换，默认值是`True`