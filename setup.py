from setuptools import setup, find_packages
setup(
    name="Signer",
    version="1.6",
    description="Signer For TikTok",
    author="Lariot",
    author_email="lariot.antsa@gmail.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'report-tiktok=TikTok.main:main'
        ]
    },
    python_requires=">=3.6",
)
