# "Signature Extraction" based connected component analysis

A design and implementation of a super lightweight algorithm for "overlapped handwritten signature extraction from scanned documents" using OpenCV and scikit-image on python.

## Quick Demo 

---

- Input = The scanned document
- Output = The signatures exist on the input

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/58767686-d9137e00-8597-11e9-9921-1bf8204ab451.jpg" | width=750>
</p>

**TODOs:**

- "Page dewarpper" module will be developed.
- "Unsharp Masking" module will be developed.
- "Color Correction" module will bedeveloped.
- "Perspective Transformation" module will be developed.
- "Outliar Removal" module will be developed to improve the signature extraction algorithm.
- CNN based "Signature Recognition" module will be developed.
- "Signature Spoofing Detection" algorithm will be developed.

---


### Sample Test Results

#### - Sample result#1:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/58767618-cea4b480-8596-11e9-9723-a4a07cc3bf42.gif" | width=450>
</p>

**Explanation:** For this case, the signature extraction algorithm can extract the 3 different handwritten signatures successfully. Just a very small portion of the signature, which is located at top-left, is lost because this part is not connected with the whole signature line so the algorithm interprets it is not a part of the signature.

## Theory

### Main pipe-line

Main pipe-line of this sample project is given below!

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/58767599-6b1a8700-8596-11e9-97ec-c0c05ddef455.jpg">
</p>

The signature extractor architecture already explain in the main repo [readme]() and the architecture of the signature extractor is given below!

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47617314-f00c6200-dad6-11e8-8ebf-c45a391b378b.jpg">
</p>

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
