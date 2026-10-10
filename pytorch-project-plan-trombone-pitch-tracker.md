# PyTorch project plan: trombone pitch and intonation tracker

Sebastian Hoving | Written 8 October 2026 | Runs 12 October to 6 December 2026 (trombone to 22 November, then saxophones and trumpet)

Decisions made on 8 October: both weekly ML blocks go to this project; recordings are made on a phone; the tool must be usable by other trombone players, so week 5 produces a web demo; after trombone, the tool adds tenor and alto sax, then trumpet.

## Project summary

A small 1D CNN that estimates pitch from raw audio, compared against the classical YIN method, plus a web demo that plots how sharp or flat each note is. Trombone comes first, then tenor sax, alto sax and trumpet. It runs on free Colab (the laptop is a Surface Pro) and takes 8 weeks at 4 hours a week.

## Objectives

1. Apply the PyTorch Blitz skills to audio: custom Dataset, DataLoader, model, training loop, evaluation.
2. Compare a learned model against YIN on real playing.
3. Publish a repo with a README and a demo that other trombone players can use.
4. Extend the tool to tenor sax, alto sax and trumpet, each scored on its own test set.

## Scope

* **In:** one note at a time, recorded audio, pitch in cents, Colab notebooks, a simple web demo. Trombone in weeks 1 to 6; tenor sax, alto sax and trumpet in weeks 7 and 8.
* **Out:** live tracking while you play, full band audio, a mobile app, any other instrument. Slides between notes are a stretch goal only.

## Deliverables

* Labelled test set of trombone recordings (yours, then 2 other players)
* Labelled test sets for tenor sax, alto sax and trumpet (30 tones each, from bandmates)
* Synthetic tone generator and NSynth loader (brass, then reed)
* Trained model, evaluation script and results table (model against YIN, per instrument)
* Web demo: upload or record a clip, choose the instrument, see the intonation plot
* README on github.com/sebhoving

## Timeline and milestones

| Milestone | Description | Duration | Owner |
|---|---|---|---|
| M1 Baseline | Colab, Drive and repo set up; 30 labelled long tones recorded on a phone; YIN scored | Week 1 (12 to 18 Oct) | Seb |
| M2 Data | Tone generator with random harmonic strengths; NSynth brass subset; Dataset and DataLoader | Week 2 (19 to 25 Oct) | Seb |
| M3 Model v1 | 1D CNN on 1024 sample frames at 16 kHz; output of 360 pitch bins of 20 cents (6 octaves); trained on synthetic tones | Week 3 (26 Oct to 1 Nov) | Seb |
| M4 Model v2 | Add NSynth, noise and gain augmentation; error analysis, octave errors first | Week 4 (2 to 8 Nov) | Seb |
| M5 Demo | Intonation plot in a notebook first, then wrapped as a web demo; silence detection; 2 other trombone players try it | Week 5 (9 to 15 Nov) | Seb |
| M6 Write up | README, results table and CV bullet for trombone | Week 6 (16 to 22 Nov) | Seb |
| M7 Saxophones | Add the NSynth reed family and retrain; score tenor and alto sax test sets; check trombone scores have not dropped; add both to the demo | Week 7 (23 to 29 Nov) | Seb |
| M8 Trumpet | Score the trumpet test set; add it to the demo; update the README and results table | Week 8 (30 Nov to 6 Dec) | Seb |

## Team and roles

* **Seb:** owner of every milestone.
* **Claude:** planning, code review, debugging.
* **Trombone testers:** 2 other players in week 5 [you to name].
* **Recording players:** one tenor sax, one alto sax and one trumpet player, 30 tones each, due by 19 November [you to name]. Ask before keeping anyone's recordings as test data.

## Budget

* **Money:** £0 with free Colab, free Drive and a phone recorder. A paid Colab tier is optional if GPU access becomes unreliable [check the current price].
* **Hosting:** a Gradio app on Hugging Face Spaces is the candidate for the demo. It has had a free CPU tier; check it still does in week 5. You would create the account yourself.
* **Time:** 32 hours of ML blocks, plus about 15 minutes of recording inside practice sessions in weeks 1 and 5, and about 15 minutes from each bandmate.

## Recording guidance

