"""Check the master dataset and saved retrospective predictions."""
from hashlib import sha256
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'Aquacast20Years_Weekly_UPDATED_TO_2026_10(2).csv'
EXPECTED_SHA256 = '6ee536b6e0051d087277726ae02ecc7d2bf23960752febc2160e6f884aa52485'
EXPECTED = {
    'E. coli': (65, 26, 7, 46),
    'Enterococcus': (78, 29, 11, 26),
}
FILES = {
    'E. coli': ROOT / 'outputs/e_coli/predictions/Ecoli_ONLY_final_test_selected_model_predictions.csv',
    'Enterococcus': ROOT / 'outputs/enterococcus/predictions/Enterococcus_ONLY_final_test_selected_model_predictions.csv',
}


def confusion_counts(actual, predicted):
    actual = np.asarray(actual, dtype=int)
    predicted = np.asarray(predicted, dtype=int)
    return (
        int(((actual == 0) & (predicted == 0)).sum()),
        int(((actual == 0) & (predicted == 1)).sum()),
        int(((actual == 1) & (predicted == 0)).sum()),
        int(((actual == 1) & (predicted == 1)).sum()),
    )


def main():
    source_hash = sha256(DATA.read_bytes()).hexdigest()
    assert source_hash == EXPECTED_SHA256, f'Input CSV hash does not match: {source_hash}'
    data = pd.read_csv(DATA, usecols=['indicator_clean', 'result_value'])
    assert len(data) == 1890
    for name, (total, limit, positives) in {
        'E. coli': (955, 400, 283),
        'Enterococcus': (935, 104, 225),
    }.items():
        subset = data.loc[data.indicator_clean.eq(name), 'result_value']
        assert len(subset) == total
        assert int((subset >= limit).sum()) == positives

        saved = pd.read_csv(FILES[name])
        pred_col = 'predicted' if name == 'E. coli' else 'prediction'
        cutoff_col = 'cutoff' if name == 'E. coli' else 'threshold'
        y, predicted = saved.actual.to_numpy(), saved[pred_col].to_numpy()
        assert len(saved) == 144
        assert (predicted == (saved.probability >= saved[cutoff_col])).all()
        tn, fp, fn, tp = confusion_counts(y, predicted)
        assert (tn, fp, fn, tp) == EXPECTED[name]
        print(f'{name:12s}  TN={tn:3d} FP={fp:3d} FN={fn:3d} TP={tp:3d}'
              f'  recall={tp/(tp+fn):.3f} precision={tp/(tp+fp):.3f}')
    print('Dataset identity and saved prediction metrics: verified.')


if __name__ == '__main__':
    main()
