---
title: SG 2018 Workshop Explorations
subtitle: Applying Machine Learning to Generative Architectural Design
attribution: Prepared by Adam Menges, Lobe.ai; Kat Park, SOM; Kyle Steinfeld, UC Berkeley; Samantha Walker, SOM; List all participants here
copyright: Copyright &copy; 2018 Adam Menges, Kat Park, Kyle Steinfeld, and Samantha Walker, and all participants
---

[[section|slide]]

Over the course of this workshop, participants train purpose-built image-based ML models to evaluate candidate design solutions based on a variety of tacit and heretofore un-encapsulatable design criteria, such as architectural style, spatial experience, or typological features. Participants then deploy these models to the cloud, and integrate them into functional generative design systems via API calls.

[[section|slide]]

# House GAN and What the Critic Sees in 3D: Gabriel Payant, Antoine Maes & Timothy Logan
<!-------------------- -------------------->

[[section]]

#### What the Critic Sees in 3D

As we discuss below, certain problems arise with the conversion of three-dimensional information, as is so often employed in the production of architectural work, to two-dimensional information, as is required by the particular models of ML based on image recognition that we are exploring here. To isolate these problems, this first example operates in a purely two-dimensional fashion.

[[section|slide]]

![vid|slide|loop controls muted](https://berkeley.box.com/shared/static/6ulwochbi1m0f1576s71wqefdc2ox0ey.gif "Transforming 2D to 3D")

![vid|slide|loop controls muted](https://berkeley.box.com/shared/static/uwhgkg9y468tykpsjctw2hrqe1unuw4g.gif "Transforming 2D to 3D via Voxel")

![fig|wide](img/explorations/Images_trainer.jpg "Representing what the critic sees in 3D")

[[section]]

#### House GAN

Using the house training set, we tried running GAN (Generative Adversarial Networks) to have the machine generate its own versions of the categories of houses.  The houses might not be meaningful or occupiable in the eyes of a practical critic, but the machine generating its own versions of data is significant in the design process as it can open up hidden solutions that have not been unearthed in a human exploration of solutions. 

[[section|slide]]

![fig|wide](img/explorations/Images_Gan.jpg "House GAN")

[[section|slide]]

# Grove : James Forren
<!-------------------- -------------------->
[[section]]

Grove compares different ideas about trees and how a machine learning model can be used to mimic an idea of "forest."  This is intended to test the way a machine learning model can be used to train architectural proposals to match an idealized image or experience.  A set of ideal forest types, alder, elm, tall conifer - are used to train a forest critic.  The critic, in turn, discerns from a series of forest proposals from a generative actor to find the shape and pattern which best satisfies the criteria of elm, tall coniferous, etc.  The process uses an isovist critic and actor, evaluating the forests perspectivally. 

[[section|slide]]

![fig|wide](img/explorations/Grove_Trainer Compiled.jpg "Trainer")


#### Heading

 This initial study was not successful in developing a working optimization model.  What was learned is the significance of the type and quality of data provided to the machine learning model.  In this case our hypothesis is that the isovist trainer needed more trees closer to its position, a deeper tonal range in the generated images, and greater variety in the idealised tree types.
 
 ![fig|wide](img/explorations/Grove-01_Isovist.gif "Isovist")

 ![vid|slide|loop controls muted](https://berkeley.box.com/shared/static/xt32pn8zhjg0azdwomsaec6vf2ij0di4.gif "")

# Artificial Generation of Floor Plans : Ben Coorey & Nonna Shabanova
<!-------------------- -------------------->
[[section|slide]]
Armed with a large dataset of consistent residential floor plans with a decent level of consistency, this team annotated the floor plans with features and trained an ML model to recognize various features on a residential floor plan, such as doors, windowns, etc).   


#### Detect Features

We trained a Convolutional Neural Network to detect the key elements of an apartment that provide the minimal information for the computer to describe the structure of an apartment. The trained model identifies windows and doors from images of floor plans, which are constructed into a network graph using parametric tools.

![fig|wide](img/explorations/01_FP_Detection.png "plans")


#### Represent Floor Plans as a Network Graph

 Each network graph (new representation of floor plans) was then classified by shape and style of windows / ventilation strategy such as Wrap Around, Corner, Complex, Single Aspect, Cross-Through. A ML model trained to classify these various types is well-suited to unearth hidden relationships between such patterns and the designed space.

![fig|wide](img/explorations/04_floorplan_images.PNG "network graphs")


#### Classify Floor Plans
Each floor plan was allocated into types which were then trained into a predictive AI model to implement a workflow that can detect features from an image of a floor plan, and then determine the type of floor plan automatically.

![fig|wide](img/explorations/02_FP_Classification.png "classification")


#### Generate New Floor Plans
Experimentation with Generative Adversarial Networks that are trained on a library of floor plans, which then allow the computer to generate populations of novel unique floor plans from scratch.

![fig|wide](img/explorations/03_FP_Generation.png "new floor plans generated by GAN")


# Shaping Tall Buildings for Wind Effects : Samantha Walker & Marantha Dawkins
<!-------------------- -------------------->
[[section|slide]]

## Training the Critic

[[section]]

A building's shape is the most influential factor in mitigating wind effects. Using results from tests that were performed at SOM's wind tunnel in Chicago, the WT 260, an ML model is trained to assess the performance of tall buildings under wind loads based on building shape and orientation. Massing models at a 1:500 scale are positioned at the back of the wind tunnel on a load cell that measures different parameters such as frequency, displacement and forces. For the purposes of training the ML model, this data has been interpreted and organized into five different qualitative categories of wind performance: bad, fair, moderate, good and excellent. 

[[section|slide]]

![fig|wide](img/explorations/SOM-slice.jpg "Training set")

[[section|slide]]

### Voxelized Actor

[[section]]

text

[[section|slide]]

![vid|slide|loop controls muted](https://berkeley.box.com/shared/static/jxeedyh0xpi2ver4udgvnw7z98a9to8p.mp4 "Voxelized mass - excellent shape for wind effects")

[[section|slide]]

### Sectional Actor

[[section]]

text

[[section|slide]]

![fig|wide](img/explorations/sectionalVariation2.gif "Sectional mass - excellent shape for wind effects")

[[section|slide]]

### Figurative and Performative Optimization

[[section]]

text

[[section|slide]]

![fig|wide](img/explorations/fishTraining-2.gif "Sectional mass - optimization for wind effects and fish resemblanceSectional mass - excellent shape for wind effects")

