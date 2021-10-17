import platform

if "LINUX" in platform.system().upper():
    print("----------------生产环境启动---------------")
    from .development_config import config
else:
    print("----------------开发环境启动---------------")
    from .production_config import config

