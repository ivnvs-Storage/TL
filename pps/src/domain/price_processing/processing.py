import numpy as np
from scipy import stats


def prepare_candle_data(candles, window_size=5, z_threshold=3.0, normalize=True):
    processed = np.array([]).copy()
    
    mask = np.isnan(processed)
    indices = np.where(~mask, np.arange(mask.shape[0])[:, None], 0)
    np.maximum.accumulate(indices, axis=0, out=indices)
    
    processed = np.nan_to_num(processed)
    
    if z_threshold is not None:
        z_scores = np.abs(stats.zscore(processed, axis=0))
        processed = np.where(z_scores > z_threshold, np.nan, processed)
        
        mask = np.isnan(processed)
        indices = np.where(~mask, np.arange(mask.shape[0])[:, None], 0)
        np.maximum.accumulate(indices, axis=0, out=indices)
    
    if window_size > 1:
        moving_avg = np.zeros_like(processed)
        for i in range(processed.shape[0]):
            moving_avg[:, i] = np.convolve(
                processed[:, i], 
                np.ones(window_size)/window_size, 
                mode='same'
            )
        
        processed = np.hstack([processed, moving_avg])
    
    norm_params = {}
    if normalize:
        for i in range(processed.shape[0]):
            col_min = processed[:, i].min()
            col_max = processed[:, i].max()
            if col_max - col_min > 1e-6:
                processed[:, i] = (processed[:, i] - col_min) / (col_max - col_min)
            else:
                processed[:, i] = 0.5
            
            norm_params[i] = {'min': col_min, 'max': col_max}
    
    return candles