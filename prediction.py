import joblib
import features_extraction
import sys
import numpy as np

from features_extraction import LOCALHOST_PATH, DIRECTORY_NAME


def get_prediction_from_url(test_url,html):
    features_test = features_extraction.main(test_url,html)
    features_test = np.array(features_test).reshape((1, -1))

    clf = joblib.load(LOCALHOST_PATH + DIRECTORY_NAME + '/classifier/random_forest1.pkl')

    pred = clf.predict(features_test)
    return int(pred[0])

if __name__ == "__main__":
    main()
