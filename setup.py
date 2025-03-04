from setuptools import setup, find_packages

# Read README content
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="opencv-document-scanner",
    version="0.1.0",
    description="A document scanner application using OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Andrew Campbell",
    author_email="andrewc@captricity.com",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "imutils>=0.5.4",
        "matplotlib>=3.3.0",
        "pylsd @ git+https://github.com/primetang/pylsd@refs/pull/17/head"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics",
        "Operating System :: OS Independent",
    ],
    keywords="opencv document scanner image-processing computer-vision",
    project_urls={
        "Bug Reports": "https://github.com/username/OpenCV-Document-Scanner/issues",
        "Source": "https://github.com/username/OpenCV-Document-Scanner",
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'document-scanner=opencv_document_scanner.scan:main',
        ],
    },
)