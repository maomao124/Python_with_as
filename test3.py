"""
 * Project name(项目名称)：Python_with_as
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 13:54
 * Version(版本): 1.0
 * Description(描述)： 
 """
from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()


if __name__ == '__main__':
    with file_manager('a.txt', 'w') as file:
        file.write('hello world\n')
        # file.read()
        file.write('hello world')
