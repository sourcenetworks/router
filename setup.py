from setuptools import setup

install_requires = [
    'requests',
]

setup(
    name='two1router',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['two1router',
              'two1router.proxy',
              'two1router.apps',
              'two1router.apps.bitcoin'
    ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_requires,
)
