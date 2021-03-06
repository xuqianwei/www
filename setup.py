from setuptools import setup, find_packages

setup(
    name="www",
    python_requires=">=3.7",
    install_requires=[
        "aiofiles==0.4.*",
        "ddtrace==0.31.*",
        "ddtrace-asgi==0.3.*",
        "gunicorn==19.*",
        "jinja2==2.10.*",
        "markdown==3.1.*",
        "pygments==2.5.*",
        "python-frontmatter==0.5.*",
        "starlette==0.13.*",
        "uvicorn==0.11.*",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    classifiers=["Private :: Do Not Upload"],
)
