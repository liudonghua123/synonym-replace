# encoding=utf-8
import argparse
import jieba
import io
import os.path
from pathlib import Path

# https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def argParse():
    parser = argparse.ArgumentParser()
    defaultDictPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'synonym.txt')
    defaultUserDictPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'userSynonym.txt')
    defaultInputPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'demo.txt')
    defaultOutputPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'result.txt')
    parser.add_argument('-d', '--dict', nargs='?', const=defaultDictPath, type=str, default=defaultDictPath, help='指定内置同义词字典文件路径，默认为当前路径下的 synonym.txt')
    parser.add_argument('-u', '--userDict', nargs='?', const=defaultUserDictPath, type=str, default=defaultUserDictPath, help='指定自定义的同义词字典文件路径，默认为当前路径下的 userSynonym.txt')
    parser.add_argument('-i', '--input', nargs='?', const=defaultInputPath, type=str, default=defaultInputPath, help='指定输入的文件，默认为当前路径下的 demo.txt')
    parser.add_argument('-o', '--output', nargs='?', const=defaultOutputPath, type=str, default=defaultOutputPath, help='指定输出的文件，默认为当前路径下的 result.txt')
    parser.add_argument('-r', '--replaceWithDict', nargs='?', const=True, type=str2bool, default=True, help='指定是否使用内置同义词字典替换，默认值是 True')
    parser.add_argument('-p', '--replaceWithUserDict', nargs='?', const=True, type=str2bool, default=True, help='指定是否使用用户自定义同义词字典替换，默认值是 True')
    args = parser.parse_args()
    return args

def readFile(filePath):
    file = Path(filePath)
    if file.is_file():
        return io.open(filePath, mode="r", encoding="utf-8").read()

def writeFile(filePath, contents):
    file = Path(filePath)
    if file.is_file():
        print('{filePath} 已存在，内容会被覆盖'.format(filePath=filePath))
    io.open(filePath, mode="w", encoding="utf-8").write(contents)

def parseDict(contents):
    dictRecords = []
    for line in contents.splitlines():
        (search, replace) = line.split(',')
        dictRecords.append({'search': search, 'replace': replace})
    return dictRecords

def replace(dictRecords):
    def _replace(segment):
        for record in dictRecords:
            if(record['search'] == segment):
                print('替换 "{matchedText}" -> "{replacedText}"'.format(matchedText=segment, replacedText=record['replace']))
                return record['replace']
        return segment
    return _replace

if __name__ == "__main__":
    # 解析命令行参数
    args = argParse()
    print('命令行参数是 {args}'.format(args=args))
    dictRecords = parseDict(readFile(args.dict))
    userDictRecords = parseDict(readFile(args.userDict))
    inputContents = readFile(args.input)
    # 分词
    print('\n处理分词\n')
    segments = list(jieba.cut(inputContents))
    # 处理内置同义词替换
    if(args.replaceWithDict):
        replaceFunction = replace(dictRecords)
        print('\n处理内置同义词替换\n')
        segments = list(map(replaceFunction, segments))
    # 处理用户自定义同义词替换
    if(args.replaceWithUserDict):
        replaceFunction = replace(userDictRecords)
        print('\n处理用户自定义同义词替换\n')
        segments = list(map(replaceFunction, segments))
    # 组合结果
    resultContents = ''.join(segments)
    print('------------\n处理后的结果是\n------------\n{resultContents}'.format(resultContents=resultContents))
    # 保存结果
    writeFile(args.output, resultContents)
    
    