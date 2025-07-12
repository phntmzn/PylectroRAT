

from setuptools import setup, find_packages

setup(
    name="PylectroRAT",
    version="1.0.0",
    description="Modular Remote Access Tool for educational and research use",
    author="brx86",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "flask",
        "pyautogui",
        "pynput",
        "pycryptodome"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)