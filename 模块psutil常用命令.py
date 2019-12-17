# coding:utf-8
import psutil

# 显示CPU信息
print(psutil.cpu_count())  # CPU逻辑数量
print(psutil.cpu_count(logical=False))  # CPU物理核心
print(psutil.cpu_times())  # CPU用户、系统、空闲时间
for x in range(10):  # 类似top命令的CPU使用率，每秒刷新一次，累计10次
    print(psutil.cpu_percent(interval=1, percpu=True))

# 显示内存信息
print(psutil.virtual_memory())  # 获取物理内存信息
print(psutil.swap_memory())  # 获取物理内存和交换内存信息

# 显示磁盘信息
print(psutil.disk_partitions())  # 磁盘分区信息
print(psutil.disk_usage('C:\\'))  # Windows的路经，磁盘使用情况
print(psutil.disk_io_counters())  # 磁盘IO

# 显示网络信息
print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
print(psutil.net_if_addrs())  # 获取网络接口信息
print(psutil.net_if_stats())  # 获取网络接口状态
print(psutil.net_connections())  # 获取当前网络连接信息

# 显示进程信息
print(psutil.pids())  # 所有进程ID
p = psutil.Process(16112)
print(p.name())  # 进程名称
print(p.exe())  # 进程exe路径
print(p.cwd())  # 进程工作目录
print(p.cmdline())  # 进程启动的命令行
print(p.ppid())  # 父进程ID
print(p.parent())  # 父进程
print(p.children())  # 子进程列表
print(p.status())  # 进程状态
print(p.username())  # 进程用户名
print(p.create_time())  # 进程创建时间
print(p.cpu_times())  # 进程使用的CPU时间
print(p.memory_info())  # 进程使用的内存
print(p.open_files())  # 进程打开的文件
print(p.connections())  # 进程相关网络连接
print(p.num_threads())  # 进程的线程数量
print(p.threads())  # 所有线程信息
print(p.environ())  # 进程环境变量
print(psutil.test())  # 类似Linux的ps
