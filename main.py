"""A small starting point for machine learning experiments."""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def main() -> None:
    """Train and evaluate a model on a built-in dataset."""
    features, labels = load_iris(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state=42, stratify=labels
    )
    model = LogisticRegression(max_iter=200)
    model.fit(x_train, y_train)
    print(f"Iris test accuracy: {model.score(x_test, y_test):.1%}")


if __name__ == "__main__":
    main()
