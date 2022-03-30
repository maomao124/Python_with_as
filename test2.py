"""
 * Project name(项目名称)：Python_with_as
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 13:48
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    with open("test2.py", "r", encoding="utf-8") as filein:
        with open("out.txt", "w", encoding="utf-8") as fileout:
            fileout.writelines(filein.readlines())
