---
title: Fresh Eyes
subtitle: Applying Machine Learning to Generative Architectural Design
attribution: Prepared by Adam Menges, Lobe.ai; Kat Park, SOM; Kyle Steinfeld, UC Berkeley; Samantha Walker, SOM
copyright: Copyright &copy; 2018 Adam Menges, Kat Park, Kyle Steinfeld, and Samantha Walker
---

# Aim

This cluster brings recent developments in machine learning (ML) to bear on generative architectural design. To improve the utility of artificial intelligence as a creative partner for design, we have brought together experts from architectural design practice, ML engineering, and design methods research, and have developed methods for the incorporation of user-generated image-based ML recognition models into the evaluation step of a traditional generative design workflow. While existing research ((For a survey of [existing ML-related plugins](link.html "a title") for Grasshopper, see the relevant Appendix below.)) has integrated low-level ML operations into the parametric design environment with a level of success, this proposal uniquely links the familiar environment of Grasshopper with cloud-hosted models trained using the high-level and relatively user-friendly Tensorflow framework. Over the course of this workshop, participants will [^](My old college roommate) train purpose-built image-based models to evaluate candidate design solutions based on a variety of tacit and heretofore un-encapsulatable design criteria of their choosing, such as architectural style, spatial experience, or typological features. Participants will then deploy these models to the cloud, and integrate them into functional generative design systems via API calls.

((Let's try this))

The integration of an ML evaluation step into a generative design workflow opens up a range of possible design scenarios. While the definition of specific studies will be left to the discretion of workshop participants, a number of potential studies are listed here. This abbreviated list was compiled both to illustrate the new opportunities brought about by ML, and to demonstrate the breadth of potential applications implied by our approach to the subject.

# Methods

To maintain focus on the evaluation of candidate designs using ML models, technologies necessary for a rudimentary generative design workflow - understood as outlined below - will be prepared in advance of the workshop and quickly introduced to participants.

1. Generate 
2. Evaluate  
3. Iterate 

The generation of candidate design solutions will be defined as a parametric model in Grasshopper. The iteration step - exploring the space of possible solutions to find best performing options - will be handled using existing plugins (such as Galapagos or similar). With these standard pieces in place, we may focus on the unique contribution of the cluster: developing methods for the integration of ML evaluation routines into a parametric environment. These methods must address two basic concerns: training appropriate ML models, and calling upon these models to evaluate candidate design solutions.

Regarding the first concern, we will assist participants to establish training datasets, train image-based models using Tensorflow and Lobe.ai, host these models on cloud servers dedicated to this purpose, and establish structures to call upon them using an application program interface (API). For this purpose, we have partnered with Lobe.ai, a visual programming language for creating neural networks. Using the Grasshopper-like graphical programming environment provided by Lobe, workshop participants will be able to design a model, use a pre-trained one, and receive predictions from the cloud. Regarding the second concern, a toolset will be established in advance of the workshop that supports the integration of a trained and hosted ML model into a general generative design workflow. A component in Grasshopper will be provided that constructs API calls to the hosted model, and then receives and processes the results. This process is further elaborated below.
The following lists describe the prerequisites for participation in the workshop, outline the resources and tools that will be provided to participants, and account for the methods that will be developed and tested over the course of the workshop. A clear workshop schedule may be found in Appendix A.

Participants in this workshop will be expected to arrive with:

* A basic competency in parametric modeling in Grasshopper and/or scripting in Python.
* Experience in generative design, preferably using Grasshopper for design generation and one of a number of optimization tools (Galapagos, Octopus, or similar) for iteration.

Prior to the start of the workshop, the cluster organizers will provide participants with:
* Grasshopper components for interacting via API calls with a cloud-hosted ML model. These components will take in image data, perform the API call to the model, receive a response, and translate results into GH data.
* A suite of tools written in Python to assist students in establishing training sets of tagged images. This may include web scraping tools for exploring online datasets such as Instagram or Pinterest, as well as automated image processing tools for preparing large collections of images for training.

Over the course of the workshop, we will introduce methods for and competencies in:
* Establishing training sets for ML models, including collecting datasets via web scraping
* Training and testing ML models in Tensorflow
* Hosting trained models and establishing API protocols


[I'm an inline-style link to the error page with title](error.html "a link title")

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")


i am a definition list on a slide




[[section|title slide]] I am a section title slide? [[section]]

i am some stuff not on a slide

[[section|slide]] i am on a slide! [[section]]

i shoudn't be on a slide, but okay.

[[section]]

okay

[[section|slide]]

i am something on a slide


[[section|title slide]] I am a section title slide? [[section]]

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

[[section]]

i am some stuff not on a slide

