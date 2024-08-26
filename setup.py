from setuptools import setup, find_packages

setup(
    name='image_resizer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0.0',
        'Pillow>=8.0.0',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'image-resizer=image_resizer.app:main',
        ],
    },
    python_requires='>=3.6',
    author='Shivan Kumar',
    author_email='kshivan84@gmail.com',
    description='A Flask application for resizing images',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shivan118/image_resizer',  # Change to your repository URL
    license='MIT',
)
