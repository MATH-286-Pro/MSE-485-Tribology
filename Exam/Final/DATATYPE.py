import dataclasses

@dataclasses.dataclass
class UNIT:
    # 压强
    Pa  = 1
    kPa = 1_000 * Pa
    MPa = 1_000_000 * Pa
    GPa = 1_000_000_000 * Pa

    # 长度
    mm = 0.001
    cm = 0.01
    m  = 1
    um = 0.000_001
    nm = 0.000_000_001
    
    # 力
    N = 1

    # 数值常量
    pi = 3.1415926