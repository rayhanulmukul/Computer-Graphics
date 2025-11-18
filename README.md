# CSE4221 – Computer Graphics Laboratory

This repository contains the full implementation suite for **CSE4221: Computer Graphics**, including algorithmic simulations, graphics primitives, geometric transformations, and fractal rendering workflows.

Each task aligns with the official lab manual and is structured for direct execution, academic review, and portfolio demonstration.

---

## Repository Structure

```
Computer-Graphics/
│
├── 00_WarmUp_NationalFlag/
├── 00_WarmUp_NameAnimation/
├── 00_WarmUp_SpaceTravel/
│
├── 01_Hidden_Surface_Elimination/
├── 02_Cohen_Sutherland_LineClipping/
├── 03_Sutherland_Hodgman_PolygonClipping/
├── 04_Bezier_Curve/
├── 05_2D_Transformations/
├── 06_Bresenham_LineDrawing/
├── 07_Bresenham_CircleDrawing/
├── 08_Fractal_Snowflake/
│
└── Question.pdf
```

---

## Lab Portfolio

### Warm-Up Modules

* **National Flag of Bangladesh** – Basic raster rendering
* **Animated Name Rendering** – Text animation pipeline
* **Space Travel Scene Simulation** – Motion + layered perspective

### Core Experiments

**01 – Hidden Surface Removal / Visible Surface Detection**

* Depth-based surface resolution simulation

**02 – Cohen–Sutherland Line Clipping**

* Region code assignment, bitwise clipping

**03 – Sutherland–Hodgman Polygon Clipping**

* Edge-based iterative vertex processing

**04 – Bezier Curve Rendering**

* Parametric polynomial evaluation

**05 – 2D Geometric Transformations**

* Translation, rotation, scaling matrices

**06 – Bresenham Line Drawing**

* Incremental rasterized line generation

**07 – Bresenham Circle Drawing**

* Midpoint algorithm variant for circular primitives

**08 – Snowflake via Fractal Geometry**

* Recursive fractal subdivision

---

## Technology Stack

C / C++, OpenGL / GLUT, Mathematical Graphics Pipeline

---

## Execution

```
g++ filename.cpp -lGL -lGLU -lglut -o output
./output
```

---

## Academic Attribution

CSE4221 Laboratory
Department of Computer Science & Engineering
University of Rajshahi
