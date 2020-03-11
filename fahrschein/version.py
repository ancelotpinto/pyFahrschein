__all__ = ['VERSION', 'version_info']

VERSION = '0.1.0'


def version_info() -> str:
    import platform
    import sys
    from importlib import import_module
    from pathlib import Path

    dependencies = []
    for p in ():
        try:
            import_module(p.replace('-', '_'))
        except ImportError:
            continue
        dependencies.append(p)

    info = {
        'version': VERSION,
        'path': Path(__file__).resolve().parent,
        'python': sys.version,
        'platform': platform.platform(),
        'dependencies': dependencies,
    }
    return '\n'.join(
        '{:>20} {}'.format(k + ':', str(v).replace('\n', ' ')) for k, v in info.items())
