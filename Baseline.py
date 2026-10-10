import numpy as np
#import torch
#import os
from pathlib import Path
import librosa
import pandas as pd


#debug = True

''' =====================================
            Editable Settings
    ====================================='''

#DATA_DIR = Path('/content/drive/MyDrive/trombone-pitch-tracker/data/raw/trombone') # for Colab
DATA_DIR = Path(__file__).parent / 'data' /  'raw' / 'trombone' # for local
RESULTS_DIR = Path('/content/drive/MyDrive/trombone-pitch-tracker/results')
INSTRUMENT = 'trombone'
A4_HZ = 440.0            # tuning reference used when recording (currently does nothing)
TUNER_TOLERANCE_C = 5  # e.g. 5, the tolerance of the tuner you played against, (5 = +- 5)
 
SR = 16000
HOP_LENGTH = 512
TRIM_S = 0.3             # dropped from each end of every file (attack and release)
FMIN_NOTE, FMAX_NOTE = 'E2', 'F5'
THRESHOLDS_C = [50, 20, 10]
AUDIO_EXTS = {'.wav', '.m4a', '.mp3', '.flac', '.aac', '.ogg'}

''' ====================================='''



def evaluate(pred_hz: np.ndarray, true_hz: np.ndarray, instrument: str) -> dict:
  assert len(pred_hz) == len(true_hz)

  keep = true_hz > 0
  pred = pred_hz[keep]
  true = true_hz[keep]

  cents = 1200 * np.log2(pred/true) #signed: +ve = sharp
  abs_cents = abs(cents)

  results = {'instrument': instrument, 'n_frames': len(abs_cents)}

  thresholds = THRESHOLDS_C

  for t in thresholds:
    results[f'within_{t}c'] = np.mean(abs_cents <= t)
  
  results['mae_cents'] = float(np.mean(abs_cents))
  results['median_cents'] = float(np.median(cents))

  n = np.round(cents / 1200)
  leftover = np.abs(cents - (1200 * n))

  results['octave_error_rate'] = np.mean((n!= 0) & (leftover <= 50))


  return results

def yin_pitch(audio):
  f0 = librosa.yin(audio, fmin=librosa.note_to_hz(FMIN_NOTE
  ), fmax=librosa.note_to_hz(FMAX_NOTE), sr=SR, hop_length=HOP_LENGTH)
  return f0

def score_instrument(instrument, pitch_method, metadata: pd.DataFrame):
  all_pred = []
  all_true = []


  for index, row in metadata.iterrows():

    path = DATA_DIR / f"{row['File']}.wav"
    audio = librosa.load(path, sr=SR, mono=True)[0]
    f0 = pitch_method(audio)

    times = librosa.times_like(f0, sr=SR, hop_length=HOP_LENGTH)
    keep = (times > TRIM_S) & (times < (audio.shape[0]/SR - TRIM_S))
    f0 = f0[keep]

    hz = librosa.note_to_hz(row["Note"]) * np.exp2(row["Cents"]/1200)

    true = np.full_like(f0, hz)
    all_pred.append(f0)
    all_true.append(true)

  all_pred = np.concatenate(all_pred)
  all_true = np.concatenate(all_true)

  results = evaluate(all_pred, all_true, instrument)
  return results

def YIN_test():
  instrument = ['trombone']


  # generate a 3s Bb3 tone

  sr = 16000
  duration = 3.0
  t = np.linspace(0, duration, int(sr * duration), endpoint=False)
  freq = librosa.note_to_hz('Bb3')
  audio = 0.5 * np.sin(2 * np.pi * freq * t)

  f0 = librosa.yin(audio, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'), sr=sr, hop_length=512)

  eval_results = evaluate(f0, np.full_like(f0, freq), instrument[0])


  return eval_results

def main():
  metadata_path = DATA_DIR / 'metadata.csv'
  results = score_instrument(INSTRUMENT, yin_pitch, pd.read_csv(metadata_path))


  print("Evaluation Results:", results)

if __name__ == "__main__":
  main()