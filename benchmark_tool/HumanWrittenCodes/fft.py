import numpy as np

def fft_function(signal):
    """
    Perform FFT on a given signal and return the frequency and amplitude spectrum.

    Parameters
    ----------
    signal : 1-D array_like
        Input signal to be transformed.

    Returns
    -------
    fft_result : ndarray
        FFT of the input signal.
    """
    signal = np.asarray(signal, dtype=float)

    fft_result = np.fft.fft(signal)

    return fft_result
