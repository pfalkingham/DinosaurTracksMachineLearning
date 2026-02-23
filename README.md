**Project Overview**
- **Purpose:** This repo contains a small workflow to run the machine-learning approach used in [Lallensack, Romilio & Falkingham (2022)](https://royalsocietypublishing.org/rsif/article/19/196/20220588/90247/A-machine-learning-approach-for-the-discrimination) to predict affinities from dinosaur track silhouettes.

**Files**
- **`convertSihlouettes.ps1`**: PowerShell/ImageMagick script to standardize silhouette PNGs (trim, pad to square, resize, threshold).
- **`predict.py`**: Loads the trained model `tridactyl_tracks_nn_v1.h5`, reads PNGs from the `predict/` folder, runs the neural network, and writes `predictions.csv`.
- **`tridactyl_tracks_nn_v1.h5`**: Trained Keras model used by `predict.py`.

**Requirements**
- **OS:** Windows (scripts provided as PowerShell). The Python code is cross-platform.
- **System tools:** ImageMagick (`magick`) must be installed and on `PATH` for the PowerShell script.
- **Python packages:** TensorFlow (Keras), numpy, pandas, pillow, scikit-learn, matplotlib. Install with:

```
pip install tensorflow numpy pandas pillow scikit-learn matplotlib
```

**Quick Workflow**
1. Create a folder called `predict` in the repo root and put your silhouette PNGs there. Filenames with spaces will be renamed by the conversion script.
2. From PowerShell, change into the `predict` folder and run the conversion script to standardize images:

```
cd predict
..\convertSihlouettes.ps1
```

The script will trim whitespace, center the silhouette on a square canvas, resize it, and apply a threshold so each input is a 100x100 PNG suited for the model.

3. Run the prediction script from the repo root:

```
python predict.py
```

`predict.py` loads `tridactyl_tracks_nn_v1.h5`, processes every PNG under `predict/`, and writes the primary scores to `predictions.csv` in the repo root. The console will also print the `nn_model` column.

**Interpreting outputs**
- The model produces numeric scores per image (see `predictions.csv`, column `nn_model`). This project implements the approach from Lallensack et al. (2022); consult the paper for how to interpret model scores with respect to theropod/ornithopod affinity.

**Troubleshooting**
- If `magick` commands fail, ensure ImageMagick is installed and available on your `PATH`.
- If TensorFlow fails to import or the model won't load, check your Python version and TensorFlow installation.
- If no images are processed, ensure PNG files are placed in the `predict/` folder and have the `.png` extension.

**Citations / Credit**
- If you use this code or model in published work, please cite: [Lallensack, Romilio & Falkingham (2022)](https://royalsocietypublishing.org/rsif/article/19/196/20220588/90247/A-machine-learning-approach-for-the-discrimination) and acknowledge the model authors.
`Jens N. Lallensack, Anthony Romilio, Peter L. Falkingham; A machine learning approach for the discrimination of theropod and ornithischian dinosaur tracks. J R Soc Interface 1 November 2022; 19 (196): 20220588. https://doi.org/10.1098/rsif.2022.0588`

**Notes & Safety**
- This repo provides convenience scripts to run a pre-trained model. The model's predictions are probabilistic estimates and should be used with caution and expert interpretation.



