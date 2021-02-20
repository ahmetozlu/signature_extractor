# "Signature Extraction" based connected component analysis

A design and implementation of a super lightweight algorithm for "overlapped handwritten signature extraction from scanned documents" using OpenCV and scikit-image on python. ***Please contact if you need professional signature detection & recognition & segmentation & counting project with the super high accuracy!***

---

- Input = The scanned document
- Output = The signatures exist on the input

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47317435-38003480-d652-11e8-87be-0d93ea9e119a.png" | width=750>
</p>

**TODOs:**

- "Outliar Removal" module will be improved to boost the signature extraction algorithm.
- CNN based "Signature Recognition" module will be developed.
- "Signature Spoofing Detection" algorithm will be developed.
- "Signature Detector (bounding box) & Counter" module will be developed.
- "Accuracy of detection on [SigSA: On-line Handwritten Signature Database](http://research.sabanciuniv.edu/13568/1/SigDB.pdf)" will be calculated and shared.

---

## Demo of a Real-life Application of Signature Extraction Algorithm

You can find a [sample project](https://github.com/ahmetozlu/signature_extractor/tree/feature-doc_scanner_sign_extrator/sample_project) that is developed on top of "signature extractor" algorithm to extract the signatures on the digital photo of the document. Here are the functionalities of this sample project:

- [Page dewarping - Perspective transformation](https://github.com/ahmetozlu/signature_extractor/blob/feature-doc_scanner_sign_extrator/sample_project/dewapper.py)
- [Signatre extraction](https://github.com/ahmetozlu/signature_extractor/blob/feature-doc_scanner_sign_extrator/sample_project/signature_extractor.py)
- [Unsharpening mask](https://github.com/ahmetozlu/signature_extractor/blob/feature-doc_scanner_sign_extrator/sample_project/unsharpen.py)
- [Color correction](https://github.com/ahmetozlu/signature_extractor/blob/feature-doc_scanner_sign_extrator/sample_project/color_correlation.py)

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/58769479-37e4f180-85b0-11e9-8822-c6521eb54781.gif" | width=450>
</p>

### Sample Test Results of Signature Extraction Algorithm

#### - Sample result#1:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47291471-73781000-d60c-11e8-9e5c-34699d91c73e.gif" | width=450>
</p>

**Explanation:** For this case, the signature extraction algorithm can extract the 3 different handwritten signatures successfully. Just a very small portion of the signature, which is located at top-left, is lost because this part is not connected with the whole signature line so the algorithm interprets it is not a part of the signature.

#### - Sample result#2:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47291680-36604d80-d60d-11e8-9a27-6870c6724b0e.gif" | width=450>
</p>

**Explanation:** For this case, signature extraction algorithm can extract 2 handwriteetn signatures from the whole textual data but it can not remove the lines, that are located at bottom-center, because the signature has big connected pixels so the algorithm sees them as signatures.

#### - Sample result#3:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47298403-5b11f080-d620-11e8-9590-a393aeecfe3f.gif" | width=450>
</p>

**Explanation:** Some parts of the signatures are lost because they are not connected with the big connected components so the algorithm sees that they are not a part of signatures. They can cathc by setting the threshold value to a bigger value.

## Theory

### Main pipe-line

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47617314-f00c6200-dad6-11e8-8ebf-c45a391b378b.jpg">
</p>

### Theoritical Background

As already mentioned that the algorithm can extract the signatures from scanned documents based on "connected component analysis" so what is connected component algorithm then?: In image processing, a connected components algorithm finds regions of connected pixels which have the same value!

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/48627013-850ec680-e9c4-11e8-9ef5-f692531dff1d.jpg">
</p>

You can find more detailed information about the connected component analysis in [here](https://homepages.inf.ed.ac.uk/rbf/HIPR2/label.htm).

Thus, the connected components can be found and labelled by a cool functionality that is provided by scikit-image library! But why do we need it? Please just check the scanned documents, you can see that the biggest connect components are belongs the handwritten signatures! If we can get the biggest connected components, we can get the signatures from whole documents! However, we can also get the undesired lines or different shapes that have big connected components, right? So we also need a threshold value to get rid of them...

### Calculating the threshold value to get rid of the outliars:

I've calculated the threshold value to detect the outliars (any lines, shapes and texts are not a part of the signatures) via performing many experiments. I've got an equation ,are calculated based experiement results, which are works pretty good for most of the scanned documents are a4 sized.

**Detect and remove the small size outliars:**

Here the code parts that start on [signature_extractor.py - line#60](https://github.com/ahmetozlu/signature_extractor/blob/master/signature_extractor.py#L60):

    # experimental-based ratio calculation, modify it for your cases
    # a4_small_size_outliar_constant is used as a threshold value to remove connected outliar connected pixels
    # are smaller than a4_small_size_outliar_constant for A4 size scanned documents
    a4_small_size_outliar_constant = ((average/constant_parameter_1)*constant_parameter_2)+constant_parameter_3
    print("a4_small_size_outliar_constant: " + str(a4_small_size_outliar_constant))

I determined the equation (x stands for scanned document size such as A4 or A0):

- ax_small_size_outliar_constant = ((average/*constant_parameter_1*) * *constant_parameter_2*) + *constant_parameter_3*

based full of my experiments. You can modify it for your cases and also the scanned document size such as for A0 and so on... Just configure the constants:

  - *constant_parameter_1*
  - *constant_parameter_2*
  - *constant_parameter_3*

perform many experiments with the different parameter values till get the highest accuracy!

**Detect and remove the big size outliars:**

Here the code parts that start on [signature_extractor.py - line#66](https://github.com/ahmetozlu/signature_extractor/blob/master/signature_extractor.py#L66):

    # experimental-based ratio calculation, modify it for your cases
    # a4_big_size_outliar_constant is used as a threshold value to remove outliar connected pixels
    # are bigger than a4_big_size_outliar_constant for A4 size scanned documents
    a4_big_size_outliar_constant = a4_small_size_outliar_constant*constant_parameter_4
    print("a4_big_size_outliar_constant: " + str(a4_big_size_outliar_constant))

I determined the equation (x stands for scanned document size such as A4 or A0):

- ax_big_size_outliar_constant = ax_small_size_outliar_constant*constant_parameter_4

based full of my experiments. You can modify it for your cases and also the scanned document size such as for A0 and so on... Just configure the constant:

  - *constant_parameter_4*
  
perform many experiments with the different parameter values till get the highest accuracy!


## Installation

**1.) Python and pip**

Python is automatically installed on Ubuntu. Take a moment to confirm (by issuing a python -V command) that one of the following Python versions is already installed on your system:

- Python 3.3+

The pip or pip3 package manager is usually installed on Ubuntu. Take a moment to confirm (by issuing a *pip -V* or *pip3 -V* command) that pip or pip3 is installed. We strongly recommend version 8.1 or higher of pip or pip3. If Version 8.1 or later is not installed, issue the following command, which will either install or upgrade to the latest pip version:

    $ sudo apt-get install python3-pip python3-dev # for Python 3.n
    
**2.) scikit-image**

On all other systems, install it via shell/command prompt:

    pip install scikit-image

If you are running Anaconda or miniconda, use:

    conda install -c conda-forge scikit-image

See details in [here](http://scikit-image.org/docs/dev/install.html).

---
- After completing these 2 installation steps that are given at above, you can test the project by this command:

      python3 signature_extractor.py
---

## Citation
If you use this code for your publications, please cite it as:

    @ONLINE{hse,
        author = "Ahmet Özlü",
        title  = "Overlapped handwritten signature extraction from scanned documents",
        year   = "2018",
        url    = "https://github.com/ahmetozlu/signature_extractor"
    }

## Author
Ahmet Özlü

## License
This system is available under the MIT license. See the LICENSE file for more info.
