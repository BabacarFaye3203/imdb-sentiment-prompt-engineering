import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


def evaluate_predictions(y_true, y_pred):

    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(
            y_true, y_pred, pos_label="positive"
        ),
        "recall": recall_score(
            y_true, y_pred, pos_label="positive"
        ),
        "f1_score": f1_score(
            y_true, y_pred, pos_label="positive"
        )
    }

    print("Evaluation Metrics")
    print("------------------")

    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))

    return metrics