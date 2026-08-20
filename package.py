name = 'gromitmpx'
version = '1.9'

variants = [
    ['platform-linux'],
    ]

private_build_requires = [
    "cmake-3",
    ]

with scope("config") as config:
    config.release_packages_path = "/s/apps/packages/cg"

def commands():
    env.XDG_CONFIG_HOME.append('{root}/etc/gromit-mpx')
    env.XDG_DATA_DIRS.append('{root}/share')

    # GDK_CORE_DEVICE_EVENTS disables the XInput extension in GDK, which
    # gromit-mpx requires to function.
    unsetenv('GDK_CORE_DEVICE_EVENTS')

    alias('gromit', '{root}/bin/gromit-mpx')