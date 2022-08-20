import setuptools

setuptools.setup(
    name="magic-tables",
    version="0.0.1",
    author="reyemb",
    author_email="reyemb.coding@gmail.com",
    description="Add some functional to base streamlit dataframes",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 1.4",
    ],
)
