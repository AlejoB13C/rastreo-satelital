# Proyecto Rastreo Satelital Team 56

Proyecto del equipo 56 de DS4A Colombia Cohort 6 con Rastreo Satelital
Created by:
Alejandro Borda @AlejoB13C
Alejandro Yepes @ayepesp
Alejandro Ceren @alejoceren
David Niño @dmateons
Luis @1treu1
Nicolas @Jonigaro

## Installation guide

Please read [install.md](install.md) for details on how to set up this project.

## Project Organization

    ├── LICENSE
    ├── README.md               <- The top-level README for developers using this project.
    ├── install.md              <- Detailed instructions to set up this project.
    ├── auto-install.py         <- File to auto set up environment and extensions for this project.
    ├── tasks.py                <- Invoke with commands like`notebook`.
    ├── setup.py                <- Makes project pip installable (pip install -e .)
    │                               so proyecto_rastreo_satelital_team_56 can be imported.
    ├── requirements.txt        <- The requirements file for reproducing the analysis environment using`pip`.
    ├── environment.yml         <- The requirements file for reproducing the analysis environment using`conda`.
    │
    ├── .env                    <- The file for project environment variables.
    ├── .gitignore
    ├── .here                   <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── references              <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures             <- Generated graphics and figures to be used in reporting.
    │
    ├── models                  <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── data
    │   ├── external            <- Data from third party sources.
    │   ├── interm              <- Intermediate data that has been transformed.
    │   ├── processed           <- The final, canonical data sets for modeling.
    │   └── raw                 <- The original, immutable data dump.
    │
    ├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                       the creator's initials, and a short`-` delimited description, e.g.
    │   │`1.0-jqp-initial-data-exploration`.
    │
    └── proyecto_rastreo_satelital_team_56   <- Source code for use in this project.
    ├──__init__.py         <- Makes proyecto_rastreo_satelital_team_56 a Python module.
    │
    ├── data                <- Scripts to download or generate data.
    │   └── make_dataset.py
    │
    ├── features            <- Scripts to turn raw data into features for modeling.
    │   └── build_features.py
    │
    ├── models              <- Scripts to train models and then use trained models to make
    │   │                       predictions.
    │   ├── train_model.py
    │   └── predict_model.py
    │
    ├── utils               <- Scripts to help with common tasks.
    │   └── paths.py        <- Helper functions to relative file referencing across project.
    │
    └── visualization       <- Scripts to create exploratory and results oriented visualizations.
    └── visualize.py

---

Project based on the [cookiecutter conda data science project template](https://github.com/AlejoB13C/cookiecutter-docker-ds).
