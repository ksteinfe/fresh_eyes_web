---
title: SG 2018 Workshop Explorations
subtitle: Applying Machine Learning to Generative Architectural Design
attribution: Prepared by Adam Menges, Lobe.ai; Kat Park, SOM; Kyle Steinfeld, UC Berkeley; Samantha Walker, SOM; Antoine Maes; Gabriel Payant; Timothy Logan; Ben Coorey; Nonna Shabanova; Sebastian Misiurek; Jenny Zhu; Marantha Dawkins; James Forren; Jenessa Man;
copyright: Copyright &copy; 2018 Adam Menges, Kat Park, Kyle Steinfeld, and Samantha Walker, Antoine Maes, Gabriel Payant, Timothy Logan, Ben Coorey, Nonna Shabanova, Sebastian Misiurek, Jenny Zhu, Marantha Dawkins, James Forren; Jenessa Man
---

[[section|slide]]

Over the course of this workshop, participants trained purpose-built image-based ML models to evaluate candidate design solutions based on a variety of tacit and heretofore un-encapsulatable design criteria, such as architectural style, spatial experience, or typological features. Participants then deployed these models to the cloud, and integrate them into functional generative design systems via API calls. During the workshop, we also deployed iterations of GAN (Generative Adversarial Network) using our datasets, which produced new designs and perspective into how the machine sees the datasets we were offering.

[[section|slide]]

## House GAN

Complex machinations and plays of power between two competing ML allows for the generation of credible house types through 2D representation of their geometry. Generative Adversarial Networks (GAN) work in tandem with one network forging its best impression of a credible image and the other vetoing it as obviously fake or credible. Through the countless iterations of this process, each network hones its generative and detection skills.

Using the house training set, we ran iterations of GAN to have the machine generate its own versions of what it thinks is a house. The houses might not be meaningful or occupiable in the eyes of a practical critic, but the machine generating its own versions of data is significant in the design process as it can open up hidden solutions that have not been unearthed in human exploration of solutions. 

