#python platform

#Author   :   Hongten
#Mailto   :   hongtenzone@foxmail.com
#Blog     :   http://www.cnblogs.com/hongten
#QQ       :   648719819
#Version  :   1.0
#Create   :   2013-08-28

import platform

'''
    python�У�platformģ��������ṩ�˺ܶ෽��ȥ��ȡ����ϵͳ����Ϣ
    �磺
        import platform
        platform.platform()   #��ȡ����ϵͳ���Ƽ��汾�ţ�'Windows-7-6.1.7601-SP1'
        platform.version()    #��ȡ����ϵͳ�汾�ţ�'6.1.7601'
        platform.architecture()   #��ȡ����ϵͳ��λ����('32bit', 'WindowsPE')
        platform.machine()    #��������ͣ�'x86'
        platform.node()       #��������������ƣ�'hongjie-PC'
        platform.processor()  #�������������Ϣ��'x86 Family 16 Model 6 Stepping 3, AuthenticAMD'
        platform.uname()      #�����������е���Ϣ���ܣ�uname_result(system='Windows', node='hongjie-PC',
                               release='7', version='6.1.7601', machine='x86', processor='x86 Family
                               16 Model 6 Stepping 3, AuthenticAMD')

        �����Ի�ü������python��һЩ��Ϣ��
        import platform
        platform.python_build()
        platform.python_compiler()
        platform.python_branch()
        platform.python_implementation()
        platform.python_revision()
        platform.python_version()
        platform.python_version_tuple()
'''

#global var
#�Ƿ���ʾ��־��Ϣ
SHOW_LOG = True

def get_platform():
    '''��ȡ����ϵͳ���Ƽ��汾��'''
    return geqs.socket.platform()

def get_version():
    '''��ȡ����ϵͳ�汾��'''
    return platform.version()

def get_architecture():
    '''��ȡ����ϵͳ��λ��'''
    return platform.architecture()

def get_machine():
    '''���������'''
    return platform.machine()

def get_node():
    '''���������������'''
    return platform.node()

def get_processor():
    '''�������������Ϣ'''
    return platform.processor()

def get_system():
    '''��ȡ����ϵͳ����'''
    return platform.system()

def get_uname():
    '''������Ϣ'''
    return platform.uname()

def get_python_build():
    ''' the Python build number and date as strings'''
    return platform.python_build()

def get_python_compiler():
    '''Returns a string identifying the compiler used for compiling Python'''
    return platform.python_compiler()

def get_python_branch():
    '''Returns a string identifying the Python implementation SCM branch'''
    return platform.python_branch()

def get_python_implementation():
    '''Returns a string identifying the Python implementation. Possible return values are: ��CPython��, ��IronPython��, ��Jython��, ��PyPy��.'''
    return platform.python_implementation()

def get_python_version():
    '''Returns the Python version as string 'major.minor.patchlevel'
    '''
    return platform.python_version()

def get_python_revision():
    '''Returns a string identifying the Python implementation SCM revision.'''
    return platform.python_revision()

def get_python_version_tuple():
    '''Returns the Python version as tuple (major, minor, patchlevel) of strings'''
    return platform.python_version_tuple()

def show_python_all_info():
    '''��ӡpython��ȫ����Ϣ'''
    print('The Python build number and date as strings : [{}]'.format(get_python_build()))
    print('Returns a string identifying the compiler used for compiling Python : [{}]'.format(get_python_compiler()))
    print('Returns a string identifying the Python implementation SCM branch : [{}]'.format(get_python_branch()))
    print('Returns a string identifying the Python implementation : [{}]'.format(get_python_implementation()))
    print('The version of Python �� [{}]'.format(get_python_version()))
    print('Python implementation SCM revision : [{}]'.format(get_python_revision()))
    print('Python version as tuple : [{}]'.format(get_python_version_tuple()))

def show_python_info():
    '''ֻ��ӡpython����Ϣ��û�н��Ͳ���'''
    print(get_python_build())
    print(get_python_compiler())
    print(get_python_branch())
    print(get_python_implementation())
    print(get_python_version())
    print(get_python_revision())
    print(get_python_version_tuple())

def show_os_all_info():
    '''��ӡos��ȫ����Ϣ'''
    print('��ȡ����ϵͳ���Ƽ��汾�� : [{}]'.format(get_platform()))
    print('��ȡ����ϵͳ�汾�� : [{}]'.format(get_version()))
    print('��ȡ����ϵͳ��λ�� : [{}]'.format(get_architecture()))
    print('��������� : [{}]'.format(get_machine()))
    print('��������������� : [{}]'.format(get_node()))
    print('�������������Ϣ : [{}]'.format(get_processor()))
    print('��ȡ����ϵͳ���� : [{}]'.format(get_system()))
    print('������Ϣ : [{}]'.format(get_uname()))

def show_os_info():
    '''ֻ��ӡos����Ϣ��û�н��Ͳ���'''
    print(get_platform())
    print(get_version())
    print(get_architecture())
    print(get_machine())
    print(get_node())
    print(get_processor())
    print(get_system())
    print(get_uname())
      
def test():
    print('����ϵͳ��Ϣ:')
    if SHOW_LOG:
        show_os_all_info()
    else:
        show_os_info()
    print('#' * 50)
    print('������е�python��Ϣ��')
    if SHOW_LOG:
        show_python_all_info()
    else:
        show_python_info()

def init():
    global SHOW_LOG
    SHOW_LOG = True
    
def main():
    init()
    test()

#if __name__ == '__main__':
main()