Audio quality does not need to be high. The model works on 16 kHz mono, well below what any phone records, and other players will use phones, so phone recordings are the right test data. What matters:

1. No clipping. Brass and saxophones are loud: put the phone 1 to 2 metres away and to the side of the bell. If the waveform has flat tops, move further away.
2. A quiet room. A practice room is fine.
3. Turn off any enhance or noise reduction setting in the recorder app.
4. One note per file, 3 to 5 seconds, named by concert pitch (for example Bb2_01.wav). Save as WAV if the app allows.
5. Label quality matters more than audio quality. Hold each note in tune against a tuner on a second device or a clip on tuner, and write the tuner's tolerance in the README.
6. Use the same setup every time and note it in the README.

## Risks and mitigations

| Risk | Early sign | Mitigation |
|---|---|---|
| No true pitch for the recordings | Nothing to score against | Long tones against a tuner, labelled by note, tolerance stated in the README |
| Model does not beat YIN | Scores level after week 4 | Report it honestly, with where each method fails (noise, low notes, note starts) |
| Synthetic tones do not transfer to real audio | Good scores on synthetic, poor on recordings | Test on real recordings from week 3; add NSynth and augmentation in week 4 |
| NSynth labels are whole semitones | Cents scores look worse than they are | Use NSynth for training and coarse scoring only |
| Colab session resets | Lost work | Data and checkpoints on Drive; runs under an hour |
| Model fails on other players or phones | Good on your recordings, poor on theirs | Collect 10 tones from each tester in week 5 and report their scores separately |
| Web demo overruns week 5 | Notebook plot not done by the first block | Notebook first, web wrapper second; move M7 and M8 back a week before cutting the README |
| Bandmates' recordings arrive late | Nothing in hand by 19 November | Ask now, send them the recording guidance, and collect at a Thursday rehearsal |
| Written and concert pitch mixed up in labels | Scores wrong by a fixed interval for one instrument | Name every file by concert pitch and note the instrument's transposition in the data config |
| Adding reed data hurts trombone accuracy | Trombone scores fall after M7 | Run the trombone test set after every retrain; keep the week 6 checkpoint |

## Success metrics

* Share of frames within 50 cents and within 20 cents of the true pitch, per instrument
* Mean absolute error in cents
* Octave error rate
* Targets: [set after M1]. Starting point: match YIN on clean recordings and beat it on noisy ones.
* 2 other trombone players have used the demo, with their feedback logged
* Trombone repo public with README by 22 November
* Tenor sax, alto sax and trumpet each scored on a labelled test set by 6 December
* Hours logged against the 32 planned

## Tools and tech

Python, PyTorch, free Colab GPU, Google Drive, soundfile (loading audio), torchaudio (resampling only; its loading functions were removed in version 2.9), librosa (YIN baseline), mir_eval (pitch metrics), Matplotlib, Gradio (demo), Git and GitHub.

## First 7 days

1. Create the repo and a Colab notebook that mounts Drive.
2. In one practice session, record 30 long tones across your range against a tuner. Follow the recording guidance above.
3. Write the evaluation script: predicted and true pitch in, the metrics above out, reported per instrument.
4. Run YIN on the 30 tones and log its scores.
5. Ask bandmates: 2 trombone testers, plus a tenor sax, an alto sax and a trumpet player to record tones.
6. In the Sunday review, write the targets into the README.

## First 30 days

* **Day 14:** generator and loaders tested.
* **Day 21:** model v1 trained and scored on synthetic and real audio.
* **Day 30:** model v2 and error analysis done. Decide whether week 5 goes to the demo or to fixing accuracy.

## Other instruments: evaluation

**Verdict:** easy to build, and the real cost is testing. A pitch model of this kind does not depend on the instrument if its output range and training data are broad. What each new instrument needs is a labelled test set, because an instrument should not be claimed in the README until it has been scored.

### The three chosen instruments

All three sit inside the model's 33 Hz to 1,976 Hz range, so the model design does not change. Ranges are approximate.

