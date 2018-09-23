## Document Reconstructor
This tool helps you to reconstruct the document which has been stripped off of all the white spaces based on the words present in the lexicon. The tools uses backtracking algorithm to reconstruct the document. 

The tool takes three inputs:
* `--lexicon` - path to the lexicon file
* `--document` - path to the deconstructed document.
* `--output` - path to the output file.

> Note: Please use python version <b>3.4.1</b> or greater.

####Running the code
* Create a virtualenv, if you want to keep your global space clean.
    * `pip install virtualenv`
    * `virtual env --python=<path_python> <virtualenv_name>`
    * `source <virtualenv_name>/bin/activate` (depending on your shell).
* Install the package dependencies for the tool.
    * `pip install -r requirements.txt`
* Run the tool from the project's home directory.
    * `python reconstruct_document/run.py --lexicon <lexicon_path> --document <document_path> --output <output_path>`
    
> Note: To get the list of options supported by the tool, run - python reconstruct_document/run.py --help

####Tests
* The tool is shipped with a test suite for the Reconstruction class. To run the tests run the following command from the project's home directory:
    * `python -m unittest -v test.reconstruct_document.test_reconstruction`

####Usage
* Generating executables
    * Make sure all the project dependencies are installed - `pip install -r requirements.txt`
    * We will be using `pyinstaller` to generate executable binary.
        * Install `pyinstaller` if not already present - `pip install pyinstaller`.
        * Run the following command from the project's home directory - `pyinstaller --onefile -n reconstruct-document reconstruct_document/run.py`
        * The binary will be present inside the `dist` directory in the project's home folder.
        * Either copy the binary to the `/usr/local/bin` or copy it to any of the other directories and create a symlink to `/user/local/bin` using - 
        For eg: If the binary is present in the `/varlib/reconstruct-document` path we create a symlink to `/usr/local/bin` with -
        `ln -nfs /var/lib/reconstruct-document /usr/local/bin`.
        
> Note for more info on usage of `pyinstaller`, please use this [link](https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263). 
