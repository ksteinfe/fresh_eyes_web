---
title: SG 2018 Workshop Explorations
subtitle: Applying Machine Learning to Generative Architectural Design
attribution: Prepared by Adam Menges, Lobe.ai; Kat Park, SOM; Kyle Steinfeld, UC Berkeley; Samantha Walker, SOM; List all participants here
copyright: Copyright &copy; 2018 Adam Menges, Kat Park, Kyle Steinfeld, and Samantha Walker, and all participants
---

This workshop cluster, a part of the [2018 Smart Geometry Conference](https://www.smartgeometry.org/sg18/) hosted by the [University of Toronto](https://www.daniels.utoronto.ca/), brings recent developments in machine learning (ML) to bear on generative architectural design. To improve the utility of artificial intelligence as a creative partner for design, we have brought together experts from architectural design practice, ML engineering, and design methods research. 

[[section|slide]]

Here we report on the results of research conducted, and describe methods for the incorporation of user-generated image-based ML recognition models into the evaluation step of a traditional generative design workflow.

[[section|slide]]

This project uniquely links the familiar parametric environment of Grasshopper with cloud-hosted models trained using Lobe.ai: a user-friendly ML graphic programming environment that runs Tensorflow.

![fig|limit](img/index/lobe sreenshot.png "Screenshot of Lobe.ai")

[[section]]
Over the course of this workshop, participants train purpose-built image-based ML models to evaluate candidate design solutions based on a variety of tacit and heretofore un-encapsulatable design criteria, such as architectural style, spatial experience, or typological features. Participants then deploy these models to the cloud, and integrate them into functional generative design systems via API calls.

[[section|slide]]
### Feauture Recognition in Architectural Plans 
[[section]]
Ben Coorey, Nonna Shabanova

Dataset: Annotated architectural plans formatted for real-estate and trained a model to recognize various features (doors, windows, etc) on a plan.

[[section|slide]]
#### Subsection

[[section]]

some text

[[section|slide]]
#### Shaping Tall Buildings for Wind Performance

[[section]]

An ML model is trained to assess the performance of tall buildings under wind loads based on building shape and orientation. This dataset is created using results from tests that were performed at SOM's wind tunnel in Chicago, the WT 260. Massing models at a 1:500 scale are positioned at the back of the wind tunnel on a load cell that measures different parameters such as frequency, displacement and forces. For the purposes of training the ML model, this data has been interpreted and organized into five different qualitative categories of wind performance: bad, fair, moderate, good and excellent. A building's shape is the most influential factor in mitigating wind effects. This ML model is deployed in the service of helping designers to better shape buildings for wind loads and potentially offering new ideas to improve their performance.

# James Forren
<!-------------------- -------------------->

To maintain focus on the evaluation of candidate designs using ML models, technologies necessary for a rudimentary generative design workflow have been prepared in advance of the workshop and are quickly introduced to participants.

[[section|slide]]

We understand the generative design workflow to consist of:

[[section|slide]]

A design schema capable of generating new design options based on a limited set of variables. 

We call the production of new designs ***the actor***.

[[section|slide]]

A means of discerning more desirable options from less desirable ones, and which may be employed to evaluate options produced the actor. 

We term this process ***the critic***.

[[section|slide]]

A means of creating variations, and of navigating the space of possible designs, as defined by the actor, in search of better performing solutions, as understood by the critic. 

This iterative process is ***an optimization***. 

[[section]]

## Technical Overview of the Basic Workflow

We establish a workflow that allows us to focus on the unique contribution of the cluster: the development of methods for the integration of ML evaluation routines into a parametric environment. To proceed as a generative design workflow, the three basic concerns outlined above must be addressed. As an overview of the software involved, these are addressed as such:

[[section|slide]]

***We define an "actor"*** as a parametric model in Grasshopper able to generate of candidate design solutions. 

[[section]]

This approach fits easily into the common skill-set of most digitally-motivated architects, and we expect workshop participants arrive with basic parametric modeling skills.

[[section|slide]]

***We train a "critic"*** as a machine learning model capable of appropriate architectural evaluation. 

[[section]]

Here is where much of the work of the cluster lies. Here we must establish training datasets via a variety of methods (some of which require scripting in Python), train image-based models using Tensorflow, host these models on cloud servers dedicated to this purpose, and establish structures to call upon them using an application program interface (API). In support of this workflow, we have partnered with Lobe.ai, a visual programming language for creating neural networks. Using the Grasshopper-like graphical programming environment provided by Lobe, workshop participants are able to design a model, use a pre-trained one, and receive predictions from the cloud.

[[section|slide]]

***We orchestrate an "optimization"***, using existing optimization plugins for Grasshopper.

[[section]]

By pitting actor against critic, using existing tools such as Galapagos, Opossum or similar, the space of possible designs (defined by the actor) is iteratively explored in order to identify the best performing solutions (in the eyes of the critic). To this end, a toolset has been established that supports the integration of a trained and hosted ML model into a general generative design workflow. A set of components in Grasshopper are provided that construct API calls to the hosted model, receive results, and processes this information into Grasshopper compatible data. 

# Ben Coorey & Nonna Shabanova
<!-------------------- -------------------->

[[section|slide]]

Here, we describe a rudimentary example that illustrates the basic workflow outlined above, and demonstrates the utility of the integration of ML evaluation routines in a parametric environment.

[[section]]

As we discuss below, certain problems arise with the conversion of three-dimensional information, as is so often employed in the production of architectural work, to two-dimensional information, as is required by the particular models of ML based on image recognition that we are exploring here. To isolate these problems, this first example operates in a purely two-dimensional fashion.

## Training the Critic

[[section|slide]]

We begin with the training of a critic. 

For this purpose, an existing training set was identified that appeared to adopt a format amenable to the methods adopted by the cluster, and suggested a classification of form that was both diverse and immediately recognizable. 

[[section|slide]]

[A dataset of 990 binary images of leaf silhouettes](https://github.com/WenjinTao/Leaf-Classification--Kaggle), organized by species, was identified and converted into standard JPG images.

![scroll|500|800|200|20](img/index/families.gif "10 samples of silhouetted leaf images taken from 99 species of tree.")

[[section]]

### An Initial Critc

An initial set of ML models were trained on this dataset of 9,900 images organized into 99 categories of 10 samples each. A number of image resolution were tested: 20px, 50px, 100px, and 200px. 

After training was complete, we found two problems.

First, the accuracy of our models, which varied from 58% for the 20px images to 73% for the 200px images were not satisfactory. 

Second, the given organization of the leaf shapes left something to be desired from a design point of view.

### A Revised Critic

As we were interested in encapsulating the the formal characteristics of leaf forms, and not in identifying leafs in terms of the species of tree to which they belong, the existing structure of this dataset did not quite suit our ends.

[[section|slide]]

Adapting this dataset, eight new categories of form were established:
* almond
* fan
* heart
* jagged
* lobed
* long
* star
* wide

![vid|slide|loop controls muted](https://berkeley.box.com/shared/static/eourvtznud8tqgb9r7mpplijb25i4v1p.mp4 "Eight categories of leaf shape were established, and the 990 samples were re-organized according to this new ontology of form.")

[[section]]

A second model was then trained on this re-organized dataset of leaf shapes.

After training was complete, the model presented an accuracy of 81%.

## Defining the Actor

### Blackblob

### Metaball

### Metaspike

## Orchestrating an Optimization



