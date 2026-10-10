import numpy as np
import torch
import os
from pathlib import Path
import librosa

debug = True
def evaluate(pred_hz: np.ndarray, true_hz: np.ndarray, instrument: str) -> dict:
  assert len(pred_hz) == len(true_hz)

  keep = true_hz > 0
  pred = pred_hz[keep]
  true = true_hz[keep]

  cents = 1200 * np.log2(pred/true) #signed: +ve = sharp
  abs_cents = abs(cents)

  results = {'instrument': instrument, 'n_frames': len(abs_cents)}

  thresholds = [50, 25, 10]

  for t in thresholds:
    results[f'within_{t}c'] = np.mean(abs_cents <= t)
  
  results['mae_cents'] = np.mean(abs_cents)

  n = round(cents / 1200)
  leftover = abs(cents - n)

  count = 0
  for i in range(len(n)):
    if n[i] != 0 and leftover <= 50:
      count += 1
  results['octave_error_rate'] = count/len(n)


  return results

SR = 16000
HOP_LENGTH = 512
TRIM_S = 0.3

def yin_pitch(audio):
  f0 = librosa.yin(audio, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'), sr=SR, hop_length=HOP_LENGTH)
  return f0

def score_instrument(files, instrument, pitch_method):
  all_pred = []
  all_true = []

  for au_file in files:
    audio = librosa.load(au_file, sr=SR, mono=True)[0]
    f0 = pitch_method(audio)

    times = librosa.times_like(f0, sr=SR, hop_length=HOP_LENGTH)
    keep = (times > TRIM_S) & (times < (audio.shape[0]/SR - TRIM_S))
    f0 = f0[keep]

    note = Path(au_file).stem.split('_')[0]
    true = np.full_like(f0, librosa.note_to_hz(note))
    all_pred.append(f0)
    all_true.append(true)

  all_pred = np.concatenate(all_pred)
  all_true = np.concatenate(all_true)

  results = evaluate(all_pred, all_true, instrument)
  return results