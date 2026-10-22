# ml-pitch-tracker
A CNN tool which tracks instrument pitch, giving players informative analysis on their intonation.

## Baseline: YIN on trombone (M1, 20 Oct 2026)

Test set: 36 long tones, E2 to C5, recorded on a phone (setup in `data/recording_log.md`).
True pitch = note + tuner reading. The tuner's green zone is ±5 cents, so the labels themselves are only good to about ±5 cents.

Silent frames are removed before scoring (frames more than 20 dB below the loudest frame, plus the first and last 0.3 s of each file). Scores are averaged across files, so each take counts equally.

| Method | within 50c | within 20c | within 10c | MAE (cents) | Median error (cents) | Octave errors |
|---|---|---|---|---|---|---|
| YIN (librosa) | 0.985 | 0.965 | 0.908 | 7.9 | +1.2 | 0.000 |

The worst take is Db3 (MAE 66 cents), which has a clang near the end of the file. Without it, MAE is 6.3 cents.

## Targets

- **Clean recordings:** match YIN (within 20c ≥ 0.96, octave errors 0). MAE is already close to the ±5 cent label noise, so it can't show a real improvement on this test set.
- **Noisy recordings:** beat YIN on within 20c and octave errors. A noisy test set still needs to be made.

## Data

Recordings from other players are not committed to this repo unless they give permission.
