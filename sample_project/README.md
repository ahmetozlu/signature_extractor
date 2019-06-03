# A Real-life Application of Signature Extraction Algorithm

A real-life sample project which built on top of "[signature_extraction](https://github.com/ahmetozlu/signature_extractor/blob/master/signature_extractor.py)" algorithm to extract the signatures on the digital photo of the document. This project project provides a basic document scanner and signature extractor!

Here are the functionalities of this sample project:

- [Page dewarping - Perspective transformation](https://github.com/ahmetozlu/signature_extractor/blob/master/sample_project/dewapper.py)
- [Signatre extraction](https://github.com/ahmetozlu/signature_extractor/blob/master/sample_project/signature_extractor.py)
- [Unsharpening mask](https://github.com/ahmetozlu/signature_extractor/blob/master/sample_project/unsharpen.py)
- [Color correction](https://github.com/ahmetozlu/signature_extractor/blob/master/sample_project/color_correlation.py)

## Quick Demo 

---

- Input = The digital photo of the document
- Output = The signatures exist on the input

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/58767686-d9137e00-8597-11e9-9921-1bf8204ab451.jpg" | width=750>
</p>

---

### Sample Test Results

#### - Sample result#1:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/58769479-37e4f180-85b0-11e9-8822-c6521eb54781.gif" | width=450>
</p>

**Explanation:** Fristly, the page dewarping algorithm is performed to warp the page properly. And then, signature extraction algorithm is performed to extract the signature on the image. Lastly, unsharpening mask and color correction algortihms are performed to make the documents quality high!

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
