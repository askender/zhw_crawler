# Automatically created by: scrapy deploy

from setuptools import setup, find_packages

setup(
    name='zhw_crawler',
    version='0.5',
    packages=find_packages(),
    package_data={
        'zhw_crawler': ['conf/ids_list_*', 'conf/proxy_list_*']
    },
    entry_points={
        'scrapy': ['settings = zhw_crawler.settings']
    },
)
