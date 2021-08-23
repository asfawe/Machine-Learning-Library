import matplotlib.pyplot as plt
import pandas as pd
from sklearn import (
    ensemble,
    preprocessing,
    tree,
)

from sklearn.metrics import (
    auc,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
)

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
)

from yellowbrick.model_selection import (
    LearningCurve,
)
url = (
    "https://biostat.app.vumc.org/"
    "wiki/pub/Main/Datasets/titanics.xls"
)
df = pd.read_excel(url)
orig_df = df

df.dtypes