![vid||loop controls muted](http://git-to-s3-fresheyes-images.s3-website-us-east-1.amazonaws.com/houseGAN r01 Walk 17000.mp4 "Houses generated by GAN")

[[section]]

-

# Insider View: A 3D visualization of what a critic sees - Gabriel Payant, Antoine Maes & Timothy Logan
<!-------------------- -------------------->

As architectural designers, many files we work with are representations of the design, not the design artifact itself. When exploring ML based image recognition, we are challenged with the conversion of 3D information (as architectural design happens most often in 3D) to 2D information (as computer vision ML works with 2D images). The 3D representation of the design form had been converted into a series of 2D images (sections, elevations, isovists, etc), which make up the dataset that are fed as examples into the ML model. We still craved to visualize the series of 2D images in 3D, especially when the GAN generated its own versions of what a design form would be. Here, we created tools to approximate and synthesize 3D forms from the series of 2D images typical in a training dataset.

[[section|slide]]

### What the Critic Sees in 3D

Current ML technology relies heavily on cumulative advancements in image recognition. Therefore, training an ML model to act as an architectural critic involves shifting the digital 3D representation designers use to synthetic 2D image. Once the ML starts its process, the intelligible 3D model is not updated to show the transformation the architectural artifact is undergoing. We investigated the potential for reverse engineering the process that generates the 2D depth map in order to provide the designer with an "insider view" of what is going on under the hood, thus expanding the possible interactions between actor, critic and designer.

[[section|slide]]

#### VOXEL SPACE

A voxel space of a resolution equal to the square of the one used to represent a single elevation in the 2d image was mapped. Each face of every voxel was then evaluated to the corresponding elevation for its depth value by first checking for very dark pixels and causing the block to turn off, then by validating if the threshold for turning on was reached by the brightest value, for each block towards the source until was reach.

![vid||loop controls muted](http://git-to-s3-fresheyes-images.s3-website-us-east-1.amazonaws.com/AntGabTim_Voxel_Anim_600.gif " ")

[[section|slide]]

#### MAPPED POINTS

A 2D grid was generated for each view given by the ML. They were then placed in such a way as to provide a cube of possible position. Each pixel was then pushed from its originating plan to the depth given by the 2D image.

![vid||loop controls muted](http://git-to-s3-fresheyes-images.s3-website-us-east-1.amazonaws.com/AntGabTim_vid1.gif " ")

[[section|slide]]

We then used two different strategies to turn these points back into masses. The first involved creating a mesh around previously filtered points based on a charge given to each of them using the Cocoon plug-in.

![vid||loop controls muted](http://git-to-s3-fresheyes-images.s3-website-us-east-1.amazonaws.com/SaltboxClark10.gif " ")


[[section|slide]]

The second strategy was to determine a linear boundary for each Z level associated with each vertical pixel of the ML elevation and then extrude them by a distance equal to height of the pixel is standing for.

![vid||loop controls muted](http://git-to-s3-fresheyes-images.s3-website-us-east-1.amazonaws.com/PointstoBoxes.gif " ")

[[section|slide]]

We then applied the different strategies to different models of our dataset, both generated by the ML and translated from preexisting 3D models to 2D image in order to have a intelligible 3D representation of the artifacts.

![fig|wide](img/explorations/Images_trainer.jpg "Representing what the critic sees in 3D")

[[section|slide]]

Using the tool we developed in Insider View, we then converted back those generated 2D representation of houses into a 3D model that was subsequently 3D printed allowing us to evaluate visually the credibility of the houses.

![fig|wide](img/explorations/Images_Gan.jpg "3D visualization of the 2D images generated by House GAN")

[[section|slide]]

As a complementary test, we then sent the generated 2D images to a ML critic that was trained using the same dataset as the GAN, but with the goal of discerning house types. We then gathered the prediction given by the critic as another human intelligible way of peeking into how ML "sees" data.

![fig|wide](img/explorations/3DLobeSC.png "Asking ML Critic to classify a GAN generated house")

[[section]]

-

# Embodying the Intangible: a Machine Intelligence Trained to Recognize Experiential Quality of a Space - Sebastian Misiurek & Jenny Zhu
<!-------------------- -------------------->

[[section|slide]]

We generated 3D models of various spatial volumes in relation to a human occupant, and trained a machine learning model to classify the various spatial volumes such as Box, Vault, Dome, etc.  To translate these objective volume types to a more qualitative description of a space, we will be using 2 ML (a minor and a major).  Once an ML is trained to classify the volume types, it can be fed to another layer of training where a combination of the volume types can mean an experiential quality.

### Dataset of Volume Types

![fig|wide](img/explorations/SpatialExperience_Form_Isovit.gif "A human occupant's isovist view of volume types")

[[section|slide]]

### ML Model Being Trained in Lobe

![fig|wide](img/explorations/SpatialExperience_lobe-vaults.png " ")

[[section|slide]]

### Definition of Experiential Qualities of a Space

Experiential Categories:
Spatial Openness allows for varying levels of comfort based on amount of peripheral space (side to side). Spatial Mobility allows for varying levels of movement based on frontal space (front to back). Spatial Grandeur allows for varying levels of awe based on overhead space (top to bottom)


![fig|wide](img/explorations/SpatialExperienceDiagram_800x600.png " ")

[[section]]

-

# Grove : James Forren
<!-------------------- -------------------->

[[section|slide]]

Grove compares different ideas about trees and how a machine learning model can be used to mimic an idea of "forest."  This is intended to test the way a machine learning model can be used to train architectural proposals to match an idealized image or experience.  A set of ideal forest types, alder, elm, tall conifer - are used to train a forest critic.  The critic, in turn, discerns from a series of forest proposals from a generative actor to find the shape and pattern which best satisfies the criteria of elm, tall coniferous, etc.  The process uses an isovist critic and actor, evaluating the forests perspectivally. 

![fig|wide](img/explorations/Grove_Trainer Compiled.jpg "Forest types as training set")

[[section|slide]]

### Isovist View of a Forest Type

![fig|wide](img/explorations/Grove-01_Isovist.gif " ")

[[section|slide]]

![vid||loop controls muted](http://git-to-s3-fresheyes-images.s3-website-us-east-1.amazonaws.com/Grove_TreeRun01.gif "Ideal forest types")

This initial study was not successful in developing a working optimization model.  What was learned is the significance of the type and quality of data provided to the machine learning model.  In this case our hypothesis is that the isovist trainer needed more trees closer to its position, a deeper tonal range in the generated images, and greater variety in the idealised tree types.

[[section]]

-

# Pix2Pix for Architectural Styles and Forms : Jenessa Man
<!-------------------- -------------------->

[[section|slide]]

Pix2Pix (image to image translation) models were generated for various architectural styles and forms, including:
- Art Deco, Achaemenid, Post Modern, American Craftsman and Chicago School styles
- "Evil buildings", buildings perceived to epitomize evilness or scariness (see r/evilbuildings)
- Bridges

Training datasets were collected from Reddit, Arup and various academic institutions, including the Shanghai Jiao Tong University and University of Toronto.

An interactive demo for the models will be posted soon.

[[section|slide]]

![fig|wide](img/explorations/pix2pix_edges2architecture.jpg " ")

[[section|slide]]

### Architectural Style GANs
DCGANs (Deep Convolutional Generative Adversarial Networks) were generated for various architectural styles, including:
-    Achaemenid architecture, American craftsman style, American Foursquare architecture, Ancient Egyptian architecture, Art Deco architecture, Art Nouveau architecture, Baroque architecture, Bauhaus architecture, Beaux-Arts architecture, Byzantine architecture, Chicago school architecture, Colonial architecture, Deconstructivism, Edwardian architecture, Georgian architecture, Gothic architecture, Greek Revival architecture, International style, Novelty architecture, Palladian architecture, Postmodern architecture, Queen Anne architecture, Romanesque architecture, Russian Revival architecture and Tudor Revival architecture

Training datasets were collected from Reddit, Arup and various academic institutions, including the Shanghai Jiao Tong University and University of Toronto.

Samples of the generated images will available soon.

[[section]]

-

# Artificial Generation of Floor Plans : Ben Coorey & Nonna Shabanova
<!-------------------- -------------------->

[[section]]

Armed with a large dataset of consistent residential floor plans with a decent level of consistency, this team annotated the floor plans with features and trained an ML model to recognize various features on a residential floor plan, such as doors, windowns, etc).   

[[section|slide]]

#### Detect Features

We trained a Convolutional Neural Network to detect the key elements of an apartment that provide the minimal information for the computer to describe the structure of an apartment. The trained model identifies windows and doors from images of floor plans, which are constructed into a network graph using parametric tools.

![fig|wide](img/explorations/01_FP_Detection.png "Plans")

![fig|wide](img/explorations/05_FP_Diagrammatic Representation.png "Plan features to Network Graph")

[[section|slide]]

#### Represent Floor Plans as a Network Graph

 Each network graph (new representation of floor plans) was then classified by shape and style of windows / ventilation strategy such as Wrap Around, Corner, Complex, Single Aspect, Cross-Through. A ML model trained to classify these various types is well-suited to unearth hidden relationships between such patterns and the designed space.

![fig|wide](img/explorations/04_FP_images.png "Network graphs")

[[section|slide]]

#### Classify Floor Plans
Each floor plan was allocated into types which were then trained into a predictive AI model to implement a workflow that can detect features from an image of a floor plan, and then determine the type of floor plan automatically.

![fig|wide](img/explorations/02_FP_Classification.png "Classification")

[[section|slide]]

#### Generate New Floor Plans
Experimentation with Generative Adversarial Networks that are trained on a library of floor plans, which then allow the computer to generate populations of novel unique floor plans from scratch.

![fig|wide](img/explorations/03_FP_Generation.png "New floor plans generated by GAN")

[[section]]

-

# Shaping Tall Buildings for Wind Effects : Samantha Walker & Marantha Dawkins
<!-------------------- -------------------->

[[section|slide]]

### Training the Critic

A building's shape is the most influential factor in mitigating wind effects. Using results from tests that were performed at SOM's wind tunnel in Chicago, the WT 260, an ML model is trained to assess the behavior of tall buildings under wind loads based on building shape and orientation. For the purposes of training the ML model, this data has been interpreted and organized into five different qualitative categories of behavior under wind loads: bad, fair, moderate, good and excellent.

![fig|wide](img/explorations/SOM-slice.jpg "Training set")

[[section|slide]]

### A Study of Actors

A variety of different actors were employed to study different ways of shaping buildings for wind effects utilizing the trained ML critic.

![fig|wide](img/explorations/optimization-modelSlice-updated.jpg "ML optimization towards excellent shapes for wind effects using different actors")

[[section|slide]]

### Voxelized Actor

A first actor was designed as a voxelized mass. The optimizer was allowed to expand and contract the voxels in plan and elevation within certain limits. Optimization for excellent shapes to mitigate wind effects tended towards stepped and L-shaped forms.
 
![vid||loop controls muted](https://berkeley.box.com/shared/static/jxeedyh0xpi2ver4udgvnw7z98a9to8p.mp4 "Voxelized mass - optimizing towards excellent shapes for wind effects")

[[section|slide]]

### Sectional Actor

A second actor was designed to generate sectional variation. Optimizations for excellent shapes to mitigate wind effects tended towards top-heavy, bulging forms.

![fig|wide](img/explorations/sectionalVariation2.gif "Sectional mass - optimizing towards excellent shapes for wind effects")

[[section|slide]]

### Critics in Agreement: Figurative and Performative Optimization

The wind ML model is put in conversation with a ML model trained both to recognize fish and reject normative actor-generated solutions for optimal shapes for wind effects. The combined optimization works towards designs which both reduce wind loads and have the elevation of a fish. 

![fig|wide](img/explorations/fishTraining-2.gif "Sectional mass - optimization for wind effects and fish resemblance")
