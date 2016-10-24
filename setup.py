from setuptools import setup, find_packages


setup(
    name='pretix-passbook',
    version='0.0.0',
    description='Passbook tickets for pretix',
    long_description='Provides passbook tickets for pretix',
    author='Tobias Kunze',
    author_email='rixx@cutebit.de',

    include_package_data=True,
    entry_points="""
[pretix.plugin]
passbook=passbook:PretixPluginMeta
""",
)