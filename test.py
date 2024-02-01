import time
import pymiere
from pymiere import wrappers

# Check for an open project
project_opened, sequence_active = wrappers.check_active_sequence(crash=False)
if not project_opened:
    raise ValueError("please open a project")

project = pymiere.objects.app.project

# Open Sequences in Premiere Pro if none are active
if not sequence_active:
    sequences = wrappers.list_sequences()
    for seq in sequences:
        project.openSequence(sequenceID=seq.sequenceID)
    # Set the first Sequence in the list as the active Sequence
    project.activeSequence = sequences[0]

# List all videos clips in the active Sequence
clips = wrappers.list_video(project.activeSequence)
clip2 = pymiere.objects.app.project.activeSequence.videoTracks[0].clips[0]
clips0 = clips[0]

# Convert timebase in ticks per second to Frame Per Second (FPS)
fps = 1/(float(project.activeSequence.timebase)/wrappers.TICKS_PER_SECONDS)
print("Sequence as a framerate of {} fps".format(fps))

# Select the first video clip in the Timeline
print(clips[0].setSelected(True, True))
