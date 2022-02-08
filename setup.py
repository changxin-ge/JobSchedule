import setuptools

module_name = 'JobScheduleEnv'
setuptools.setup(
    name=module_name,
    version='0.0.1',
    author='Pengxiang Xu',
    author_email='pengxiang.xu@ibm.com',
    description='Job schdule environment for reinforcement learning',
    url="https://github.com/changxin-ge/JobSchedule/",
    packages=setuptools.find_packages(),
    classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['gym', 'pandas', 'numpy'],
    include_package_data=True
)