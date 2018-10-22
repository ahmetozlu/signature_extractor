# "Signature Extraction" Algorithm based connected component analysis

A design and implementation for "overlapped handwritten signature extraction from scanned documents" using OpenCV and scikit-image on python.

## 1.) Quick Demo 

### Sample result#1:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47291471-73781000-d60c-11e8-9e5c-34699d91c73e.gif" | width=450>
</p>

**Explanation:** For this case, the signature extraction algorithm can extract the 3 different handwritten signatures successfully. Just a very small portion of the signature, which is located at top-left, is lost because this part is not connected with the whole signature line so the algorithm interprets it is not a part of the signature.

### Sample result#2:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47291680-36604d80-d60d-11e8-9a27-6870c6724b0e.gif" | width=450>
</p>

**Explanation:** For this case, signature extraction algorithm can extract 2 handwriteetn signatures from the whole textual data but it can not remove the lines, that are located at bottom-center, because the signature has big connected pixels so the algorithm sees them as signatures.

### Sample result#2:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47298403-5b11f080-d620-11e8-9590-a393aeecfe3f.gif" | width=450>
</p>

**Explanation:**