| Instrument | Key | Sounds | Concert range | Training data | Extra work |
|---|---|---|---|---|---|
| Tenor sax | Bb | A major ninth below written | Ab2 to E5 | Needs the NSynth reed family | About 5 hours for both saxophones together |
| Alto sax | Eb | A major sixth below written | Db3 to Ab5 | Same reed data as tenor | Shared with tenor |
| Trumpet | Bb | A major second below written | E3 to Bb5, higher for lead players | Already covered by the brass family | 2 to 3 hours |

The two saxophones share one retrain, so the separate cost per instrument is its test set and its transposition setting. Trumpet is the cheapest of the three, because the brass data is already in the model from week 4. If a trumpet player's tones are in hand early, trumpet could be scored in week 6 and the saxophones could keep week 7.

### What depends on the instrument

* **Pitch range.** A tenor trombone covers about E2 to F5, lower with pedal notes. 360 bins of 20 cents cover 6 octaves, about 33 Hz to 1,976 Hz, which holds the fundamentals of nearly every instrument except the top of the piccolo, violin and piano.
* **Timbre.** Set by the training data. The tone generator randomises harmonic strengths, and NSynth groups its notes into families (bass, brass, flute, guitar, keyboard, mallet, organ, reed, string, synth lead, vocal), so adding one is a change to a filter.
* **Display.** Transposing instruments need a written or concert pitch setting. Ensembles tune to different references, so the reference needs a setting too (A = 440 Hz by default).
* **Test data.** About 30 labelled tones per instrument from a player, or a public set with pitch labels such as URMP [check its contents and licence].

### Effort by instrument group

Hours are estimates.

| Group | Examples | Extra work | Why |
|---|---|---|---|
| Other brass | Trumpet, horn, euphonium, tuba | Low: 2 to 3 hours each | Same sustained single note sound. Record a test set, add transposition. Low tuba notes raise octave errors |
| Woodwind | Sax, clarinet, flute, oboe | Low to medium: 3 to 4 hours each | NSynth has reed and flute families. Breath noise on flute needs checking |
| Bowed strings and voice | Violin, cello, singing | Medium: 6 to 10 hours | Vibrato and slides make the true pitch ambiguous, so the labels and the plot both need rethinking |
| Plucked and struck | Guitar, piano | High: out of scope | Notes decay fast and are usually played several at once, which is a different problem. A pianist cannot adjust intonation anyway |
| Unpitched percussion | Drums | Not possible | No pitch to track |

### Design choices to make now (about 1 extra hour in total)

1. Output covers the full 6 octaves, not just the trombone's range (M3).
2. The tone generator randomises harmonic strengths, so it is not trombone specific (M2).
3. A data config lists the NSynth families in use and each instrument's transposition, starting with brass (M2).
4. The evaluation script reports scores per instrument (M1).
5. The demo has two settings: instrument (sets transposition and note names) and reference pitch (M5).
6. The README claims an instrument only once it has a labelled test set (M6 to M8).

## Templates

* **Project brief:** Name | One sentence goal | Owner | Start and end dates | Hours | Success test | Out of scope. The summary above is a filled example.
* **Milestone checklist:** [ ] Done criterion met. [ ] Notebook runs top to bottom in a fresh session. [ ] Results in README. [ ] Hours logged. [ ] Pushed to GitHub.
* **Risk log entry:** one row of the risk table, plus Owner and Status.
* **Gantt:** the milestone table, one row per week.

## Assumptions

* Both ML blocks go to this project until 6 December [confirmed to 22 November on 8 October; confirm the extra 2 weeks].
* Free Colab GPU access stays available.
* The frame size and pitch bins follow the CREPE model and are a starting point.
* Readers of the write up are engineers and recruiters in software and AI.

## Open questions

1. Which 2 trombone players will test the demo in week 5?
2. Who records the tenor sax, alto sax and trumpet tones?
3. Do the ML blocks stay on this project until 6 December?

## Notes

1. Chosen on 8 October from five evaluated options. Its employer link is the weakest of the five (music and audio technology firms in software and AI). The planned follow up is the solar generation forecaster on Open Climate Fix's uk_pv data, which reuses the 1D CNN and training loop. Adding weeks 7 and 8 moves that follow up to after 6 December.
2. NSynth, URMP and CREPE details, and the instrument ranges, are from memory. Check them before relying on them.
3. Do not put this project on a CV or in a letter until there are results to quote.
