from sklearn.feature_selection import mutual_info_classif
from src.features.build_features import run
from sklearn.feature_selection import SelectKBest


def select_features():

    X_train, X_test, y_train, y_test, feature_names = run()

    selector = SelectKBest(score_func=mutual_info_classif, k=20)

    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    selected_mask = selector.get_support() #boolean return 
    selected_features = feature_names[selected_mask]

    print("\nOriginal shape:", X_train.shape)
    print("Reduced shape:", X_train_selected.shape)

    return X_train_selected, X_test_selected, y_train, y_test, selected_features



if __name__ == "__main__":
    select_features()
