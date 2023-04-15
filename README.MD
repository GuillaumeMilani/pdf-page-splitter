## Compile for MacOS

To compile the Python script into a macOS app, you can follow these steps:

Install PyInstaller:

```
pip install pyinstaller
```

Navigate to the directory containing your Python script and create a spec file using the following command:

```
pyinstaller --name=PDFSplitter --windowed --onefile pdf_cutter.py
```

This will create a spec file named PDFSplitter.spec in the same directory as your script.

Edit the spec file to include any additional files or data that your app needs.
For example, if your app requires any images or other resources, you can include them in the spec file using the datas
option.

Build the app using the spec file by running the following command:

```
pyinstaller PDFSplitter.spec
```

This will create a dist directory containing the app bundle.

Test the app by running the executable in the dist directory.

Note that when you run PyInstaller, it will attempt to bundle all the Python modules that your app depends on into
the executable. However, if your app depends on any non-Python libraries or packages, you may need to include them
manually in the spec file using the binaries option. Additionally, some Python packages may not be compatible with
PyInstaller and may require additional configuration to be included in the app bundle.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
