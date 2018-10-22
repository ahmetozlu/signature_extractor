## "Signature Extraction" Algorithm based connected component analysis

A design and implementation for "overlapped handwritten signature extraction from scanned documents" using OpenCV and scikit-image on python.

### 1.) Quick Demo 

- Input = The scanned document
- Output = The signatures exist on the input (scanned document)

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47317435-38003480-d652-11e8-87be-0d93ea9e119a.png" | width=750>
</p>


#### Sample result#1:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47291471-73781000-d60c-11e8-9e5c-34699d91c73e.gif" | width=450>
</p>

**Explanation:** For this case, the signature extraction algorithm can extract the 3 different handwritten signatures successfully. Just a very small portion of the signature, which is located at top-left, is lost because this part is not connected with the whole signature line so the algorithm interprets it is not a part of the signature.

#### Sample result#2:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47291680-36604d80-d60d-11e8-9a27-6870c6724b0e.gif" | width=450>
</p>

**Explanation:** For this case, signature extraction algorithm can extract 2 handwriteetn signatures from the whole textual data but it can not remove the lines, that are located at bottom-center, because the signature has big connected pixels so the algorithm sees them as signatures.

#### Sample result#3:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47298403-5b11f080-d620-11e8-9590-a393aeecfe3f.gif" | width=450>
</p>

**Explanation:** Some parts of the signatures are lost because they are not connected with the big connected components so the algorithm sees that they are not a part of signatures. They can cathc by setting the threshold value to a bigger value.

### 2.) Theory
As already mentioned that the algorithm can extract the signatures from scanned documents based on "connected component analysis" so what is connected component algorithm then?: In image processing, a connected components algorithm finds regions of connected pixels which have the same value!

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/47317877-4733b200-d653-11e8-97d9-ba80248c24d0.png" | width=450>
</p>
taken from [here](https://slideplayer.com/slide/4593148/15/images/67/Extraction+of+connected+components.jpg).

Thus, the connected components can be found and labelled by a cool functionality that is provided by scikit-image library! But why do we need it? Please just check the scanned documents, you can see that the biggest connect components are belongs the handwritten signatures! If we can get the biggest connected components, we can get the signatures from whole documents! However, we can also get the undesired lines or different shapes that have big connected components, right? So we also need a threshold value to get rid of them...






