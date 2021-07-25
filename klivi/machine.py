import platform

def machine() -> dict:
    machine:str = platform.machine()
    node:str = platform.node()
    system:str = platform.system()
    processor:str = platform.processor()
    arch:tuple = platform.architecture()
    return {
        "machine": machine,
        "node": node,
        "system": system,
        "processor": processor,
        "arch": arch
    }
